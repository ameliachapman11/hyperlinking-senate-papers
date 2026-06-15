# Build Approach Recommendations

## Build From Scratch

### **General Structure

### **Links
### **CSS Frameworks
### **Frontend Frameworks
### **Backend Frameworks

<br/>

## Content Management Systems

### What Is a Content Management System?
A Content Management System (CMS) is software which facilitates the creation, editing, organization, and publication of digital content. Digital content can entail anything from blog posts to PDF's to images to videos. The biggest benefit of using a CMS is that they require little to no code to develop, so anyone can create a website&mdash;no costly developer necessary. They are frequently used for the development of small travel/food blogs, portfolio websites, and e-commerce websites, but large organizations and governments also rely on them (such as Tesla, Microsoft, and the official White House website). Some of the most popular CMS’s include WordPress, Wix, Squarespace, Drupal, Joomla, and Shopify. CMS's power over two thirds of the internet's websites globally, with WordPress alone accounting for over 40%. 

An additional feature of CMS's is that they provide capabilities for users with different permission levels across an organization to manage certain sections of content or data. This means admin staff and executives may have different privileges when it comes to managing the company's website. There are also real-time editing and preview capabilities, meaning when users make changes, they can preview content exactly as it will appear once published. Finally, CMS’s make it so metadata tags can easily be added to content, allowing for efficient search and filtering.

### General Structure
If we were to pursue using a CMS to build the prototype, we would need to use it in combination with a text extraction software and a backend search engine. This project's primary focus is on search within Senate documents, and a CMS alone does not have the capabilities to perform text extraction from the PDF documents and full-text search. Full-text search has linguistic awareness and is more computationally efficient than doing literal phrase matching, which scans word-by-word. The project should be capable of handling aspects of advanced search such as relevance ranking, stemming, fuzzy matches, and synonyms.

### **Search Engines and Text Extraction
**Text Extraction:** Before a search engine can perform a full-text advanced search, the text must AHHH 

### WordPress
WordPress is the world's leading CMS and is most often used for small websites such as travel or recipe blogs. While WordPress could support a basic repository of Senate papers, including PDF storage, manual metadata, and some filtering through plugins, it lacks the ability to easily integrate an strong search experience. Creating advance search would depend on multiple plugins or external tools, making the system more difficult to configure and maintain. WordPress is more suitable for applications which only require simple content publishing. 

### Drupal
Drupal is an open-source CMS which uses drag and drop style page building tools, and is generally viewed as more flexible than others CMS's. Adding specialized functionality to a Drupal web application can typically be achieved using a module, a bundle of code (PHP, JavaScript, and CSS files) which can be added to a Drupal project via the admin dashboard of the website. There are over 40,000 freely available modules, supported and developed by the open-source community. Some existing modules that may be relevant to the develoment of this prototype include [Apache Solr Search](https://www.drupal.org/project/apachesolr) for the search backend and [Media Thumbnails PDF](https://www.drupal.org/project/media_thumbnails_pdf) for the UI. 

While added flexibility is Drupal's biggest draw, it also results in a bigger learning curve than other CMS's&rarr;this runs the risk of having to abandon some of the desired features due to a limited timeline.

### Joomla
Joomla is another open-source CMS which, like Drupal, is written in PHP and uses MySQL as a database. Large-scale companies such as Ikea, Linux, and Holiday Inn use Joomla to power their sites. It is highly customizable, with almost ten thousand plug-ins developed by the community available for download. 

Compared to Drupal, Joomla falls short in terms of search. Drupal has a more mature and widely used integration path for Solr than Joomla. While Joomla can still work with external search tools such as Solr and Tika, this is more likely to require custom development for integration, which increases project risk. Joomla offers native plugins with tools such as [OS PDF indexer](https://extensions.joomla.org/extension/os-pdf-indexer/) with Joomla Smart Search, but lacks some of the required advanced search capabilities that Solr offers. A possible benefit of Joomla over Drupal is that it is regarded to be easier to use and has a smaller learning curve, which may make it more viable for the timeline of this project. 

### **SharePoint

### **Recommendation for CMS's:

<br/>

## Digital Asset Management System

### What Is a Digital Asset Management System?
A Digital Asset Managment (DAM) system is a type of software which is used for organizing, storing, and distributing digital files such as images, videos, and audio files. A benefit of DAM’s is centralizing media libraries, allowing for a streamlined workflow. It also manages versions and approvals, allowing teams to clearly keep track of what is a draft and what is a final product. Files stored in a DAM have attached metadata, creating a structured taxonomy design within an organization. Some examples of popular open-source DAM's include ResourceSpace and Pimcore.

**DAM vs CMS:** Although DAM’s and CMS’s are both used for digital content management, CMS’s are more focused towards publishing and presenting content to user through a website while DAM’s are focused on organizing and storing content for internal structure. DAM's are often combined with CMS's rather than being used independently. The DAM is responsible for organizing and securely storing versions and media assets, while the CMS uses those assets to build and publish web pages.

### Recommendation on using a DAM
It is not advised to use a DAM for this project. Using a DAM would require sacrificing the desired user interface. The frontend interfaces of DAM’s are typically designed around asset management workflows rather than creating a database-style search experience as planned in the mockup. Additionally, it is difficult to add a customized frontend which would require additional work in the future should our prototype eventually be integrated into the university ecosystem. 

Another issue with using a DAM is that they are designed for rich media and high volumes of content. DAM’s handle enterprise level tasks, organizing frequently-changing assets from a variety of teams across an organization. With less than 500 files to manage for our project, using a DAM would be overkill. A CMS alone has the capabilities of handling our requirements, so using a DAM on top of this is unnecessary. 

<br/>

## **Overall Recommendation
