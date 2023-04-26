import PyPDF2

pdfFileObj = open('data/ch15/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(f'pdfReader.numPages: {pdfReader.numPages}')

pageObj = pdfReader.getPage(0)
print(f'pageObj.extractText(): {pageObj.extractText()}')

pdfReader = PyPDF2.PdfFileReader(open('data/ch15/encrypted.pdf', 'rb'))

print(f'pdfReader.isEncrypted: {pdfReader.isEncrypted}')

# pdfReader.getPage(0)  # PyPDF2.utils.PdfReadError: file has not been decrypted

# pdfReader = PyPDF2.PdfFileReader(open('data/ch15/encrypted.pdf', 'rb'))

print(f"pdfReader.decrypt('rosebud'): {pdfReader.decrypt('rosebud')}")

pageObj = pdfReader.getPage(0)
