
import csv

import regex as re
from generateJournalList import *


import requests
from bs4 import BeautifulSoup
from generateJournalList import getJournalListFromFile
from publications import Publication
from information import SearchStringEntry



@staticmethod        
def getHitsInfo(soup):
    hits_info = soup.find("div", class_="col-xs-7 rdsSearchInfo")
    if hits_info:
        total_hits_text = hits_info.get_text(strip=True)
        total_hits = int(total_hits_text.split("von")[-1].strip())
        return total_hits
    else:
        return None

@staticmethod
def scraping(journalList: list, years = [2019, 2020, 2021, 2022, 2023, 2024]):
    '''
        Returns two list hitsInfo, results. hitsInfo is a list of SearchStringEntry Objects and results is a list of publication objects
    '''
    results = []
    hitsInfo = []
    for elem in journalList: 
        numResultAllYears = 0
        count = 0
        for year in years:
            journal = elem.getName()
            URL = "https://rds-stg.ibs-bw.de/opac/RDSProxy/Search?join=AND&bool0%5B%5D=AND&lookfor0%5B%5D=resilience&lookfor0%5B%5D="+str(year)+"&lookfor0%5B%5D="+journal+"&lookfor0%5B%5D=%22company%22+OR+%22business%22+OR+%22firm%22+OR+%22enterprise%22+OR+%22corporation%22+OR+%22venture%22&type0%5B%5D=ti&type0%5B%5D=py&type0%5B%5D=so&type0%5B%5D=ab&filter%5B%5D=ftav%3A%221%22&dfApplied=1&limit=50"
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            numResults = getHitsInfo(soup)
            numResultAllYears += numResults or 0
            media_entries = soup.find_all('div', class_='media')
            for media in media_entries:
                # Titel extrahieren
                title_tag = media.find('a', class_='title getFull')
                title = title_tag.get_text(strip=True) if title_tag else "Titel nicht gefunden"
                # Autoren und Journal-Details aus der "short-view"-Sektion extrahieren
                short_view_div = media.find('div', class_='short-view')
                # HTML in der short-view-Sektion analysieren
                if short_view_div:
                    details_div = short_view_div.find_all('div')[1]  # Der letzte <div> enthält Autoren & 
                    details_div = details_div.get_text(separator="\n", strip=True) if details_div else ""
                    detail_list = details_div.split('\n')
                    author = detail_list[0]
                    journalResult = detail_list[1]
                    
                    if re.match(journal, journalResult):
                        count +=1 
                        results.append(Publication(title = title, year = year, journal = journalResult, author = author, rating = elem.getRating()))
                        
        hitsInfo.append(SearchStringEntry(numResults = numResultAllYears, journal = journal, hitsNoMismatch=count))
    return hitsInfo, results

class LiteraturRecherche():
    @ staticmethod
    def readInAtt(filepath):
        '''
            reads in the journals that has to be searched from a text file
            return: list of Journal instances
            
        '''
        with open(filepath, 'r', encoding="utf-8") as f:
            for l in f: 
                pass
    



        
        






