import docx


def getText(filename, linefeed=1, indent=False):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        prefix = '    ' if indent else ''
        fullText.append(prefix + para.text)

    return (linefeed * '\n').join(fullText)


print(
    f"getText('data/ch15/demo.docx'):\n{getText('data/ch15/demo.docx', linefeed=2, indent=True)}")
