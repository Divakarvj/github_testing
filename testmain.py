# import pdfplumber

with open("docs/Solverminds_Survey_Note.md", "r") as file:
    md_file = file.read()
    lines = md_file.splitlines()

    for line in lines:
        # print("Lines :",line)
        
        if line.startswith("#")  or line.startswith("##") or line.startswith("###"):
            print("Heading found:", line)
