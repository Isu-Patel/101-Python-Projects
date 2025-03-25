from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        # Create a PDF reader object
        pdf_reader = PdfReader(file)
        
        # Extract text from each page
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
 
pdf_path = "D:\\101 Python Course 2025\\Advanced\\Working with Files and Datas\\story.pdf"
text_from_pdf = extract_text_from_pdf(pdf_path)
print(text_from_pdf)
