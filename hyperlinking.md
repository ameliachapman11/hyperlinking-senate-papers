# Automating Hyperlinking
## Goal and Overview
### Goal
One of the primary goals of this project is to research how adding hyperlinks between Senate papers may be automated. For the purpose of the prototype, we will be focusing on a subsection of the wider document library, looking only at the Senate and Education Committee (SEC) papers for the 2023-2024 academic year.

There is currently a lack of existing technologies that can automatically detect references between a set of papers and generate hyperlinks between them, so a custom workflow/logic has to be implemented. 

### Paper Codes and File Names
The hyperlinks will be widely based on paper codes, whose notation provides information about the committee, academic year, meeting number, and paper number. For instance, a paper code of S 23/24 3D indicates it is a Senate document (denoted by S), part of the 2023-2024 academic year (denoted by 23/24), part of the third meeting (denoted by the 3 in 3D), and is the fourth document in that meeting (denoted by the D in 3D). The papers for each meeting follow alphabetical order, with A being the first paper, B being the second paper, and so on. In the hyperlinking process, the information gathered from a paper code will used to identify the metadata of another paper and generate a link to it.

The documents also follow a strict naming schema which provides information about committee, paper type, and meeting date/duration (as electronic meetings take place over multiple days. The committee abbreviations are SEN for Senate and SEC for Senate Education Committee. They are as follows: 
* Meetings on a single day:
   * Agendas and papers: `&lt;committee-abbreviation&gt;\_AP\_&lt;date of meeting&gt;.pdf`
   * Minutes: `&lt;committee-abbreviation&gt;\_M\_&lt;date of meeting&gt;.pdf`
* Meetings over multiple days (electronic):
   * Agendas and papers: `&lt;committee-abbreviation&gt;\_AP\_&lt;start&gt;_&lt;end>_e.pdf`
   * Minutes: `&lt;committee-abbreviation&gt;\_M\_&lt;start&gt;_&lt;end&gt;_e.pdf`

### Hyperlink Locations
The following are particular places in which hyperlinks should automatically be added:
* Each item in the minutes should link back to the item in the agendas and papers, based on the paper code
* Each item in the agenda and papers should link to the item's reference in the minutes, based on the paper code
* Any other references of a specific paper code should link to the relevant document in the agendas and papers
* Obvious references between papers such as is in the E-Senate *Agenda and Papers* file from the September 23-27, 2023 session of the E-Senate: section e-S 23/24 1B mentions that the "Senate Quality Assurance Committee (SQAC) considered the paper at its meeting on 12 September 2023."

</br>

## Alternative Forms of Storing Files
Editing the source PDF file can result in breaking structural integrity and corrupting existing formatting. We want to instead keep the source PDF as an original, unaltered document, and produce a new hyperlinked version which users can reference to speed up research time. The final hyperlinked version of the document will likely be rendered as HTML rather than being converted back to a PDF. Rendering an alternative method of file storage (XML or JSON) as PDF would require using HTML as an intermediary stage, so it is easier to stop at HTML rather than converting original PDF &rarr; XML/JSON &rarr; HTML &rarr; PDF.

### XML as an Intermediary File Stage
Using XML as an intermediary file stage allows for custom tagging schema which can be helpful in locating text elements like headings, which can then identify the start of a paper. The metadata can be stored as dedicated elements at the top of the file, such as `<committeeName>SEN<\committeeName>`. XML also naturally supports mixed content, which makes it easy to replace reference with an inline link using an href/target tag. This can then be rendered cleanly to html as an `<a>` tag. The possible downside of using XML is that is is slower than something like JSON and can result in a larger file size.

### JSON as an Intermediary File Stage
With JSON, metadata would be stored as key-value pairs (for example, "committeeName": "SEN") and there would be nested objects for sections/items. Although JSON does not offer custom tagging in the traditional sense like XML, it is possible to create custom field names and nested structures to represent the same ideas. JSON is particularly well known for API's and is also faster than XML. However, the main downside of using JSON is adding hyperlinks, which is important to this applicaiton. Since text in JSON is usually stored as a single flat string, adding an inline link requires breaking the string into arrays of text fragments and link objects. This is more awkward to generate and maintain when compared to XML.

### Conversion Directly to HTML
If we skipped using an intermediary file storage and instead rendered the hyperlinked file directly as HTML, a few issues arise. First, we would have to encode structure as CSS classes rather than with custom tags, which makes it harder to query. Second, if we later need to add a new field to the schema or alter the HTML structure, it would require regenerating everything from the PDF rather than just re-rendering the XML, which is a slower process. Finally, injecting the generated hyperlinks into the HTML requires using regex matching over the whole HTML file, which is error prone. Although eliminating an intermediary step would result in a cleaner workflow, it is more difficult to create a well-structured file for processing text and creating hyperlinks.

### Recommendation
The best choice for alternative file storage beyond PDF's is to use XML, and later to generate HTML from this. The flexibility that XML offers for custom structure will be helpful for querying paper contents and generating hyperlinks. It will be easier to query and maintain than direct converson to HTML, and will be easier to insert inline links than JSON.

The following is an example of how a custom XML schema may be implemented to contain the relevant metadata, paper structure, etc:
```
<committeeDoc>
<documentType> AP <\documentType>
<committeeName> SEN <\committeeName>
<committeeMeetingData> 2024-05-22 </committeeMeetingData>
<committeeYear> 2023/4 </committeeYear>
<meetingNumber> 3 </meetingNumber>
<items>
<agendaItem number="1" paper = "S 23/24 3A">
<metadata> ... </metadata>
<content> ... </content>
<\agendaItem>
     ...
     ...
<\items>
<\committeeDoc>
```

</br>

## Conversion from PDF to XML

### Python library evaluation
The first step of converting from PDF to XML is extracting the text with awareness of what may be a header, paper code, body paragraph, etc. There are a wide variety of Python libraries which are targeted towards text extraction of PDF files. The following is a description of some of the most popular ones:

PyMuPDF:
* Wraps the MuPDF rendering engine
* Main strengths:
   * Runs on C so faster than other libraries
   * Good at extracting text with positional data and font information, rendering PDF’s as images, image extraction
* For server-side use requires either open-sourcing your code or purchasing a commercial license from Artifex &rarr; this should not a problem for our application as it will be publicly available

pdfminer.six
* Python 3 fork of the original pdfminer library
* Main strengths: character-level extraction, extracting text with positional data and font information, no dependencies
* Downsides: slower than PyMuPDF since it processes at the character level, lacks table detection

Pdfplumber
* Built on top of pdfminer.six
* Main strengths: table extraction, character-level extraction, extracting within a specified region of a page 
* Downside: slower than PyMuPDF since it processes at the character level, no PDF writing/merging

Pypdf
* Main strengths: merge/split, zero dependencies
* Downside: does not return positional and font data, has trouble with complex layouts and multicolumn text, more basic than other options

Unstructured
* Creates semantically labelled chunks (Title, Paragraph, etc.) by applying rule-based heuristics
* Downside:
   * Although it retains data about position, does not retain information about font
   * Requires rendering the PDF page as an image and using AI to extract a table (higher computational cost)

**Overall recommendation:** 
If a Python library is used for text extraction and PDF conversion, the best option is to use PyMuPDF. PyMuPDF returns detailed information about the text, including the font name, font size, and whether it is bolded/italicized, without compromising speed. As there are many instances of tables throughout the Senate papers, we need to include this ability in our consideration. Although PyMuPDF is considered to be weaker in terms of table extraction than pdfplumber, it includes a `find_tables()` function which handles text wrapping inside explicit grid lines well, which is our primary use case. If tables are being flattened badly, it is possible to later integrate pdfplumber, but using PyMuPDF alone is the best starting place.

### Alternatives to Python Libraries
**Apache Tika:**
* Java-based content extraction toolkit designed to pull text and metadata out of many file types, including PDFs
* Implementation in the pipeline: would just be used for text extraction, cannot also automatically convert to PDF
* Main strengths: can run as a server so the app can send PDFs to it automatically
* Downside: information about font and layout is flattened/lost, still need to implement post-processing logic about whether or not a paragraph continues across the page *(see Conversion Pipeline)*

**GROBID:**
* Open-source machine learning library designed to parse documents into structured XML
  * Uses TEI (Text Encoding Initiative), a standardized format/XML vocabulary commonly used in the digital humanities
* Primarily intended for scholarly papers and journal articles
* Main strengths: can be used for outputting XML, not just for extracting text, can handle paragraphs across multiple pages
* Downside: would still need to be mapped to a custom schema, information about font and layout is flattened/lost, more computationally heavy because it is ML-based

**Overall recommendation:**
Stick with PyMuPDF. Tika is best for text-extraction applications when you do not know what type of file you are dealing with ahead of time&mdash;it normalizes everything into standard XHTML. However, since we know ahead of time that we are only dealing with PDFs, PyMuPDF provides more information about the text (including font and position), which enables precise control about what becomes what type of text becomes what type of XML tag. 

While GROBID has the advantage of going straight to XML with a standardized schema, to really benefit from it offers, it would be better to convert from using a custom schema to using TEI. The metadata included at the top could be included in the `<teiHeader>` tag. However, there is no guarantee that TEI would fit well with the structure of the Senate paper documents&mdash;would it be able to section the different papers based on paper code, for instance? GROBID provides uncertainty, while we know a custom schema fits the strcutre of the documents precisely.

### Structure of Extraction in PyMuPDF
Extracted text in PyMuPDF follows a specific hierarchy: Page → Block → Line → Span (meaning spans are within lines which are within blocks, ...). A span is a span of words with consistent styling (font, font size, bold/italic, etc.). The maximum length of a span is an entire line. A line is a horizontal row, like a line of text. A block is the highest level of text organization on a page, and usually represents a structural element like a paragraph, a column of text, a header, or an image.

### Building an XML Tree (lxml)
While PyMuPDF provides the ability to recognize precise structure of the document, it cannot natively create an XML document with a custom schema from this information. From the font and positional data provided by PyMuPDF, we need to create rules to identify certain elements of the paper. For example, the combination of a larger font + bold + in top right corner of page = paper code. Or small text + bottom of page = footer. From the identified element, we can add in the desired XML tag with the extracted text from that section.

As XMLs follow a nested tree structure, we have to keep track of where the opening and closing tags should be. One method of keeping track of where the tags should start and end is by using a stack. However, a cleaner method would be to use lxml, a Python library used for processing XML/HTML. lxml manages the open/close tags for you by building an in-memory tree structure, which eliminates the need for a stack. It also provides the advangtage of automatically converting PDF text containing characters like &, <, or > into an XML-friendly format. You can also modify the tree dynamically, meaning you can change tag names along the way instead of having to redo the entire stack. When the document is ready to be finished, lxml automatically handles the serialization to XML. 

As lxml cannot read/parse PDF files on its own, it must be used in combination with one of the previously mentioned Python libraries, such as PyMuPDF.

**XPath support:** lxml offers has full XPath support. XPath is a querying language much like SQL which is used to identify and extract information from particular parts of an XML document, and relies on XML tags. XPath will be useful for searching for specific tags when finding places to inject hyperlinks. For instance, we should not be inserting a hyperlink at every instance of a paper code; for the actual paper, they are repeatedly used as a header. With XPath, we could specifically query instances of a papercode that are *not* within a header tag. 

**lxml structure:** When creating an XML tree using lxml, the root of the document is created with an `Element` object. A branch/child node is then added with a `SubElement` object, which allows for a detailed nested structure. SubElements can take on custom attributes which may be helpful for storing metadata. An example of creating a new `SubElement` object is say we have identified a paper code in the header based on large font size and location in upper right corner. If we see that it is a new paper code, indicating the start of the next paper, we can add `etree.SubElement(root, "paper", paperCode="S 23/24 3D")` which will create the tag `<paper paperCode="S 23/24 3D"> ... </paper>` in the final XML file.  

### XML Validation
A major concern when creating the XML documents is how do to ensure the generated tree fits the desired schema&mdash;how do we prove the generated document is correct? This can be achieved through the creation of an XSD (XML Schema Definition) file. XSD files are XML files which dictate the structure, data types, and rules for an XML document. The XML document can be linked to the relevant XSD, much like how you link to a CSS file at the top of an HTML file.

### Conversion Pipeline
1. Extract blocks with PyMuPDF
2. Combine blocks across pages where there is a continued paragraph
3. Classify each block based on custom tags
4. Add a `SubElement` in lxml for the relevant block classification
5. Serialize to XML once all of the document has been processed
6. Validate XML construction using XSD file

*Note:* Based on the hierarchy of how PyMuPDF extracts text, blocks are limited within the page. This may occasionally cause a paragraph to be broken off into two blocks if it continues over the page line (as it will not be detected as a continuation of the same block by the library). The suggested solution is to perform a post-processing step once the library has extracted the text to combine blocks together that seem to be part of the same paragraph, likely based on if the next block starts with lowercase or the previous block does not end with punctuation. Another method would be to start from spans, then combine into lines, then combine into blocks. In other words, create custom blocks rather than relying on the library's built in detection.

*Note:* We are likely going to have to define different procedures for creating the XML the different types of documents, as there are some structural differences between the minutes versus the agendas and papers. There is also some variation within the document types themselves&mdash;some minutes use tables while others use lists. This is particularly relevant when creating the XSD to validate the generated file.

</br>

## Workflow (CMS version)
**Note:** In the following workflow, it is assumed that the recommended build approach of using a CMS such as Drupal and a search engine such as Apache Solr is taken, as detailed in the [Build Approach](buildApproach.md) file. It is also assumed that the recommendation of using PyMuPDF and lxml is used, as suggested in the *Conversion from PDF to XML* section.

### 1. Upload Each Paper Into the CMS
Each PDF paper will be stored in the content management system as the original authoritative document.

### 2. Trigger Processing Pipeline
Once the PDF is uploaded, the CMS will trigger a backend processing job, which can either be done immediately or added to background queue. Taking Drupal as an example, a custom Drupal module will need to be developed using PHP and YAML files which tells the CMS that once the file is uploaded to execute the rest of the workflow.

### 3. Extract Metadata From File Name and Add to CMS
As detailed in the *Paper Codes and File Names* section, the file names of the PDF's follow a strict naming convention. We can take advantage of this to extract metadata information by using regex matching, which can then be attached to the file in the CMS. 

### 4. Convert from PDF to XML
Convert each PDF to structured XML with a custom schema using PyMuPDF and lxml, as described in the *Conversion from PDF to XML* section. We will also include a `xml:id` at the beginning of each agenda, paper, minute item, etc. which will be used later when creating links. `xml:id` is a standard attribute used to assign unique identifiers to elements in an XML document and can be rendered as HTML IDs (a unique id for an HTML element). We will need to a define a custom naming schema for the ID's, likely largely based on the file name convention. 

### 5. Store the XML file in the CMS 
Add the XML extracted version of each paper into the CMS and inherit metadata from the parent PDF paper. This should be done alongside the original paper instead as a replacement. It may be helpful to include an extra metadata field for the XML to show which parent PDF it comes from, perhaps the file name.

### 6. Generate Deterministic Links for Obvious Matches
There are many instances where a paper will refer to another paper explicitly by paper code; in this case, it is easy to link them together. We can take advantage of the XML ID's previously added to generate the hyperlink. Through the standard naming schema of the paper code, we can identify which document is being referenced by metadata, take the file name, and append `#unique-id` to generate a hyperlink to that specific section. 

An example is `xml:id = "S_23/24_3F"`. We can identify this belongs to the file `SEN_AP_20240522`, so the generated hyperlink would be `SEN_AP_20240522.html#S_23/24_3F`. Note that the filepath includes `.html` instead of `.pdf` or `.xml`, as we want it to link to the correct spot in the HTML once the XML is rendered as HTML.

The logic for matching agenda and minute items versus other explicit references to paper codes will be slightly different. For example, each item in the agenda should link back to the item in the minutes. If we kept the same logic as other references, we would like to the paper code later in the same Agenda & Papers instead of to the minutes as desired. This would likely be a good use of XPath to specify that for certain tags, it should follow a certain logic.

### 7. Prepare Documents To Send to Solr
Search engines such as Apache Solr store documents in a core or a collection, which acts like a database. Documents consist of multiple fields, which can include the text of the document itself along with various metadata fields. We have to prepare records to be sent to the search engine before it can be stored and indexed. For each document, we should include parent file metadata (including unique parent document ID) and the actual XML file. 

Solr only automatically parses XML if it is in Solr's native XML format (with specified fields). Since we are using a custom XML schema, we need to convert to Solr update XML schema, which flattens our XML into a searchable version usable by Solr. "Flattening" our XML means getting rid of the nested structure, and instead consists of `<field>` tags within a larger `<doc>`. We can add our custom tag name back into the `name` attribute of the `field` tag. 
* *Note: instead of converting to Solr update XML, we could alternatively convert to JSON but it feels more logical to stick with XML*

We will have to create one Solr document per whole paper and one per logical section (ex. for a specific paper within a wider SEC meeting). The smaller units can be identified through the XML tags we have already created through our custom schema. The document per whole paper will be used for keyword search functionality, when a user searches a keyword/keyword phrase and the application will return the most relevant documents. The document per section will be used when linking more ambiguous references between Senate papers. Since we will have multiple document types, it may be helpful to add an extra metadata field to denote record type so that when you are querying Solr you can specify whether you want to search unit-level or document-level. This may be done through something like `record_type = document` or `record_type = section`. 

### 8. Send for Indexing
When you send documents to a search engine, they are automatically added to the core/collection and indexed. A document being indexed means that it is broken down into searchable terms and organized it into a data structure much like an index in a back of a textbook, where you can search up a word and it tells you relevant pages. We can verify that records have been correctly added and with the correct metadata by opening the Solr Admin UI and running a query for known metadata.

### 9. Resolve Additional/Ambiguous Links Using Unit-Level Search
After indexing, we will query the unit-level Solr records to find the best target unit for harder references that were not resolved by explicit rules. In general terms, these will be references where a specific committee and meeting date is listed, but a specific paper code is not included.

**Practical example:** Say that there is a phrase in a Senate paper that says "...the October 2024 meeting of the APRC..." and elsewhere in the sentence it mentions "the School of Literatures, Languages, & Cultures." In the paper for the October 2024 meeting of the APRC, the search engine will find the section/paper most relevant to literature, languages, and cultures and return it. This is the proposed section to be hyperlinked.

This task can further be broken down into subtasks:
* Detect candidate references to other papers
* Match each reference to a target paper by metadata matching (committee, date)
* Extract the local context around the reference (current sentence, hearby sentences, current section heading)
* Find most relevant target section by querying the target paper with the local context
* Generate hyperlink to that specific section
* Apply confidence rule *(see below)*
* Inject hyperlink back into HTML

*Note: although the original XML document will be changed, we do not need to resend the document to Solr because the text has been flattened, which will not include hyperlinks*

**Confidence Rule:** Although we have found a proposed section to hyperlink to, this should not be accepted blindly. Instead, the backend should implement a confidence which only creates a section-level link if one section is clearly the best match, and creates a link to the start of the document if the match is weak. Possible ways of identifying a "good match" are heuristic rules using the relevance score of the top result, the gap between scores of the top and second result, whether an exact phrase or heading terms matched, etc.

### **10. Render XML as HTML

### **11. Add Final HTML to Frontend

### TO DO: FINISH ADDING STEPS 

</br>

## Possible Usage of an AI Agent
At present, the outlined workflows only identifies obvious references between Senate papers. A possible expansion to this application is identifying ambiguous references, references with inconsistent phrasing, and hyperlinking to a wider domain of sites (perhaps to other sites within the University of Edinburgh ecosystem). This could be possible through an AI agent, which can be implemented either using an API (proprietary) or a local model (open-source). The agent could also be added in to a specific part of the workflow, such as partitioning/sectioning text from the PDF documents when being converted to XML.

A possible concern with using an AI agent is higher cost and that the agent should not add hyperlinks blindly, which again brings up the issue of an admin staff.

</br>

## AI Acknowledgement
ELM, the University of Edinburgh's official AI innovation platform, was used throughout the research process to understand possible ways of automating hyperlinking, provide suggestions for the workflow, and gain further understanding of how each step would be implemented on the backend. ELM was set to be GPT 5.4 for the model, and web search was enabled. AI was used as a suggestion rather than a final decision point for the workflows, with deviations particularly made in the XML version of the workflow. All descriptions were written by hand.

I would also like to acknowledge my advisor for writing the example XML schema and explanation of the structure of file names.
