import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb['Sheet']
italic24Font = Font(size=24, italic=True)  # Create a font.
sheet['A1'].font = italic24Font  # Apply the font to A1.
sheet['A1'] = 'Hello, world!'

fontObj1 = Font(name='Times New Roman', bold=True)
sheet['A5'].font = fontObj1
sheet['A5'] = 'Bold Times New Roman'

fontObj2 = Font(size=24, italic=True)
sheet['A10'].font = fontObj2
sheet['A10'] = '24 pt Italic'

wb.save('data/ch13/styles.xlsx')
