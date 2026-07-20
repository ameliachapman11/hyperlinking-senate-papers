# Design Process of Web Application

## Inspiration
For the structure of the web application, I took inspiration from academic databases such as ProQuest, JSTOR, IEEE Xplore, DiscoverEd, and ScienceDirect. Academic databases are specialized search platforms for journals, scholarly articles, textbooks, etc. The goal of the web application we are developing for the University of Edinburgh's Senate is largely the same&mdash;users should be able to search through Senate papers that match entered keywords as well as filter the relevant results. 

## Mockup
The following is a mockup of the UI of the web application, created using Figma. The mockup lacks functionality and is entirely for visual purposes to shape the development of the future prototype.

The official brand guidelines of the University of Edinburgh were followed. Source sans pro was used for all navigational elements and in-page elements (headings, links, button text, etc.). Crimson text was used for the banner headings. University red (hex code D50032) was used for banners and as an accent color. For more information on the standards used for development, reference the following links for [typography](https://gel.ed.ac.uk/legacy/foundations/typography/) and [color theming](https://gel.ed.ac.uk/legacy/foundations/colour/).

[Link to Figma mockup prototype](https://www.figma.com/proto/AK8cc36Ifu0WSqUknUchYs/UoE-Senate-Search?node-id=0-1&t=kUomcy5QFbOxt5IN-1)
![Mockup of a search application for Senate papers, with filters and results](./assets/UoE%20Senate%20Search.png)

## Key Features
* **Search bar:** In the search bar at the top of the page, users can enter keywords such as "Scottish Funding Council" or "Informatics" to bring up papers containing the keywords.
* **Refine results:** Users can refine results by filtering by committee or by the academic year in which the meeting occurred. The filter lists are collapsible. There is opportunity to expand the filters, perhaps by adding "Paper type" (agenda and papers, minutes, report, etc.).
* **Sort results:** Users can sort results either by relevance (the paper in which the keyword occurs most often at the top), newest first, or oldest first
* **PDF's:** Users can access the PDF's by clicking on the title of the PDF, which will be turned blue and underlined when a user hovers over it to demonstrate that it is a hyperlink
