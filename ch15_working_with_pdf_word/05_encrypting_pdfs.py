import PyPDF2

pdfFile = open('data/ch15/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('swordfish')

resultPdf = open('data/ch15/encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)

resultPdf.close()
pdfFile.close()
