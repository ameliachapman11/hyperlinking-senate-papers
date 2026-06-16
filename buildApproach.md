# Build Approach Recommendations

## Build From Scratch

### Links
Links is a functional programming language developed by researchers at the University of Edinburgh which allows for tierless web programming (as opposed to having the frontend and backend separated by different frameworks/languages). Links automatically creates and executes SQL queries, with PostgreSQL being used as the backend. In the past, Links has been used to prototype a COVID-19 data curation application, replicate the GtoPdb pharmacology database, and to recreate popular games such as 2048.

Although using Links for this project would simplify the divide of having to separately develop the front and backend of the application, the lack of existing support for combining Links with search engines makes it an unsuitable choice to develop the prototype. The goal of the application is primarily focused on search behavior so it is important to be able to perform advanced search rather than just doing database queries, which is what Links is designed to do. Additionally, the fact that the Senate papers are currently stored as PDF’s, and fulltext search cannot be easily performed on the PDF through a database query.

### General Structure
If we were to pursue this project from the ground up, decisions would need to be made regarding fullstack development: which frontend framework, backend framework, and database would be most suitable for creating the application? In addition to the frontend framework, which CSS framework would be best for a custom UI that adheres to the University of Edinburgh’s brand identity? 

The general structure would consist of CSS framework + frontend framework + backend framework + database + PDF storage + text extraction + search engine. PDF storage would be done seperately from the database because storing directly in the database can lead to slower backups/restores and worse scalability. 

### Frameworks
**CSS:** CSS frameworks are software libraries that allow for easier, more standards-compliant web design than using CSS directly and are focused on the styling/aesthetics of a website. Examples of popular CSS frameworks include Bootstrap, Tailwind, and Bulma. For this project, Tailwind would be most suitable as it provides the opportunity to follow the branding identity of the university. Bootstrap and Bulma have pre-defined looks which can make a website instantly be recognizable as a Bootstrap site or Bulma site; we instead want to create an experience with the prototype where users can feel that they are using a *real* University of Edinburgh website. This will also streamline integration later down the line.

**Frontend:** A frontend framework is a collection of pre-written code, components, and tools that help developers create the frontend (buttons, navigation, UX) of a web app more efficiently. Frontend frameworks also make it possible to dynamically update parts of a page without requiring full page reloads, resulting in a smoother experience. Frontend frameworks need to be used in combination with a CSS framework&mdash;frontend frameworks only handle structure and behavior, while a CSS framework is needed for styling. Some popular frontend frameworks include React, Angular, Vue, Svelte, and Next JS. For this project, Vue would be the most suitable as it has a smaller learning curve compared to other frontend frameworks, but still has the capabilities and scalability required for this project. 

**Backend:** A backend framework is a collection of pre-written code, tools, and libraries which helps developers develop the backend (database communication, user authentication, routing) more efficiently. Some popular backend frameworks include Node JS, Django, FastAPI, and Spring Boot. For this project, Django is most suitable. Django is a Python-based framework which benefits from Python’s well-developed document-processing libraries (which is important to this application as it is based on processing PDF’s and then searching them). Although FastAPI is also built on Python, it is more so intended for developing API’s rather than a full web app, so Django remains as a better choice. 

### Database and PDF Storage
**Database:** In this application, the database would be used to store metadata for the Senate papers. Some examples of popular databases are PostgreSQL, MySQL, and MongoDB. As we are handling structured data that is not highly variable, it would be best to use a relational database (which eliminates MongoDB as an option). For this project, MySQL would be the most suitable option because, although simpler than PostgreSQL, it is able to handle the scope of this project where we are just storing the metadata such as committee and year. 

**PDF storage:** As the Senate papers are frequently over 100 pages long, it is not a good idea to store them directly in the database as it degrades database performance. Instead, they would be stored in a seperate object storage such as AWS S3, Azure Blob Storage, or MiniIO. For this project, MiniIO is the most suitable as it is opensource, while the other two options are proprietary (being owned by Amazon and Microsoft, respectively). 

