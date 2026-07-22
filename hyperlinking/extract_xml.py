# Imports
import pymupdf
from lxml import etree
import re
import pandas as pd
import base64
import argparse
import os

# Returns true if a block overlaps with any of the bounding boxes provided
def overlaps(block_bbox, bboxes):
    ax0, ay0, ax1, ay1 = block_bbox
    for bx0, by0, bx1, by1 in bboxes:
        if ax1 < bx0 + 1.5 or ax0 > bx1 - 1.5 or ay1 < by0 + 1.5 or ay0 > by1 - 1.5: # no overlap (with 1.5 px margin)
            continue
        return True
    return False

# Returns a dictionary of all hyperlinks on a page w/ the link's bbox and display text
def get_page_links(page):
    links = []
    for link in page.get_links():
        if link.get('uri'):
            bbox = link['from']
            display_text = page.get_textbox(bbox).strip()
            links.append({
                'bbox': bbox,
                'uri': link['uri'],
                'display_text': display_text,
            })
    return links

# Returns a dictionary of text spans w/ the matching link -> Used for text blocks
def find_links_in_spans(line_spans, page_links):
    found_links = []
    for span in line_spans:
        sx0, sy0, sx1, sy1 = span['bbox']
        for link in page_links:
            lx0, ly0, lx1, ly1 = link['bbox']
            # Check for matching bbox (w/ 1.5 pt tolerance)
            if sx0 >= lx0 - 1.5 and sy0 >= ly0 - 1.5 and sx1 <= lx1 + 1.5 and sy1 <= ly1 + 1.5:
                found_links.append({
                    'text': span['text'], 
                    'uri': link['uri'],    
                })
    return found_links

# Returns a dictionary of display text w/ the matching link -> Used for table cells
def find_links_in_cell(cell_bbox, page_links):
    found_links = []
    cx0, cy0, cx1, cy1 = cell_bbox
    for link in page_links:
        lx0, ly0, lx1, ly1 = link['bbox']
        # Check to see if link bbox falls completely within cell bbox (w/ 1.5 pt tolerance)
        if lx0 >= cx0 - 1.5 and ly0 >= cy0 - 1.5 and lx1 <= cx1 + 1.5 and ly1 <= cy1 + 1.5:
            found_links.append({
                    'text': link['display_text'], 
                    'uri': link['uri'],    
                })
    return found_links

# Joins all accumulated lines into one block dict
def make_sub_block(current_lines):
    text = " ".join(l['text'] for l in current_lines) 
    text = re.sub(r'\s+', ' ', text).strip() # get rid of extra whitespace caused by linebreaks
    if not text:
        return None
    return {
        'text': text,
        'font_size': current_lines[0]['font_size'],
        'font': current_lines[0]['font'],
        'bold': current_lines[0]['bold'],
        'bbox': current_lines[0]['bbox'],
        'type': 'text',
        'links': [link for l in current_lines for link in l.get('links', [])] # prevents key error on lines w/o links
    }

# Returns whether a text block is a page number
def is_page_num(block):
    text = block['text'].strip()
    if block['type'] != 'text':
        return False
    # Matches page numbers: "1", "12", etc.
    if re.fullmatch(r'\d+', text):
        return True
     # Matches "Page 1 of 9", "Page 12 of 100", etc. 
    if re.fullmatch(r'[Pp]age\s+\d+\s+of\s+\d+', text):
        return True
    return False

# Seperates bullet points and numbered lists in a block
def clean_bullet_points(text):
    text = re.sub(r'\s*•', '\n•', text)
    text = re.sub(r'\s*(?<!\w)o(?!\w)', '\n•', text)
    text = re.sub(r'\s*(\d+\.) ', r'\n\1 ', text) # numbered list
    return text.strip()

