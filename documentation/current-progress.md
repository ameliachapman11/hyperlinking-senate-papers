# Current Progress
## Outlining Problem
I researched and evaluated the current storage methods of the University of Edinburgh's Senate papers, which you can read more about in the [Overview and Motivation file](../internship/overview-and-motivation.md). To summarize, the primary issue is lack of centralization. For example, if a Senate member is reading through an Education Committee paper and find a reference to a decision in a prior Senate meeting, they then have to go to the Senate website, scroll down through many years of papers to find the relevant one, and then scroll through a document that may be over 100 pages long. It would be much easier if, one, users could perform keyword search and, two, if references between papers were automatically hyperlinked&mdash;these are our two primary goals in developing a web application.

<br/>

## Web App Development
### Build Approach
I researched and evaluated possible build approaches for the web app, focusing on paper storage, keyword search, and automating hyperlinking. The recommended approach, and the one taken in development of the prototype, is to use a content management system. Using a content management system provides scalability/ability to handle large amounts of Senate Documents and has the added benefit of speeding up development due to the wide amount of community-developed modules freely available. The CMS currently being used for development is WordPress. I also evaluated possible search engines for keyword search, spending time to understand the NLP aspects of full-text search and the process of preparing files for the search index. For more information about build approach evaluations, please read the [Build Approach](../internship/build-approach.md) file. 

### Prototype Website
The prototype website is being developed on a LocalWP dev environment. The custom taxonomy and custom post type have been configured to correctly take in the metadata and files for a paper. At the moment, the XML file must be uploaded seperately to the PDF document. In the future, we are hoping to make it so that the PDF can be uploaded and then automatically converted to XML/hyperlinked. 

Currently, the homepage has the ability to display all papers. Users can filter by document type, committee, and academic year. They can also sort papers by date (either newest first or oldest first). Below is a current screenshot of the protoyped homepage:

![Screenshot of the homepage of the prototype](./assets/homepage.png)

## Hyperlinking Pipeline
I researched what the process to automate hyperlinking would look like and designed a pipeline. The following is a summary of the pipeline:
1. Create new **Paper** document in admin side of website, fill in metadata and upload the PDF version of the document
2. Trigger conversion to XML, converting PDF to a custom XML schema using a Python script and then saving it in the **Paper**
4. Once all papers are uploaded, trigger generating hyperlinks by identifying possible matches and querying the CMS to see if there is a matching document. Generate a hyperlink to a specific paper tag if a matching target document is found.
5. Save the new version of the XML document in place of the previous one

For a more detailed explanation of the pipeline, please read the [Hyperlinking](../hyperlinking.md) document.

Currently, we have designed a custom XML schema specific to Senate papers, which you can learn more about in the [XML Schema](xml-schema.md) document. We have also created a preliminary Python script to convert from PDF to XML, and an XSLT sheet for rendering the XML as HTML. The script generally works well on Minutes documents but struggles on longer Agenda & Papers documents where there is more irregular formatting, complicated table structure, variety of image type, etc. For more information about ongoing rendering problems encountered with the script, please reference the [Problematic Files](problematic-files.md) document. We have not yet developed the custom WordPress plugin needed to automate conversion. 
