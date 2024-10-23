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

meta_dates = soup.find_all('div', class_="meta__details")
for i3, meta_date in enumerate(meta_dates, 1):
    this_soup = BeautifulSoup(str(meta_date), 'xml')
    journal = this_soup.find('a', class_="meta__serial")
    journal_text = journal.get_text(strip=True)
    date = this_soup.find('span', class_="meta__epubDate")
    date_text = date.get_text(strip=True)if date else "Not found"
    print(f"{i3}. journal: {journal_text}, date: {date_text}")
