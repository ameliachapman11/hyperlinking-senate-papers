# Conversion from PDF to XML
**Overview:** the following file provides instructions on how to use the `xml_conversion.py` script to convert a PDF Senate paper to the custom XML schema designed for the purposes of the project, as outlined in the [XML Schema](../documentation/xml-schema.md) file within the `documentation` folder.

## Running the Script
### Arguments
The script takes two arguments, the first of which is required and the second of which is optional.

The first argument is the filepath for the input PDF document. Please note that it should be the filepath relative to the current working directory, not to where the `extract_xml.py` file is stored (although these will likely be the same). Some examples of what this argument may look like are `SEC_AP_20231109.pdf` or `assets/input/SEN_M_20240618.pdf`.

The second argument is the filepath for the desired destination of the outputted XML document, relevant to the current working directory.  Some examples of what this may look like are `march_senate_meeting.xml` or `assets/output/SEC_AP_20231109.xml`. Please note that if you choose to specify the output filepath, you must make sure the filename ends with `.xml` and you must include include `--output_filepath` before your filepath. If left blank, this argument will default to be the same directory as the input filepath, and the filename will be the same as the input file but with an extension of `.xml` instead of `.pdf`. 

The following are a few examples of what to run on your command line:
* `python extract_xml.py SEN_M_20240110_20240124_e.pdf`
* `python extract_xml.py SEC_AP_20231109.pdf --output_filepath /docs/result.xml`

</br>

### Filename Naming Conventions
The input files must follow a specific naming convention for the script to run correctly. In order to create the `<metadata>` section of the XML file, the script first queries a CSV file using filename and, if that fails, manually extracts the metadata via the naming convention.

The naming convention consists of the following parts, connected by underscores:
* **Committee abbreviation:** SEN for Senate, SEC for Education Committee, APRC for Academic Policy Regulations Committee, and SQAC for Quality Assurance Committee
* **Document type:** AP for Agenda & Papers or M for minutes
* **Date/start date:** must follow a YYYYMMDD format
* **(Optional) end date:** must follow a YYYYMMDD format, only for e-meetings which span across multiple days/weeks
* **Optional e:** to denote a paper is in regards to an e-meeting

</br>

**Examples of extracted information from the naming convention:**
Example 1: `SEC_AP_20231109.pdf`
* The naming convention tells us that this document is the Agenda & Papers document for the Senate Education Committee meeting that occurred on November 9, 2023
Example 2: `SEN_M_20240110_20240124_e.pdf`
* The naming convention tells us that this document is the Minutes document for the E-Senate meeting that lasted from January 10, 2024 to January 24, 2024

</br>

## CSV replacement
Currently, the script automatically extracts metadata via a CSV file. If you choose to replace the CSV file (as it currently only includes information for the Senate and SEC meetings from the 2023/2024 academic school year), there are a few steps you must follow. 

First, the CSV file should have the following column names:
* fileName: the file name without any extension
* documentType: either AP or M
* committeeName: the abbreviation of the committee name, except for in the case of "Senate" or "E-Senate"
* startDate: following DD/MM/YYYY format
* endDate: following DD/MM/YYYY format
* academicYear: following YYYY/YYYY format
* meetingNumber

Notes:
* In order for the script to run correctly, the column names as described above *must* be used. The actual formatting of each metadata value is left to the user. I have described above the formatting that I chose to implement.
* If a meeting only spans one day, `startDate` and `endDate` will have the same value.

<br/>

**Alterations to code:** Once your new CSV file has been created, please place it in the same directory as the script and then go down to the `if __name__ == "__main__"` section at the bottom. Replace the value of the `csv_filepath` variable with the filepath of your desired CSV file. 
