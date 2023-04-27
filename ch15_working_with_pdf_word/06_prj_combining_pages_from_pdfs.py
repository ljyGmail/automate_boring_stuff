import PyPDF2
import os
from pathlib import Path

# Get all the PDF filenames.
pdfFiles = []

srcFolder = Path('data/ch15/pdf_files')

for filename in os.listdir(srcFolder):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(srcFolder / filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('data/ch15/allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)

pdfOutput.close()
