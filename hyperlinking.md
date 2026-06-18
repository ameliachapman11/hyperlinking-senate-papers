# Automating Hyperlinking
**Goal:** One of the primary goals of this project is to research how adding hyperlinks between Senate papers may be automated. For the time being, we will focus on obvious references between papers. One example is in the E-Senate *Agenda and Papers* file from the September 23-27, 2023 session of the E-Senate: section e-S 23/24 1B mentions that the "Senate Quality Assurance Committee (SQAC) considered the paper at its meeting on 12 September 2023." This would be an appropriate place where a hyperlink would be automatically added. 

There is currently a lack of existing technologies that can automatically detect references between a set of papers and generate hyperlinks between them, so a custom workflow/logic has to be implemented. 

</br>

## Workflow of Automating Hyperlinking
**Note:** In the following workflow, it is assumed that the recommended build approach of using a CMS such as Drupal and a search engine such as Apache Solr is taken, as detailed in the [Build Approach](buildApproach.md) file.  

### 1. Add Papers to the CMS
Upload each PDF paper into the CMS and manually enter metadata such as committee, academic year, meeting date, source URL, etc.

### 2. Trigger Processing Pipeline
Once the PDF is uploaded, the CMS will trigger a backend processing job. This can either be done automatically or added to a queue which is then processed in the background. Taking Drupal as an example, a custom Drupal module will need to be developed using PHP and YAML files which tells the CMS that once the file is uploaded to then extract text, split it into page-level text units, etc. (the rest of the workflow). JSON files may also be used as part of the module for exchanging structured data with the Solr/Tika APIs, such as creating records for the search index. 

### 3. Extract Text via Text Extraction Software
### 4. Prepare Searchable Records for Search Engine
### 5. Send Searchable Records to the Search Engine
### 6. Detect References to Other Papers
### 7. Match the Reference to a Target Paper
### 8. Find Most Relevant Target Page and Generate Hyperlink
### 9. Apply a Confidence Rule To Accept/Reject Suggested Hyperlink
### 10. Store the Generated Hyperlink Data
### 11. Add to Frontend

</br>

## Possible Usage of an AI Agent

</br>

## AI Acknowledgement
