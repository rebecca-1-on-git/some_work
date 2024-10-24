from bs4 import BeautifulSoup
import regex as re
with open ("html_doc3.html", encoding='utf-8')as file: 
    soup = BeautifulSoup(file, 'xml')   

def extract_title():
    titles = soup.find_all('h4', class_="meta__title meta__title__margin")
    title_list = []
    # Extract and return the titles
    for index, title in enumerate(titles, 1):
        title_text = title.get_text(strip=True)
        title_list.append((index, title_list))
    return(title_list)


def extract_autor():
    autors = soup.find_all('ul', class_="meta__authors rlist--inline" )

    autor_list = []
    for index2, autor in enumerate(autors, 1):
        autor_text = autor.get_text(strip= True)
        autor_list.append((index2, autor_text))
    return(autor_list)

def extract_meta_dates():
    meta_dates = soup.find_all('div', class_="meta__details")
    md_list = []
    for i3, meta_date in enumerate(meta_dates, 1):
        this_soup = BeautifulSoup(str(meta_date), 'xml')
        journal = this_soup.find('a', class_="meta__serial")
        journal_text = journal.get_text(strip=True)
        date = this_soup.find('span', class_="meta__epubDate")
        date_text = date.get_text(strip=True)if date else "Not found"
        md_list.append((journal_text, date_text))
    return(md_list)

def extract_url():    
    # Alle Links finden
    links = soup.find_all('a', href=True)
    url_list=[]
    # Nur die URLs extrahieren
    urls = [link['href'] for link in links]
    for id4,elem in enumerate(urls,1):
        url_list.append((id4,elem))
    return(url_list)    
    
    

def extract_abstracts():
    
    # Alle Abstracts finden (Beispiel: wenn sie in einem <div> mit der Klasse 'abstract' sind)
    abstracts = soup.find_all('span', class_='hlFld-Abstract')
    # Text des Abstracts extrahieren
    abstract_texts = [abstract.get_text(strip=True) if abstract else 'no abstract' for abstract in abstracts]

    
    return(abstract_texts)


print(len(extract_url()))


