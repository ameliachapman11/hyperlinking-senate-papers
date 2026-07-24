# Future Steps
## Ongoing Work
### Web dev:
We are currently working on adding keyword search to the website's homepage, and am looking into various possible available plugins that can be used. A caveat is that we would like the search to query from the paper's XML rather than the content of a blog post as is typical in WordPress search. One possible option is the [ACF: Better Search](https://wordpress.org/plugins/acf-better-search/) plugin as the XML document is configured as a custom field. [Relevanssi](https://en-gb.wordpress.org/plugins/relevanssi/) may also be helpful as it includes many essential aspects of full-text search such as fuzzy matching. Since switching to WordPress, we are moving away from the idea of using search engines such as Apache Solr and Opensearch, which require a large amount of extra work to integrate with Wordpress.

We are currently creating a template which applies across all **Paper** pages, meaning that when a user clicks on the link to any **Paper**, it should bring them to a page with the same general layout: title, display of some metadata fields, link to the original PDF, and the XML rendered as HTML. This requires downloading additional plugins as features such as creating a template and displaying a metadata field within a page are only available in the Pro version of Elementor (paid). 

### Script:
Although the script for PDF to XML conversion is generally completed, there are a few questions that are currently being addressed:
1. When identifying where to begin a paper tag, should it only be dependent on font size (as it currently is)? Or should it adhere to the structure of a paper code? The issue with only identifying by paper code is that in some SEC documents, it just lists A or B instead of the full code.
2. Add in `<possibleLink>` tag to anywhere where a paper code occurs (excepting in `<paper>` tags for the time being)
3. Altering command line interaction: is it possible so you can have just a filepath and not also a filename for the second argument (will default to the same name as the input file but .xml)? In other words, it is possible to give the option to specify the outputs folder without the filename?
4. Should minutes documents be extracted differently than Agenda & Papers documents? Currently minutes documents consist of just an **Agenda** with body text, tables, and images within it rather than having sub-items.

For additional rendering issues that are being addressed/investigated, see the [Problematic Files](problematic-files.md) document.

<br/>

## Future Problems to be Tackled
The future steps of this project are primarily to do with completing the development of web app and integrating the pipeline into the ongoing WordPress prototype. 

Plugins to be developed:
* Upon upload of PDF, automate running script for XML conversion
* Plugin which can be triggered via a menu in the admin interface which generates and injects hyperlinks across all **Paper** documents within the CMS

Specific questions to be answered:
* How can you create a hyperlink to a specific part of another XML document? Or would it have to be to a specific section of HTML as that's how it will be rendered on the webpage?
* How can we ensure the link will go to the correct Wordpress webpage? Is there a general formula for the `slug` of our **Paper** pages that we can utilize?
* When performing keyword search, is it possible to go to the most relevant paper section rather than just the top of the document? In other words, can we change the displayed link for the papers or does it just have to go to the general webpage?
