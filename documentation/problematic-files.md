# Problematic files
**Overview:** the conversion from PDF to XML, though generally maintaining the structure of documents well, comes with a loss of some information. The following are specific instances of information loss/incorrect extraction that demonstrate the shortcomings of the script developed. These issues may be addressed in the future. Many of the issues listed are found throughout many documents, although only a single specific example is provided.

**SEN_AP_20240618**
* Page 9 says "Any changes to the membership are highlighted in yellow" but the way that the way text is currently extracted does not preserve highlighting
* Pages 20-21: visually it is clear that the "Proposed Priority" row should be part of the same table as continues on the next page. However, currently the extraction script starts a new table when there is a new page, which will result in a visual break in the rendering.
* Page 29: visually it is clear that there are two columns, one for author and one for presenter. However, the script reads line by line so the information associated with author/presenter will not be clearly lined up or interpretable in the output.
* Page 33: although the first table cell is purposefully blank, the script skips it and so the second column in the row will be instead intepreted as the first column. In other words, the column will not line up correctly with the column on the previous page that it is intended to be continued from.

**SEN_AP_20240522**
* Page 29 has some misplaced bullet points. The extracted text contains "• •" followed by "Clear governance and openness in decision making [...]" and "CMVM as a learning organisation [...]" which are both meant to be associated with those bullet points
* Page 31: another instance of a misaligned table. Current School/Deanery should be one column to the right from where it is, but is not as we do not retain empty cells.
* Page 31: the text between the two tables (number 14.) has been lost
* Page 35: As the image includes text that can be interacted with (it can be highlighted/copied, unlike the text in the image on page 32, suggesting a different image format), it is extracted as text rather than an image. This loses all of the structure and color of the image, meaning all original meaning is lost.
* Page 42: Similar to page 35; this table would be best interpreted as an image but is instead interpreted as a table. It does not retain the placement of the text communicating which months certain events occur. All original meaning of the table is lost.
* Page 42: the heading of "H/02/02/02" should have been eliminated by the script but remains in the paper title
* Page 45: footnotes appear as by their location in the text, as expected. However, this means it seems that there are just random links within the paper's text as opposed to being clearly a footnote
* Page 53: the image is again being interpreted as text and all meaning is lost
* Page 54: the image is being rendered on a black background even though it should be white. This may be an issue with conversion to Base64 string. Same issue appears on pages 58-62.
* Pages 69-70: there is a black image/bar on the break between the two pages. It is not clear why an image was detected here.
* Page 74: cells containing text "TBC &mdash; election outcomes not yet known" is being interpreted as multiple cells where there are linebreaks &rarr; may be an issue with the highlighting?
* Page 81: has extracted the text "Rationale and fit" twice and put it into a new cell
* Pages 84-85: when a table cell should be continued over a page (based on rules such as lowercase start which indicates continuation of the same sentence), it is instead part of a separate table due to current definition of when to begin a new table
* Page 93: The link to "Senate Education Committee" was not detected. This is often due to the exact bounding box of the cell and/or the link not being extracted correctly. However, if we increase the tolerance, then it will begin to include text in the link that should not be included.
* Page 108: list item 10. was interpreted as a table. It is not clear why. 

General issues
* Loss of specific formatting information like highlighting, italics, alternative font color -> necessary to retain or unnecessary information?
* Blank cells in tables may cause misalignment -> make it so that there is a blank cell so that it correctly aligns with the column as included in the dict?
* Visual columns without clear table boundaries will not be rendered correctly/clearly interpretable
* New lines are not kept within tables (so that the width of a paragraph is not limited to what it originally was in the PDF); however, this may cause large blocks of text within a table cell which is difficult to read
* Footnotes --> is it possible to assemble all footnotes for a paper and append it in a `<footnotes>` tag after all of the other text?