# Extracts each table on a page and returns an array of dict blocks
def extract_table_blocks(page, page_blocks, table_bboxes, page_links):
    for table_i, table in enumerate(page.find_tables()):
            table_bboxes.append(table.bbox)
            
            rows = table.extract()
            for row_i, row in enumerate(rows):
                for col_i, cell_text in enumerate(row):
                    # Skip empty cells
                    if not cell_text or not cell_text.strip():
                        continue
                    
                    # Get individual cell bbox from table.cells
                    cell_bbox = table.rows[row_i].cells[col_i]
                    
                    page_blocks.append({
                        'text': re.sub(r'\s+', ' ', cell_text).strip(),
                        'type': 'table',      
                        'row': row_i,      
                        'col': col_i,  
                        'table_i': table_i,    
                        'page_i': page.number, 
                        'bbox': table.bbox, # bbox for the whole table 
                        'links': find_links_in_cell(cell_bbox, page_links) 
                    })
                    
# Extracts each image on a page and returns an array of dict blocks
def extract_img_blocks(doc, page, page_blocks):
    for img in page.get_images():
            xref = img[0]
            bbox = page.get_image_rects(xref)[0] # bbox of image
            if not bbox:
                continue
            
            # Extract the image's raw data 
            raw_img = doc.extract_image(xref)
            if raw_img:
                img_bytes = raw_img['image']  # Raw binary data
                img_ext = raw_img['ext'] # such as PNG or JPG -> needed for rendering
                
                # Convert the binary bytes into a Base64 string -> image will live entirely in the XML
                base64_encoded = base64.b64encode(img_bytes).decode("utf-8")
                
                page_blocks.append({
                    'type': 'img',
                    'bbox': list(bbox), # need to convert rect object to list
                    'image_data': base64_encoded,
                    'image_ext': img_ext
                }) 

# Extracts body text blocks in a page and returns an array of dict blocks
def extract_body_text_blocks(page, page_blocks, table_bboxes, page_links):
    blocks = page.get_text('dict', sort = True)['blocks']
    for block in blocks:
        # Skip blocks if it overlaps w/ tables or is an image
        if overlaps(block['bbox'], table_bboxes) or block['type'] != 0:
            continue
        
        # Build a metadata dictionary per line
        lines_meta = []
        for line in block['lines']:
            spans = line['spans']
            if not spans:
                continue
            
            # Get rid of unnecessary heading frequently at the top of SEN papers
            cleaned_spans = []
            for span in spans:
                updated_text = span['text'].replace('H/02/02/02', '').strip()
                if updated_text:
                    span['text'] = updated_text
                    cleaned_spans.append(span)
            spans = cleaned_spans
            if not spans:
                continue
                
            # Combine text across all spans for the line
            line_text = ' '.join(span['text'] for span in spans).strip()
            
            # Identify the 'dominant' span (the longest text piece) to represent the line's style
            line_dominant = max(spans, key=lambda s: len(s['text'])) 
            
            lines_meta.append({
                'text': line_text,
                'bbox': line_dominant['bbox'],
                'font': line_dominant['font'],
                'font_size': line_dominant['size'],
                'bold': bool(line_dominant['flags'] & 16), # Bitwise check for bold flag
                'type': 'text',
                'links': find_links_in_spans(spans, page_links) 
            })

        # Group lines together into sub-blocks based on formatting continuity
        sub_blocks = []
        current_lines = [] 
        
        for line in lines_meta:
            if not current_lines:
                current_lines.append(line)
                continue

            prev_line = current_lines[-1] # last item in the array
            should_split = False

            # Split conditions: change in size, font, bold state, or large whitespace gaps
            if abs(line['font_size'] - prev_line['font_size']) > 1:
                should_split = True
            elif line['font'] != prev_line['font']:
                should_split = True
            elif line['bold'] != prev_line['bold']:
                should_split = True
            elif re.search(r'\n{2,}', line['text']):
                should_split = True
            elif re.search(r'\s{3,}', line['text']):
                should_split = True

            if should_split:
                new_block = make_sub_block(current_lines)
                if new_block is not None:
                    sub_blocks.append(new_block)
                current_lines = [line] # Reset and start a new sub-block with the current line
            else:
                current_lines.append(line) # Append to the ongoing sub-block

        # Add the final accumulated group of lines
        if current_lines:
            text = ' '.join(l['text'] for l in current_lines)
            text = re.sub(r'\s+', ' ', text).strip()
            if text:
                new_block = make_sub_block(current_lines)
                if new_block is not None:
                    sub_blocks.append(new_block)

        # Save valid sub-block
        for block in sub_blocks:
            if block['text']:
                page_blocks.append(block)                  

