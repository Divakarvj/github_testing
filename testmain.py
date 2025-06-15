# import pdfplumber

with open("docs/Solverminds_Survey_Note.md", "r") as file:
    md_file = file.read()
    lines = md_file.splitlines()

    for line in lines:
        print("Lines :",line)