import PyPDF2
with open("C:/Users/User/Desktop/DeckSheet_20221219090709.pdf", "rb") as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    print(page.extractText())