# Extract blocks across all pages of a document
def extract_blocks(doc):
    all_blocks = []
    for page in doc:
        page_blocks = []
        page_links = get_page_links(page)
        
        # Extract tables
        table_bboxes = []
        extract_table_blocks(page, page_blocks, table_bboxes, page_links)
                        
        # Extract images
        extract_img_blocks(doc, page, page_blocks)
        
        # Extract body text
        extract_body_text_blocks(page, page_blocks, table_bboxes, page_links)
                        
        # Sort blocks in page to appear by position
        # Table and image blocks were added first, which may not reflect the actual position on the page
        page_blocks.sort(key=lambda b: b['bbox'][1])
        
        # Put newlines where there are bulletpoints ("•" or "o") for rendering
        for block in page_blocks:
            if block['type'] != 'img':
                block['text'] = clean_bullet_points(block['text'])
        
        all_blocks.extend(page_blocks)
                
    # Merge blocks across pages that are part of the same paragraph together
    extracted_blocks = []
    buffer = None
    seen_images = set()

    for block in all_blocks:
        # If we encounter an image, clear out the buffer
        if block['type'] == 'img':
            # Skip duplicate images throughout doc
            if block['image_data'] in seen_images:
                continue
            seen_images.add(block['image_data'])
            
            if buffer:
                extracted_blocks.append(buffer)
                buffer = None
            extracted_blocks.append(block)
            continue
            
        # Leave out page numbers
        if is_page_num(block):
            continue
            
        # If there's no active buffer, make this block the buffer
        if buffer is None:
            buffer = block
            continue

        # Check for paragraph continuation rules
        curr_text = block['text']
        same_sentence = False
        if curr_text:
            lowercase_start = curr_text[0].islower()
            same_font_size = True
            if block['type'] == 'text' and buffer['type'] == 'text':
                same_font_size = not abs(block['font_size'] - buffer['font_size']) > 1
            same_sentence = lowercase_start and same_font_size
        list_item = re.fullmatch(r'\d+\.', buffer['text'])
        bullet_point = re.fullmatch(r'•', buffer['text'])
        same_paragraph = same_sentence or list_item or bullet_point
        
        # If part of the same paragraph, append text to buffer, otherwise begin new block
        if same_paragraph:
            buffer['text'] = buffer['text'] + ' ' + curr_text
        else:
            extracted_blocks.append(buffer)
            buffer = block

    # Append last accumulated block
    if buffer:
        extracted_blocks.append(buffer)
    
    return extracted_blocks

# Extract metadata automatically from CSV
def fetch_metadata_from_csv(target_file, csv_path):
    csv = pd.read_csv(csv_path)
    match = csv[csv['fileName'] == target_file] # target file should have no ext (such as .pdf)
    if match.empty:
        return None
    else:
        return match.iloc[0].to_dict() # grabs first matching row & converts to dictionary

