# Build Approach Recommendations

## Build From Scratch

### **General Structure
### **Links
### **Frameworks
### **Recommendation on Building from Scratch

<br/>

## Content Management Systems

### What Is a Content Management System?
A Content Management System (CMS) is software which facilitates the creation, editing, organization, and publication of digital content. Digital content can entail anything from blog posts to PDF's to images to videos. The biggest benefit of using a CMS is that they require little to no code to develop, so anyone can create a website&mdash;no costly developer necessary. They are frequently used for the development of small travel/food blogs, portfolio websites, and e-commerce websites, but large organizations and governments also rely on them (such as Tesla, Microsoft, and the official White House website). Some of the most popular CMS’s include WordPress, Wix, Squarespace, Drupal, Joomla, and Shopify. CMS's power over two thirds of the internet's websites globally, with WordPress alone accounting for over 40%. 

An additional feature of CMS's is that they provide capabilities for users with different permission levels across an organization to manage certain sections of content or data. This means admin staff and executives may have different privileges when it comes to managing the company's website. There are also real-time editing and preview capabilities, meaning when users make changes, they can preview content exactly as it will appear once published. Finally, CMS’s make it so metadata tags can easily be added to content, allowing for efficient search and filtering.

### General Structure
If we were to pursue using a CMS to build the prototype, we would need to use it in combination with a text extraction software and a backend search engine. This project's primary focus is on search within Senate documents, and a CMS alone does not have the capabilities to perform text extraction from the PDF documents and full-text search. Full-text search has linguistic awareness can handle aspects of advanced search such as relevance ranking, stemming, fuzzy matches, and synonyms. The flow of data would be as follows: CMS stores the PDFs and metadata &rarr; text extraction software extracts text from the PDFs &rarr; CMS sends that extracted text to the search index.

### Text Extraction and Search Engines
**Text Extraction:** Before a search engine can perform full-text advanced search, the text must be extracted so it can be indexed for search. Apache Tika can be used to achieve this. Tika is an open-source content analysis toolkit written in Java which can extract metadata and structured text from over 1,000 different file formats (including PDF’s). 

**Search Engines:** After the text is extracted with Tika, a search engine can perform a full-text search based on the user-inputted keywords. Some popular open-source search engines include Apache Solr, Elasticsearch, and OpenSearch. Elasticsearch and OpenSearch, though open source, are owned by companies, which means that the company could choose to make it proprietary software at any point. Elasticsearch is owned by Elastic while OpenSearch is owned by Amazon. By choosing Solr, which is owned by a nonprofit, we are future-proofing the application, and also provide easier integration with Tika as they are developed by the same company.  

### WordPress
WordPress is the world's leading CMS and is most often used for small websites such as travel or recipe blogs. It is open-source. While WordPress could support a basic repository of Senate papers, including PDF storage, manual metadata, and some filtering through plugins, it lacks the ability to easily integrate an strong search experience. Creating advance search would depend on multiple plugins or external tools, making the system more difficult to configure and maintain. WordPress is more suitable for applications which only require simple content publishing. 

### Drupal
Drupal is an open-source CMS which uses drag and drop style page building tools, and is generally viewed as more flexible than others CMS's. Adding specialized functionality to a Drupal web application can typically be achieved using a module, a bundle of code (PHP, JavaScript, and CSS files) which can be added to a Drupal project via the admin dashboard of the website. There are over 40,000 freely available modules, supported and developed by the open-source community. Some existing modules that may be relevant to the develoment of this prototype include [Apache Solr Search](https://www.drupal.org/project/apachesolr) for the search backend and [Media Thumbnails PDF](https://www.drupal.org/project/media_thumbnails_pdf) for the UI. 

While added flexibility is Drupal's biggest draw, it also results in a bigger learning curve than other CMS's&mdash;this runs the risk of having to abandon some of the desired features due to a limited timeline.

### Joomla
Joomla is another open-source CMS which, like Drupal, is written in PHP and uses MySQL as a database. Large-scale companies such as Ikea, Linux, and Holiday Inn use Joomla to power their sites. It is highly customizable, with almost ten thousand plug-ins developed by the community available for download. 

