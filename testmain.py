# import pdfplumber
import re

with open("docs/Solverminds_Survey_Note.md", "r") as file:
    md_file = file.read()
    lines = md_file.splitlines()
    chunks = []
    for line in lines:
        # print("Lines :",line)
        heading_match = re.match(r'^(##+)', line)
        # print("Heading Match:", heading_match)
        if heading_match:
            print("Heading found on line:", line)
            print("Heading level:", len(heading_match.group(0)))
            print("Heading text:", line[heading_match.end():].strip())
            

        # else:
            # print("Not a heading:", line)
        
