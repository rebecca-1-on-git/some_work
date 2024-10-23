from bs4 import BeautifulSoup
with open ("html_doc3.html", encoding='utf-8')as file: 
    soup = BeautifulSoup(file, 'xml')   

titles = soup.find_all('h4', class_="meta__title meta__title__margin")

# Extract and print the titles
for index, title in enumerate(titles, 1):
    title_text = title.get_text(strip=True)
    print(f"{index}. {title_text}")


