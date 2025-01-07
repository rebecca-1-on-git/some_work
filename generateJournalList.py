import re
import pandas as pd
from journal import Journal

@staticmethod
def get_PERS():
    with open('../PERS.txt', 'r') as file:
        pers = {}
        for line in file: 
            pattern = re.search(r'(?P<journal>.*)((?:\s\d{4}-\d{4}\s)|(?:\s\d{4}-\d{3}X\s))(?P<rating>\S\+?)', line)
            if pattern:
                listEntry = []
                this_dict = pattern.groupdict()
                pers[this_dict['journal']] = this_dict['rating']
            else:
                print("No match found")
        return pers
    
@staticmethod
def get_ORGA():
    with open('../ORGA.txt', 'r') as file:
        orga={}
        for index,line in enumerate(file): 
            pattern = re.search(r'(?P<journal>.*)((?:\s\d{4}-\d{4}\s)|(?:\s\d{4}-\d{3}X\s))(?P<rating>\S\+?)', line)
            if pattern:
                this_dict = pattern.groupdict()
                orga[this_dict['journal']] = this_dict['rating']
            else:
                print("No match found " + line + str(index))
        return orga

@staticmethod
def writeFinalListToFile(orga, pers):
    final = orga
    for key_i, value_i in pers.items(): 
        if key_i not in orga.items():
            final[key_i] = value_i
    with open ('ORGA_plus_aditional_entries_from_pers.txt', 'w') as file:
        for key,value in final.items():
            file.write(key + '\t' + value + '\n')

@staticmethod
def getJournalListFromFile(filename :str):
    '''
        reads in a text file that contains a journal name and its rating separated with a \t for each line and returns a list of Journal Objects        
    '''
    journalList = []
    with open (filename,'r') as file:
        for l in file: 
            l = l.split('\t')
            l = [_.strip('\n') for _ in l]
            this_journal = Journal(l[0], l[1])
            journalList.append(this_journal)
    return journalList


@staticmethod
def writeResultsToFile(hitsInfo: list, results: list):
    
    # write to file ist noch nicht fertig
    suchstrings = pd.read_excel('example.xlsx', sheet_name='Suchstrings')
    ergebnisse = pd.read_excel('example.xlsx', sheet_name='Ergebnisse')
    for elem in hitsInfo:
        suchstrings.loc['Suchstring']=[elem.getSearchString()]
        suchstrings.loc['Suchmaschine']=[elem.getSearchEngine()]
        suchstrings.loc[]
    #for elem in results:
        #ergebnisse.loc['Titel']=[elem.getTitle(), elem.getAuthor(), elem.getYear(),'', elem.getJournal(), elem.getRating(),'']
    #with pd.ExcelWriter('example.xlsx', mode = 'w') as writer:
        #suchstrings.to_excel(writer, sheet_name='Suchstrings', index=False)
        #ergebnisse.to_excel(writer, sheet_name='Ergebnisse', index=False)

