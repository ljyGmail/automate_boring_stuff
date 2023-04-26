import PyPDF2

minutesFile = open('data/ch15/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)

pdfWatermarkReader = PyPDF2.PdfFileReader(
    open('data/ch15/watermark.pdf', 'rb'))

minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open('data/ch15/watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)

minutesFile.close()
resultPdfFile.close()
