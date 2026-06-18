# Automating Hyperlinking
**Goal:** One of the primary goals of this project is to research how adding hyperlinks between Senate papers may be automated. For the time being, we will focus on obvious references between papers. One example is in the E-Senate *Agenda and Papers* file from the September 23-27, 2023 session of the E-Senate: section e-S 23/24 1B mentions that the "Senate Quality Assurance Committee (SQAC) considered the paper at its meeting on 12 September 2023." This would be an appropriate place where a hyperlink would be automatically added. 

There is currently a lack of existing technologies that can automatically detect references between a set of papers and generate hyperlinks between them, so a custom workflow/logic has to be implemented. 

</br>

## Workflow of Automating Hyperlinking
**Note:** In the following workflow, it is assumed that the recommended build approach of using a CMS such as Drupal and a search engine such as Apache Solr is taken, as detailed in the [Build Approach](buildApproach.md) file.  

### 1. Add Papers to the CMS
Upload each PDF paper into the CMS and manually enter metadata such as committee, academic year, meeting date, source URL, etc.

### 2. Trigger Processing Pipeline
Once the PDF is uploaded, the CMS will trigger a backend processing job. This can either be done automatically or added to a queue which is then processed in the background. Taking Drupal as an example, a custom Drupal module will need to be developed using PHP and YAML files which tells the CMS that once the file is uploaded to then extract text, split it into page-level text units, etc. (the rest of the workflow). JSON files may also be used as part of the module for exchanging structured data with the Solr/Tika APIs, such as creating documents for the search index. 

### 3. Extract Text via Text Extraction Software
Extract text with extraction software such as Apache Tika or PDFBox. The text should be extracted page by page to allow for later finding the most relevant page for a hyperlink. To then reconstruct the full document text (which will be used for a regular keyword search enquiry by a user), the extracted text for all pages can be joined together. The extracted text is stored in the backend/memory temporarily before records for the search engine are created.

### 4. Prepare Documents for Search Engine
Search engines such as Apache Solr store documents in a core or a collection, which acts like a database. Documents consist of multiple fields, which can include the text of the document itself along with various metadata fields. We have to prepare records to be sent to the search engine before it can be stored and indexed. As for reasons previously stated, we are looking to have documents both on the whole-paper level and on the page level, so we have to prepare documents for each. 

The documents on the whole-paper level should contain the full extracted and concatenated text along with metadata fields inherited from the parent PDF document stored in the CMS. This may include document ID, title, committee, academic year, meeting date, and source URL/file path. 

The documents on the per-page level should contain the extracted page text, inherited parent metadata (see above), along with additional metadata fields for identifying which page the document corresponds to. This may include page record ID, page number, and parent document ID (to know which paper the page is part of).

It would also be helpful to add a field to denote record type so that when you are querying Solr you can specify whether you want to search page-level or document-level. This may be done through something like `record_type = document` or `record_type = page`.

### 5. Send Searchable Documents to the Search Engine
When you send documents to a search engine, they are automatically added to the core/collection and indexed. A document being indexed means that it is broken down into searchable terms and organizing it into a data structure much like an index in a back of a textbook, where you can search up a word and it tells you relevant pages. You can verify that records have been correctly added and with the correct metadata by opening the Solr Admin UI and running a query for known metadata.

### 6. Detect References to Other Papers
This step takes place in backend logic, again likely through a custom Drupal module. It tries to find phrases with combinations of committee name, month/year, paper code, etc.&mdash;anything that can be used to match the metadata of another paper&mdash;and then could create candidate reference objects to be matched in the next step. 

**Note:** This step is interchangable with steps 4-5. Since detecting references to other papers is using the same extracted text that is used to make the documents for the search engine, either can be done first. 

### 7. Match the Reference to a Target Paper
After detecting a candidate reference, the backend (in the same Drupal module) matches it to a known paper using extracted clues such as committee or meeting date. This matching can use either the metadata in the CMS or the metadata indexed in the search engine. While CMS metadata benefits from being the authoritative source and does not rely on the search engine being up to date, using the search engine metadata fits more naturally with the rest of the search pipeline.

