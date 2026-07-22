# Conversion from PDF to XML
**Overview:** the following file provides instructions on how to use the `xml_conversion.py` script to convert one a PDF text file to the custom XML schema designed for the purposes of the project, as outlined in the `hyperlinking.md` document within the `documentation` folder.

# TODO
* Add in hyperlink to other docs mentioned in overview
* Include instructions about CSV replacement. Currently the script automatically extracts information from a CSV file (will also extract automatically from the filename if this fails). Column names: fileName, documentType, committeeName, startDate, endDate, academicYear, meetingNumber. The fileName should follow the naming conventions as outlined in the `hyperlinking.md file`. The dates should follow DD/MM/YYYY format. documentType is either AP for Agenda & Papers or M for Minutes. academicYear follows a YYYY/YYYY format. To replace the CSV file used, go down to the `if __name__ == "__main__"` section at the bottom and replace the `csv_filepath` variable with the filepath of your desired CSV file. 
* Include instructions on how to run on command line, where outputted file will be stored
* First argument is filepath for the input PDF document from the CWD
* The second optional argument is the filepath for the desired destination of the outputted XML document from the CWD. If left blank it will be the same as the input filepath.
* An example of running the script: first cd into the hyperlinking folder, then run `SEN_M_20240110_20240124_e.pdf`