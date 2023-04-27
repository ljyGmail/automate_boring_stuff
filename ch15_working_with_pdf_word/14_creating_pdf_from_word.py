import win32com.client
import docx

# Not working...
wordFilename = 'data/ch15/word2pdf.docx'
pdfFilename = 'data/ch15/word2pdf.pdf'

doc = docx.Document()
doc.add_heading('Header 0', 0)
doc.save(wordFilename)

wdFormatPDF = 17  # Word's numeric code for PDFs.
wordObj = win32com.client.Dispatch('Word.Application')
docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)

docObj.Close()
wordObj.Quit()