# Extract metadata automatically from filename (does not extract meeting number)
def extract_metadata_from_filename(target_file):
    parts = target_file.split('_')
    e_meeting = len(parts) > 3
    
    # Extract doc type
    extracted_doc_type = parts[1]

    # Extract committee name
    extracted_committee_name = None
    if parts[0] == 'SEN': #in the CSV file, Senate and E-Senate do not keep abbreviation
        if e_meeting:
            extracted_committee_name = 'E-Senate'
        else:
            extracted_committee_name = 'Senate'
    else:
        extracted_committee_name = parts[0]
        
    # Extract meeting date(s)
    extracted_start_date = None
    extracted_end_date = None

    if e_meeting: # seperate start and end dates
        extracted_start_date = parts[2]
        extracted_end_date = parts[3]
    else:
        extracted_start_date = extracted_end_date = parts[2]
    
    # Extract academic year 
    year = int(extracted_start_date)[:4] 
    new_academic_year = f"{year}0801" # New academic year starts August 1 of the year
    extracted_academic_year = f"{year}/{year+1}" if extracted_start_date >= new_academic_year else f"{year-1}/{year}"
    
    def fix_date_formatting(d): # DD/MM/YYYY
        if d:
            return f"{d[6:]}/{d[4:6]}/{d[:4]}"
        return None
    extracted_start_date, extracted_end_date = map(fix_date_formatting, (extracted_start_date, extracted_end_date))
    
    return {
        'fileName': target_file,
        'documentType': extracted_doc_type,
        'committeeName': extracted_committee_name,
        'startDate': extracted_start_date,
        'endDate': extracted_end_date,
        'academicYear': extracted_academic_year,
        'meetingNumber': 'Unknown'
    }

# Extract metadata
def extract_metadata(file, csv_filepath):
    filename = file.name.removesuffix('.pdf')
    
    # Validate filename follows naming conventions
    valid_meeting_pattern = r"^(SEN|SEC|APRC|SQAC)_(AP|M)_20\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])$" #supports years 2000-2099
    valid_e_meeting_pattern = r"^(SEN|SEC|APRC|SQAC)_(AP|M)_20\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])_20\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])_e$"
    if not(re.match(valid_meeting_pattern, filename) or re.match(valid_e_meeting_pattern, filename)):
        raise Exception('Invalid filename format')
    
    # Try extraction from CSV first
    metadata = fetch_metadata_from_csv(filename, csv_filepath)
    
    # Fallback to data extraction from filename
    if metadata is None:
        metadata = extract_metadata_from_filename(filename)
        
    return metadata

# Creates a <tag> element under parent_el
    # Embeds links as <a> inline
    # Creates a <br> tag before each bullet point so it displays on a new line
def build_text_el(parent_el, tag, block):
    el = etree.SubElement(parent_el, tag)
    links = block.get('links', [])
    
    # Split on newlines —> marks where bullet point begins
    parts = block['text'].split('\n')
    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
        
        if i > 0: # no need for an empty newline before the first bit of text
            br = etree.SubElement(el, 'br')
        
        # For each part, find which links fall within it
        part_links = [l for l in links if l['text'] in part]
        
        # If no links, set text directly
        if not part_links:
            if i == 0: # no <br> beforehand
                el.text = (el.text or '') + part
            else:
                br.tail = part
        # Else, build inline <a> tags for each link
        else: 
            remaining_text = part
            
            for link in part_links:
                link_text = link['text']
                
                # Find where the linked text sits within the remaining text
                link_i = remaining_text.find(link_text)
                if link_i == -1:
                    continue
                
                before = remaining_text[:link_i]
                after = remaining_text[link_i + len(link_text):]
                
                # Set text before the link
                if len(el) == 0:
                    el.text = (el.text or '') + before 
                else:
                    el[-1].tail = (el[-1].tail or '') + before # el[-1] is the last <a> tag
                
                # Create the inline <a>
                a = etree.SubElement(el, 'a')
                a.set('href', link['uri'])
                a.text = link_text
                a.tail = ''
                
                # Remaining text in part to be processed
                remaining_text = after
            
            # Set remaining text after the last link
            el[-1].tail = (el[-1].tail or '') + remaining_text
    
    return el

