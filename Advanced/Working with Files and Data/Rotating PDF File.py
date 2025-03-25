from PyPDF2 import PdfReader, PdfWriter
import pandas as pd

def rotate_pdf(input_pdf, output_pdf, rotation_angle):
    with open(input_pdf, "rb") as file:
        pdf_reader = PdfReader(file)
        pdf_writer = PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page.rotate(rotation_angle)
            pdf_writer.add_page(page)
            
        with open(output_pdf, "wb") as output_file:
            pdf_writer.write(output_file)

        
input_pdf = "D:\\101 Python Course 2025\\Advanced\\Working with Files and Datas\\story.pdf"
output_pdf = "D:\\101 Python Course 2025\\Advanced\\Working with Files and Datas\\rotated_story.pdf"
rotate_pdf(input_pdf, output_pdf, 90)
