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
A Content Management System (CMS) is software which facilitates the creation, editing, organization, and publication of digital content. Digital content can entail anything from blog posts to PDF's to images to videos. The biggest benefit of using a CMS is that they require little to no code to develop, so anyone can create a website&mdash;no costly developer necessary. They are frequently used for the development of small travel/food blogs, portfolio websites, and e-commerce websites, but large organizations and governments also rely on them (such as Tesla, Microsoft, and the official White House website). Some of the most popular CMS’s include WordPress, Wix, Squarespace, Drupal, Joomla, and Strapi. CMS's power over two thirds of the internet's websites globally, with WordPress alone accounting for over 40%. 

An additional feature of CMS's is that they provide capabilities for users with different permission levels across an organization to manage certain sections of content or data. This means admin staff and executives may have different privileges when it comes to managing the company's website. There are also real-time editing and preview capabilities, meaning when users make changes, they can preview content exactly as it will appear once published. Finally, CMS’s make it so metadata tags can easily be added to content, allowing for efficient search and filtering.

### General Structure
If we were to pursue using a CMS to build the prototype, we would need to use it in combination with a text extraction software and a backend search engine. This project's primary focus is on search within Senate documents, and a CMS alone does not have the capabilities to perform text extraction from the PDF documents and full-text search. Full-text search has linguistic awareness and is more computationally efficient than doing literal phrase matching, which scans word-by-word.  

The following are aspects of advanced search that the application should be capable of:
* Relevance ranking: puts most likely useful search result at the top
* Stemming: matches to related forms of the word (if the keyword entered is "run," will match words like "ran" or "running")
* Fuzzy matches: finds matches even when the search query does not perfectly match the target data, typically used to account for spelling mistakes
* Synonyms: finds thematically similar words (if the keyword entered is "parent," will match words like "mother" or "family")
* Highlighted snippets: shows the matching snippet of the text with the keyword(s) highlighted

### **WordPress
WordPress is the world's leading CMS and is most often used for small websites such as travel or recipe blogs. While WordPress could support a basic repository of Senate papers, including PDF storage, manual metadata, and some filtering through plugins, it lacks the ability to easily integrate an strong search experience. Creating advance search would depend on multiple plugins or external tools, making the system more difficult to configure and maintain. WordPress is more suitable for applications which only require simple content publishing. 

### **Drupal
Drupal is an open-source CMS which uses drag and drop style page building tools, and is generally viewed as more flexible (and thus more complex) than others CMS's. This additional functionality makes Drupal more suited for the needs of this project when compared to something like WordPress, which is primarily used for creating blogs or basic portfolio websites. Adding specialized functionality to a Drupal web application can typically be achieved using a module. A module is a bundle of code (PHP, JavaScript, and CSS files) which can be easily added to a Drupal project by installing the module via the Drupal admin dashboard of the website. The open-source nature of Drupal means there are a vast host of freely available modules (the Drupal website reports over 40,000). Some existing modules that may be relevant to the develoment of this prototype include [Apache Solr Search](https://www.drupal.org/project/apachesolr) for the search backend and [Media Thumbnails PDF](https://www.drupal.org/project/media_thumbnails_pdf) for the UI. 

Pros and Cons:
* Pros: more versatile than other CMS's, existing module to combine with Solr
* Cons: bigger learning curve than other CMS's (which may mean not all features can be achieved in the timeline), may be overkill for required features

### **Joomla
Joomla is another open-source CMS which, like Drupal, is written in PHP and uses MySQL as a database. Large-scale companies such as Ikea, Linux, and Holiday Inn use Joomla to power their sites. 

### **SharePoint

<br/>

### **Search Engines and Text Extraction:

### **Recommendation for CMS's:

## Digital Asset Management System

### **What Is a Digital Asset Management System?
### **ResourceSpace

<br/>

## **Overall Recommendation
