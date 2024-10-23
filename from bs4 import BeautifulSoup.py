from bs4 import BeautifulSoup
with open ("html_doc.html", encoding='utf-8')as file: 
    soup = BeautifulSoup(file, 'xml')   

print(soup.title)