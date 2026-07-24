# XML Schema
This document provides a description of the custom XML schema developed for representing Senate papers. 

<br/>

## General structure
* Entire document wrapped in a `<committeeDoc>` tag
* First section is metadata, containing the document type, committee name, start date, end date, academic year, and meeting number. This information is extracted automatically from a CSV file (or extracted manually via a filename convention if querying the CSV fails).
* Second section is an `<agenda>` item. This contains all text/tables/images before the first paper.
* Following the agenda, there are an arbitrary number of papers (wrapped in a `<paper>` tag). Each paper has a `paperCode` attribute, which is identified by a large text size (>12 px). Papers contain images, tables, and text.
* Images are encoded as Base64 strings, which allows the image to be stored directly in the XML, and are wrapped in an `<image>` tag. Each image has an `ext` attribute representing the extension (such as .png or .jpeg), which is used for rendering purposes.
* Hyperlinks are wrapped in an `<a>` tag. Each link has an `href` attribute for the actual link and the text of the tag is the display text of the link.
* Tables are represented through `<table>` tags, which comprise of rows (`<row>`), each row containing cells (`<cell>`). The cell itself contains the actual text. Text within cells can contain links, but will not contain any additional styling such as bold or italics. 
* Bolded text is wrapped in a `<boldText>` tag, which is rendered as bolded and with a margin above it (as bold text is often a subheading)
* Any other type of text is considered to be body text and is wrapped in a `<bodyText>` tag
* `</br>` tags are used for seperating bullet points/numbered lists and push the text to a new line

</br>

## Example - SEN_AP_20240522.pdf:
The following is an example of the general structure when applied to the` SEN_AP_20240522.pdf` document. It does not contain the actual text/exact structure of the extracted document but is more so for demonstration purposes.

```xml
<committeeDoc>
  <metadata>
    <documentType> AP </documentType>
    <committeeName> Senate </committeeName>
    <startDate> 22/5/2024 </startDate>
    <endDate> 22/5/2024 </endDate>
    <academicYear> 2023/2024 </academicYear>
    <meetingNumber> 3 </meetingNumber>
  </metadata>

  <agenda>
    <boldText> ... </boldText>
    <bodyText> ... </bodyText>
    <bodyText> ... </bodyText>
  </agenda>

  <paper paperCode="S 23/24 3A">
    <table>
      <row>
        <cell> ... </cell>
        <cell> ... </cell>
        <cell> ... </cell>
      </row>
      <row>
        <cell> ... </cell>
        <cell> ... </cell>
        <cell> ... </cell>
      </row>
    </table>
  </paper>

  <paper paperCode="S 23/24 3B>
    <bodyText> Search on <a href="google.com> Google </a> </bodyText>
    <img ext=".png"> ... </img>
  </paper>
<\committeeDoc>
```
