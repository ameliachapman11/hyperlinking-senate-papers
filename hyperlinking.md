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
If a Python library is used for text extraction and PDF conversion, the best option is to use PyMuPDF. PyMuPDF returns detailed information about the text, including the font name, font size, and whether it is bolded/italicized, without compromising speed. As there are many instances of tables throughout the Senate papers, we need to include this ability in our consideration. Although PyMuPDF is considered to be weaker in table extraction than pdfplumber, it includes a `find_tables()` function which handles text wrapping inside explicit grid lines well, which is our primary use case. If tables are being flattened badly, it is possible to later integrate pdfplumber, but using PyMuPDF alone is the best starting place.

### Building an XML Tree (lxml)
While PyMuPDF provides the ability to recognize precise structure of the document, it cannot natively create an XML document with a custom schema from this information. From the font and positional data provided by PyMuPDF, we need to create rules to identify certain elements of the paper. For example, the combination of a larger font + bold + in top right corner of page = paper code. Or small text + bottom of page = footer. From the identified element, we can add in the desired XML tag with the extracted text from that section.

As XMLs follow a nested tree structure, we have to keep track of where the opening and closing tags. One method of keeping track of where the tags should start and end is by using a stack. However, a cleaner method would be to use lxml. 


### **Conversion Pipeline

</br>

## **Workflow

</br>

## **Alternative solution (non-XML)
If using XML became unrealistic (perhaps due to timeline constraints), an alternative solution would be to eliminate XML from the workflow and produce a "Referenced Papers" section in the paper's page on the website. 

</br>

## Possible Usage of an AI Agent
At present, the outlined workflows only identifies obvious references between Senate papers. A possible expansion to this application is identifying ambiguous references, references with inconsistent phrasing, and hyperlinking to a wider domain of sites (perhaps to other sites within the University of Edinburgh ecosystem). This could be possible through an AI agent, which can be implemented either using an API (proprietary) or a local model (open-source). The agent could also be added in to a specific part of the workflow, such as partitioning/sectioning text from the PDF documents when being converted to XML.

A possible concern with using an AI agent is higher cost and that the agent should not add hyperlinks blindly, which again brings up the issue of an admin staff.

</br>

## AI Acknowledgement
ELM, the University of Edinburgh's official AI innovation platform, was used throughout the research process to understand possible ways of automating hyperlinking, provide suggestions for the workflow, and gain further understanding of how each step would be implemented on the backend. ELM was set to be GPT 5.4 for the model, and web search was enabled. AI was used as a suggestion rather than a final decision point for the workflows, with deviations particularly made in the XML version of the workflow. All descriptions were written by hand.

I would also like to acknowledge my advisor for writing the example XML schema and explanation of the structure of file names.
