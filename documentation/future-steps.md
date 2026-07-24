# Future Steps
## Ongoing Work
Web dev:
* Reevaluate keyword search implementation -> is Solr necessary? Can you query Solr with XML directly, or do you have to use JSON? Would OpenSearch or Elasticsearch be better for querying XML? Can I just use a plugin from WordPress?
* Add keyword search to website homepage
* Create template which applies across all Paper pages -> figure out how to 

Script:
* Where to start paper tags? Should it have to follow the paper code? Sometimes it will just list A or B instead of the full code...
* Adding `<possibleLink>` tag to anywhere where a paper code occurs (excepting in `<paper>` tags for the time being)
* Command line interaction: is it possible so you can have just a filepath and not also a filename for the second argument (will default to the same as the input file but .xml)? In otherwords it is possible to give the option to specify the outputs folder without the filename?

Writing documentation:
* **documentation folder:** current-progress, future-steps, problematic-files, wordpress-guide, xml-schema
* **internship folder:** reflection

<br/>

## Future Problems to be Tackled
Script/problems with rendering:
* When a link is continued across multiple lines (currently sometimes renders as 2 blocks), instead make it so that if the preceding block is a link and the current link is the same as that link to combine them into one block
* Consider whether minutes documents should be extracted seperately so it can have a `<subItem>` instead of just consisting of an agenda
* Is it possible to identify footnotes and to inject them as a hyperlink into the place they were originally referencing? They currently just look like random out of place text

Hyperlinking: 
* Figure out structure for generating hyperlinks to another XML doc... or would it have to be to HTML as that's how we're rendering it?
* Figure out how to make links that will work on the WordPress site and bring you to the correct section
* Create plugin that automates converting to XML and adding these hyperlinks when the PDF is uploaded into WordPress site... it is okay for now if it does not actually query the other XML doc (as it would require ALL docs being uploaded before this can take place). In other words make it so the script runs and saves it to the correct part of the metadata for the paper. May need to return XML instead of saving it.
* Figure out how to make it so `style.xslt` can be applied across all Paper pages when rendering -> need to develop another plugin
* See if it is possible to go to the most relevant paper section rather than just the top of the doc when doing keyword search
