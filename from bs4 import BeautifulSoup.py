from bs4 import BeautifulSoup
with open ("html_doc3.html", encoding='utf-8')as file: 
    soup = BeautifulSoup(file, 'xml')   

def extract_title():
    titles = soup.find_all('h4', class_="meta__title meta__title__margin")

    # Extract and return the titles
    for index, title in enumerate(titles, 1):
        title_text = title.get_text(strip=True)
        return f"{index}. {title_text}"


def extract_autor():
    autors = soup.find_all('ul', class_="meta__authors rlist--inline" )


    for index2, autor in enumerate(autors, 1):
        autor_text = autor.get_text(strip= True)
        print(f"{index2}. {autor_text}")

