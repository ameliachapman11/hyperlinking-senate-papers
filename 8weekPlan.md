# LFCS Internship - 8 Week Plan
## Week 1
* Become familiarized with the structure of the University of Edinburgh's Senate, what each committee is responsible for, how archive documents are currently stored on the Registry Services Website
* Read through a selection of Senate papers to become familiarized with the type of content we are dealing with, frequency of existing hyperlinking, and to understand the extent of interconnectedness between the papers (how often do they explicity refer to each other?)
* Look into Links as a possible solution for developing a web application, understand its capabilities and structure, alternative CSS frameworks that could be combined with it

## Week 2
* Look into various content management systems as possible solutions for the web application
* Look into frontend, backend, and fullstack frameworks as possible solutions
* Look at the UI structure of existing academic database-style software for inspiration and create Figma mockup in line with the University's branding identity
* Begin documentation providing suggestions for build approach, which one would be most appropriate for this project

## Week 3
* Finish documentation of build approach suggestions, present to advisor for approval
* Look further into alternative methods of storing Senate papers, moving away from PDF's and focusing on hyperlinking function
* (If recommendations approved by advisor) Begin building a concrete prototype of the website

## Weeks 4-6
Implement features:
* Add a search function to the web app so users can enter keywords and relevant Senate documents will be brought up
* Add filtering, so users can filter by academic year, committee, etc. (dependent on feedback from the requirements gathering meeting) &rarr; requires being able to add tags to documents
* Add a way for users to sort results, possibly by alphabetical order, oldest first, newest first, etc.
* Add a spellcheck feature so that if users misspell keywords, the app will find a close match
* (If possible) Bring up and display hyperlinks relevant to the keywords from across the university's digital ecosystem, extending search beyond just within the Senate documents
* (If possible) Extend keyword search to be beyond just exact matches, brings up related results (ex. if a user searches for the keyword "parent," the app will also bring up documents that contain the word "family")

## Week 7
* Focus on testing, finding edge cases, making small tweaks to polish up before meeting
* Begin implementing changes based on meeting

## Week 8
* Coding &rarr; Continue implementing suggested changes, polish project
* Create formal documentation reflecting on project and prototype created

## Additional notes/possible risks
* Feature implementation in weeks 3-6: The order of implementation for the various features is flexible; some may take more or less time to implement than expected depending on the selected build approach and thus may be shifted week by week. Additionally, before the build approach is decided on, it is not possible to know what existing technology/API's may be combined with it, and thus what features are viable for the timeline of the project.
* Testing: Testing will be done throughout the process of implementing features rather than as a seperate task. The note on testing in week 7 provides dedicated time for edge cases beyond the expected/primary functionality of the prototype. 
* Accuracy: Consistency of quality of the PDFs and way their metadata is tagged is variable, which could affect search accuracy, filtering, and a possible implementation of automated hyperlinking. Some of the PDF's have sections which appear to have been altered later, with old text being crossed off in red. Additionally, metadata tagging will be done manually, which leaves room for human error.
