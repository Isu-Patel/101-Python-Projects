# from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader

# Open the PDF file and get the number of pages
def get_page_count(pdf_path):
    pdf_reader = PdfReader(pdf_path)
    num_pages = len(pdf_reader.pages)
    return num_pages

pdf_path = "D:\\101 Python Course 2025\\Advanced\\Working with Files and Datas\\story.pdf"
page_count = get_page_count(pdf_path)
print(f'The number of pages in the PDF file is: {page_count}')
