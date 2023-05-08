from pdfminer.high_level import extract_pages
 
FILE_PATH = R"C:/Users\User/Desktop/資格手当（研究職用）/会社説明資料_ワールドインテックRD_改訂23.02.03.pdf"
 
text = extract_pages(FILE_PATH)
print(text)