### Recommendation on Building from Scratch
If this project were to be pursued as a grounds-up project, the recommended build structure consists of the following: Tailwind + Vue + Django + MySQL + MiniIO + Apache Tika + Apache Solr. For more information on why Tika and Solr were chosen, see the *Text Extraction and Search Engines* section of *Content Management Systems*. 

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
Drupal is an open-source CMS which uses drag and drop style page building tools, and is generally viewed as more flexible than others CMS's. Adding specialized functionality to a Drupal web application can typically be achieved using a module, a bundle of code (PHP, JavaScript, and CSS files) which can be added to a Drupal project via the admin dashboard of the website. There are over 40,000 freely available modules, supported and developed by the open-source community. Some existing modules that may be relevant to the develoment of this prototype include [Apache Solr Search](https://www.drupal.org/project/apachesolr) for the search backend and [Media Thumbnails PDF](https://www.drupal.org/project/media_thumbnails_pdf) for the UI. While added flexibility is Drupal's biggest draw, it also results in a bigger learning curve than other CMS's&mdash;this runs the risk of having to abandon some of the desired features due to a limited timeline. 

An example of a Drupal-based website that contains a search interface highly similar to the one designed in the mockup is the [Ontario Search Commission](https://www.osc.ca/en). It includes filters for refining search results, sorting capabilities, each PDF paper hyperlinked, and an elegant user interface.  

### Joomla
Joomla is another open-source CMS which, like Drupal, is written in PHP and uses MySQL as a database. Large-scale companies such as Ikea, Linux, and Holiday Inn use Joomla to power their sites. It is highly customizable, with almost ten thousand plug-ins developed by the community available for download. 

Compared to Drupal, Joomla falls short in terms of search. Drupal has a more mature and widely used integration path for Solr than Joomla. While Joomla can still work with external search tools such as Solr and Tika, this is more likely to require custom development for integration, which increases project risk. Joomla offers native plugins with tools such as [OS PDF indexer](https://extensions.joomla.org/extension/os-pdf-indexer/) with Joomla Smart Search, but lacks some of the required advanced search capabilities that Solr offers. A possible benefit of Joomla over Drupal is that it is regarded to be easier to use and has a smaller learning curve, which may make it more viable for the timeline of this project. 

### SharePoint
SharePoint is a proprietary CMS developed by Microsoft, and is intended for enterprise-level usage. Although SharePoint is proprietary, it is already used by the University of Edinburgh which gives it a distinct advantage from an integration standpoint. If SharePoint were to be used for the project, it would be structured as follows: SharePoint document library to store the PDF files with added metadata, Microsoft Search to perform full-text search on the PDF’s (as opposed to Solr), and a SharePoint site for user interaction with the documents. For building the site’s UI, we would additionally use PnP Modern Search, which is a set of open-source SharePoint web parts designed for custom search pages. 

The main drawback of using SharePoint when compared to other CMS’s lack of flexibility in terms of search engine choice. SharePoint site owners are essentially forced to use Microsoft Search; SharePoint does not natively integrate with other search engines such as Solr. Additionally, Microsoft Search is weaker than Solr when comparing capabilities like fuzzy matching, phrase matching, and page/chunk level indexing (displaying something like “match on p. 64”). While it is easier out of the box, Microsoft Search does not allow for deeply tuning search. 

A benefit of using SharePoint beyond integration is hosting. Microsoft hosts SharePoint sites directly, while with other CMS’s, you have to host on an external provider. External providers are either free, but may have ads or be unreliable in terms of network speed, or are proprietary. 

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
A CMS is advised to be used to build the web application. Although building from scratch offers maximum control over user interface, user experience, and search, all of the desired features for this project can be achieved using a content management system, which will significantly speed things up on the development side and has a lower learning curve. The drag-and-drop approach for the frontend of a CMS website means that we do not have to spend time fiddling with frontend and CSS frameworks to achieve essentially the same result&mdash;this time can instead be spent enhancing search on the backend. Using a CMS also ensures responsive web design, while with development from scratch, this is something that needs to be built in. 

_Summary of Recommendations for CMS's:_
* If search capabilities are most important: Drupal + Apache Tika + Apache Solr
* If integration with existing systems and timeline are most important: SharePoint + Microsoft Search

<br/>

## AI Acknowledgement
ELM, the University of Edinburgh's official AI innovation platform, was used throughout the research process to gain suggestions for which frameworks and content management systems would be most relevant to this project. ELM was set to be GPT 5.4 for the model, and web search was enabled. ELM was also used to compare between various search engines and content management systems, and to understand their capabilities, such as the integration of Apache Solr with Joomla vs with Drupal. AI was used as a suggestion rather than a final decision point for the provided recommendation.
