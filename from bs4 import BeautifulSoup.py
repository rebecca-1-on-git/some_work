from bs4 import BeautifulSoup
import csv
import pandas as pd
import regex as re
with open ("AoM201_206.html", encoding='utf-8')as file: 
    soup = BeautifulSoup(file, 'xml')   

def extract_title():
    titles = soup.find_all('h4', class_="meta__title meta__title__margin")
    title_list = []
    # Extract and return the titles
    for title in titles:
        title_text = title.get_text()
        title_list.append(str(title_text))
    return title_list


def extract_autor():
    autors = soup.find_all('ul', class_="meta__authors rlist--inline" )

    autor_list = []
    for autor in autors:
        autor_text = autor.get_text()
        autor_list.append(autor_text)
    return autor_list

def extract_meta_dates():
    meta_dates = soup.find_all('div', class_="meta__details")
    md_list = []
    for meta_date in meta_dates:
        this_soup = BeautifulSoup(str(meta_date), 'xml')
        journal = this_soup.find('a', class_="meta__serial")
        journal_text = journal.get_text(strip=True)if journal else "Not found"
        date = this_soup.find('span', class_="meta__epubDate")
        date_text = date.get_text(strip=True)if date else "Not found"
        md_list.append((journal_text, date_text))
    return md_list 

def extract_url():    
    # Alle Links finden
    links = soup.find_all('a', href=True)
    
    # Nur die URLs extrahieren
    urls = [link['href'] for link in links]
    p = re.compile('/doi/')
    url_text = ["https://journals.aom.org" + elem for elem in urls if p.match(elem)]

    return url_text   
    
    

def extract_abstracts():
    
    # Alle Abstracts finden (Beispiel: wenn sie in einem <div> mit der Klasse 'abstract' sind)
    abstracts = soup.findAll('span', class_='hlFld-Abstract')
    # Text des Abstracts extrahieren
 
    abstract_texts = [abstract.text for abstract in abstracts]
    
    return abstract_texts



def export_to_csv(filename='output.csv'):
    # Extract data from the functions
    titles = extract_title()
    authors = extract_autor()
    meta_dates = extract_meta_dates()
    urls = extract_url()
    abstracts = extract_abstracts()

    # Determine the maximum number of rows
    max_rows = max(len(titles), len(authors), len(meta_dates), len(urls), len(abstracts))

    # Prepare rows for CSV
    rows = []
    for i in range(max_rows):
        
        title = titles[i] if i < len(titles) else ''
        author = authors[i] if i < len(authors) else ''
        journal = meta_dates[i][0] if i < len(meta_dates) else ''  # Journal
        date = meta_dates[i][1] if i < len(meta_dates) else ''  # Date
        url = urls[i] if i < len(urls) else ''
        abstract = abstracts[i] if i < len(abstracts) else ''
        
        
        rows.append([title, author, journal, date, url, abstract])
             

    # Write to CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, dialect="excel")
        # Write the header row
        writer.writerow(['Title', 'Authors', 'Journal', 'Publication Date', 'URL', 'Abstract'])
        # Write the data rows
        writer.writerows(rows)
    
    df= pd.read_csv(filename)
    df.to_excel('table1.xlsx', index=False)

    print(f"Data exported to {filename}")

# Call the export function to create the CSV
export_to_csv("table.csv")