Compared to Drupal, Joomla falls short in terms of search. Drupal has a more mature and widely used integration path for Solr than Joomla. While Joomla can still work with external search tools such as Solr and Tika, this is more likely to require custom development for integration, which increases project risk. Joomla offers native plugins with tools such as [OS PDF indexer](https://extensions.joomla.org/extension/os-pdf-indexer/) with Joomla Smart Search, but lacks some of the required advanced search capabilities that Solr offers. A possible benefit of Joomla over Drupal is that it is regarded to be easier to use and has a smaller learning curve, which may make it more viable for the timeline of this project. 

### SharePoint
SharePoint is a proprietary CMS developed by Microsoft, and is intended for enterprise-level usage. Although SharePoint is proprietary, it is already used by the University of Edinburgh which gives it a distinct advantage from an integration standpoint. If SharePoint were to be used for the project, it would be structured as follows: SharePoint document library to store the PDF files with added metadata, Microsoft Search to perform full-text search on the PDF’s (as opposed to Solr), and a SharePoint site for user interaction with the documents. For building the site’s UI, we would additionally use PnP Modern Search, which is a set of open-source SharePoint web parts designed for custom search pages. 

The main drawback of using SharePoint when compared to other CMS’s lack of flexibility in terms of search engine choice. SharePoint site owners are essentially forced to use Microsoft Search; SharePoint does not natively integrate with other search engines such as Solr. Additionally, Microsoft Search is weaker than Solr when comparing capabilities like fuzzy matching, phrase matching, and page/chunk level indexing (displays something like “match on p. 64”). While it is easier out of the box, Microsoft Search does not allow for deeply tuning search. 

A benefit of using SharePoint beyond integration is hosting. Microsoft hosts SharePoint sites directly, while with other CMS’s, you have to host on an external provider. External providers are either free, which may have ads or be unreliable in terms of network speed, or are proprietary. 

### Recommendation on Using a CMS
If we choose to use a CMS for this project, the best option is either Drupal or SharePoint, depending on what stakeholders feel it is more important to prioritize. Drupal can easily be integrated with Apache Solr, providing advanced search capabilities which will help Senate members easily identify sections of past papers relevant to their research. It also provides the edge over Microsoft Search in areas such as fuzzy matching and stemming behavior. However, SharePoint is better if it is more important to prioritize integration with existing University of Edinburgh websites. University of Edinburgh websites are primarily built in either SharePoint or on EdWeb2, the official University of Edinburgh CMS. Another consideration is timeline—SharePoint has a more user-friendly entry point, while Drupal has a steeper learning curve for developers. If Drupal is chosen, some features may have to be dropped to accommodate the timeline. 

<br/>

## Digital Asset Management System

### What Is a Digital Asset Management System?
A Digital Asset Managment (DAM) system is a type of software which is used for organizing, storing, and distributing digital files such as images, videos, and audio files. A benefit of DAM’s is centralizing media libraries, allowing for a streamlined workflow. It also manages versions and approvals, allowing teams to clearly keep track of what is a draft and what is a final product. Files stored in a DAM have attached metadata, creating a structured taxonomy design within an organization. Some examples of popular open-source DAM's include ResourceSpace and Pimcore.

**DAM vs CMS:** Although DAM’s and CMS’s are both used for digital content management, CMS’s are more focused towards publishing and presenting content to user through a website while DAM’s are focused on organizing and storing content for internal structure. DAM's are often combined with CMS's rather than being used independently. The DAM is responsible for organizing and securely storing versions and media assets, while the CMS uses those assets to build and publish web pages.

### Recommendation on Using a DAM
It is not advised to use a DAM for this project. Using a DAM would require sacrificing the desired user interface. The frontend interfaces of DAM’s are typically designed around asset management workflows rather than creating a database-style search experience as planned in the mockup. Additionally, it is difficult to add a customized frontend which would require additional work in the future should our prototype eventually be integrated into the university ecosystem. 

Another issue with using a DAM is that they are designed for rich media and high volumes of content. DAM’s handle enterprise level tasks, organizing frequently-changing assets from a variety of teams across an organization. With less than 500 files to manage for our project, using a DAM would be overkill. A CMS alone has the capabilities of handling our requirements, so using a DAM on top of this is unnecessary. 

<br/>

## Overall Recommendation
A CMS is advised to be used to build the web application. Although building from scratch offers maximum control over user interface, user experience, and search, all of the desired features for this project can be achieved using a content management system, which will significantly speed things up on the development side and has a lower learning curve. The drag-and-drop approach for the frontend of a CMS website means that we do not have to spend time fiddling with frontend and CSS frameworks to achieve essentially the same result&mdash;this time can instead be spent enhancing search on the backend.

_Summary of Recommendations for CMS's:_
* If search capabilities are most important: Drupal + Apache Tika + Apache Solr
* If integration with existing systems and timeline are most important: SharePoint + Microsoft Search

<br/>

## **AI Acknowledgement
ELM, the University of Edinburgh's official AI innovation platform, was used throughout the research process to gain suggestions for which frameworks and content management systems would be most relevant to this project. ELM was set to be GPT 5.4 for the model, and web search was enabled. ELM was also used to compare between various search engines and content management systems, and to understand their capabilities, such as the integration of Apache Solr with Joomla vs with Drupal. AI was used as a suggestion rather than a final decision point for the provided recommendation.
