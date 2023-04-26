import PyPDF2

minutesFile = open('data/ch15/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
print(f'page.rotateClockwise(90): {page.rotateClockwise(90)}')

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)

resultPdfFile = open('data/ch15/rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)

resultPdfFile.close()
minutesFile.close()
