# Current Progress
## Web App Development
* Evaluations of possible build approaches, recommendation being a CMS
* Began developing website in a LocalWP dev environment
* Have currently configured the custom taxonomy and custom post type to correctly take in the metadata/files for a paper
* Homepage: displays all papers; can filter by document type, committee, and academic year; can sort papers by date (newest first or oldest first)

## Hyperlinking Pipeline
* Outline of pipeline/main goal
* Development of custom XML schema
* Python script for converting PDFs to custom schema. Generally works well on Minutes documents but struggles on longer Agenda & Papers documents where there is more atypical formatting, complicated table structure, variety of image type, etc.
* XML can be rendered as HTML using XSLT sheet