# Converts pdf file to xml file 
def convert_pdf_to_xml(file, csv_filepath):
    root = etree.Element('committeeDoc')
    tree = etree.ElementTree(root)

    # Connect to the XSLT styling sheet
    xslt = etree.ProcessingInstruction(
        'xml-stylesheet', 'type="text/xsl" href="style.xslt"'
    )
    root.addprevious(xslt)

    # Extract & add metadata (docType, committeeName, startDate, endDate, academicYear, meetingNumber)
    metadata = extract_metadata(file, csv_filepath)
    metadata_el = etree.SubElement(root, 'metadata')
    doc_type = etree.SubElement(metadata_el, 'documentType')
    doc_type.text = metadata['documentType']
    committee_name = etree.SubElement(metadata_el, 'committeeName')
    committee_name.text = metadata['committeeName']
    start_date = etree.SubElement(metadata_el, 'startDate')
    start_date.text = metadata['startDate']
    end_date = etree.SubElement(metadata_el, 'endDate')
    end_date.text = metadata['endDate']
    academic_year = etree.SubElement(metadata_el, 'academicYear')
    academic_year.text = metadata['academicYear']
    meeting_num = etree.SubElement(metadata_el, 'meetingNumber')
    meeting_num.text = str(metadata['meetingNumber'])
    
    # First item will always be the agenda, then the papers
    agenda_el = etree.SubElement(root, 'agenda')

    # Loop through extracted blocks
    current_item = agenda_el
    current_table = None
    current_table_i = -1
    current_row = None
    current_row_i = -1
    current_page_i = -1
    current_paper_code = None
    for block in extract_blocks(file):
        type = block['type']
        
        if type == 'img':
            img_el = etree.SubElement(current_item, 'image', ext = block['image_ext'])
            img_el.text = block['image_data']
        
        elif type == 'table':
            # Create a new table when either the page or the table index changes
            # TODO could also enforce that if they're the same row, it has to make sense in terms of col number instead of splitting by page
            # TODO could also keep track of number of columns in prev table, if there is the same number of columns here then it is prob part of the same table
            is_new_table = (
                block['page_i'] != current_page_i or
                block['table_i'] != current_table_i
            )

            if current_table is None or is_new_table:
                current_table = etree.SubElement(current_item, 'table')
                current_row = None
                current_row_i = -1
                current_table_i = block['table_i']
                current_page_i = block['page_i']

            # Create a new row when the row index changes
            if block['row'] != current_row_i:
                current_row = etree.SubElement(current_table, 'row')
                current_row_i = block['row']

            build_text_el(current_row, "cell", block)
        
        elif type == "text":
            text = block["text"]
            font_size = block["font_size"]
            bold = block["bold"]
            
            # Reset table
            current_table = None
            current_table_i = -1
            current_row = None
            current_row_i = -1
            current_page_i = -1
            
            if font_size > 12: # paper code identified by large font size
                # Only start a new paper if the paper code is different from the current one
                if current_paper_code == text:
                    continue
                else:
                    paper_el = etree.SubElement(root, 'paper', paperCode = text)
                    current_item = paper_el
                    current_paper_code = text
            elif bold:
                build_text_el(current_item, 'boldText', block)
            else:
                build_text_el(current_item, 'bodyText', block)   
    return tree

# Make it run as a script
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    # Required argument for input PDF filepath
    parser.add_argument('input_filepath')
    
    # Optional argument for where the outputted XML should be stored
    parser.add_argument('--output_filepath', default=None)
    
    args = parser.parse_args()
    
    # Check the input file actually exists
    if not os.path.exists(args.input_filepath):
        print(f"Error: file '{args.input_filepath}' not found.")
        exit(1)
    
    # Work out the output path
    if args.output_filepath:
        output_path = args.output_filepath
    else:
        input_dir = os.path.dirname(os.path.abspath(args.input_filepath))
        input_name = os.path.splitext(os.path.basename(args.input_filepath))[0]
        output_path = os.path.join(input_dir, f"{input_name}.xml")
    
    # Open the document and run your existing pipeline
    doc = pymupdf.open(args.input_filepath)
    csv_filepath = 'SenatePapers23-24.csv'
    tree = convert_pdf_to_xml(doc, csv_filepath) 
    
    # Save the XML
    with open(output_path, 'wb') as f:
        tree.write(f, xml_declaration = True, encoding = 'utf-8', pretty_print = True)
    
    print(f"Done — XML saved to {output_path}")