### 8. Find Most Relevant Target Page and Generate Hyperlink
Hyperlinks do not have to be just to the beginning of documents, but can link to specific pages. This step queries the search engine to find which page of the referenced paper should be used for the hyperlink. The backend should take the local context around the reference (such as the current section heading, current sentence, or nearby sentences) and then query the search engine which will return the best-matching page. The search engine should automatically handle normalization (making text all lowercase, removing stop words, etc.) as part of its indexing/query process.

A practical example of this concept is say that there is a phrase in a Senate paper that says "...the October 2024 meeting of the APRC..." and elsewhere in the sentence it mentions "the School of Literatures, Languages, & Cultures." In the paper for the October 2024 meeting of the APRC, the search engine will find the page most relevant to literature, languages, and cultures and return it. This is the proposed page to be hyperlinked.

This step should also generate a hyperlink at the page level, which includes a link to certain page of the referenced paper and an appropriate link title based on the original identified phrase for the candidate reference.

### 9. Apply a Confidence Rule To Accept/Reject Suggested Hyperlink
Although the previous step suggested a specific page to be hyperlinked to for the reference, this should not be accepted blindly. Instead, the backend should implement a confidence rule. It would be along the following lines:
* If one page is clearly the best match, create a page-level link
* If the match is weak, only link to the start of the document
* If no reliable match exists, do not create a hyperlink

**How to determine if something is a good match?** Example heuristics could use the relevance score of the top result, the gap between scores of the top and second result, whether an exact phrase or heading terms matched, etc.

**Why use a confidence rule?** Another option would be to have the program just suggest links and have a human verify each one manually. However, this would require having admin accounts (perhaps using university emails and and SSO) and developing a separate admin interface to go along with it. There also the additional concerns that may not be an appropriate staff member at the university to perform this job and that the application needs to have enhanced security for storing confidential login details. By using a confidence rule, we are treating creating hyperlinks as an pre-publication data processing step. *Note: the downside of a confidence rule is that when new papers are added later, we need to rerun the pipeline & redeploy.*

### 10. Add Generated Hyperlinks to Metadata
All accepted hyperlinks for a paper should be added to the CMS as metadata. There should be a metadata field for a list of hyperlink records which will contained the hyperlinks for all referenced papers for a specific paper. It would also be helpful for a hyperlink record to contain other data such as target document ID (which paper is being referenced), target page number, confidence score, link type (page-level or document-level). The hyperlink itself can be implemented as a Drupal Link field, HTML anchor tag, etc.

### 11. Add to Frontend
On the frontend, when a user clicks on a link for a specific paper, it will bring up a page showing metadata, a link to the original PDF or a way to view it, and a section for related/referenced papers. All hyperlinks generated throughout the previous steps will be included in the referenced papers section. Choosing to have a referenced papers section as opposed to adding the hyperlink back into the text is a safer approach than rewriting the PDF and also no longer needs a seperate XML and HTML document for each paper.

*Note: In the XML section, we will explore an alternative solution where hyperlinks are embedded back into the text.*

</br>

## Possible Usage of XML files

### Conversion of PDF to XML
Senate papers are currently stored as PDFs. In order for the web application to make use of XML files in the automatic hyperlink generation process, they need to be be converted. This can be done manually using proprietary software like Adobe Acrobat Pro, open-source software like Apache Tika, or Python libraries like pdfplumber and pdfminer. A concern with automatic conversion to XML is that it may lead to messy papers/tags; if the document is not well-structured then it may not be helpful in further steps. 

As the papers are text-based rather than scanned, software that focuses on Optical Character Recognition (OCR) do not have added beneficiality. 

### **XPath
### **XML-focused CMSs
### **Amended Workflow
If XML were to be used, the workflow would stay the same in general principles, with a few caveats. The main change would be from using a text extraction software such as Apache Tika to 

### **Recommendation on Using XML

</br>

## **Possible Usage of an AI Agent

</br>

## **AI Acknowledgement
