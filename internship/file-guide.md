# Guide to Files Within the Internship Folder
**Overview:** the `internship` folder consists of documentation created throughout my internship in June-July 2026 in the Laboratory for Foundations of Computer Science (LFCS) at the University of Edinburgh's School of Informatics. The documentation was primarily used for communicating my research findings with my supervisor, Vashti Galpin, a senior researcher in the LFCS.

The recommendations made throughout the documents do not necessarily reflect the results of later research or decisions made to time/scheduling constraints. For instance, we were unable to schedule meetings with Senate members and therefore could not respond to feedback given as planned in the *8 Week Plan*. Additionally, in the *Build Approach* file there is a mention of using Apache Tika to extract the text from PDFs but this changed once we focused more on hyperlinking&mdash;we are instead extracting the PDF content using a Python library and storing it in a custom XML schema. A final example is that, although the Build Approach file makes a recommendation for Drupal, due to time constraints, WordPress was instead used for website development.

</br>

The following is an outline of each document within this folder, ordered by date of creation:
* The [Overview and Motivation](overviewAndMotivation.md) file outlines the current issues with the University of Edinburgh's Senate's file storage and search, as well as the goals to be achieved in the new prototyped application
* The [8 Week Plan](8weekPlan.md) file is the planned schedule of the internship, week by week
* The [Design Process](designProcess.md) file describes the process of the UI design of the application, and includes a Figma mockup for the homepage of the site
* The [Build Approach](buildApproach.md) file provides recommendations for possible build approaches of the web application, including evalutations of various from-scratch and out-of-the-box approaches, including CMS's such as Drupal. It also explores different possibilities for including keyword search, such as Apache Solr. 
* The [Hyperlinking](hyperlinking.md) file provides a workflow for how automated hyperlinking of references between papers could be implemented in the web application, focuses on automation of the pipeline, and evaluates a possible usage of XML files for this purpose
* The [Reflection](reflection.md) file reflects on my process throughout the internship, things that I felt went well, and things I would change
