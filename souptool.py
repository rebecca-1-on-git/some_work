
import csv
import pandas as pd
import regex as re
from generateJournalList import *

class Journal():
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
    
    def getName(self):
        return self.name
    
    def getRating(self):
        return self.rating
    



class Publication():
    def __init__(self):
        self.title
        self.author
        self.date
        self.abstract
        self.journal
        self.rating 
       
    

    def extract_meta_dates():
        pass 

    def extract_url():    
        # Alle Links finden
        pass
        
        # Nur die URLs extrahieren
        
    def extract_title():
        pass

        

    def extract_abstracts():
        pass

        


class Searchresult():
    def __init__(self, publications: list):
        self.publications = []

    



   

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
    


class SoupBar():
    '''
        contains a soupbar with soup from the different years
    '''
    def __init__(self, url, years: list):

        self.soupbar = {}
        
        






    


# read in 
suchstrings = pd.read_excel('Resilienz_Paper.xlsx', sheet_name='Suchstrings')
ergebnisse = pd.read_excel('Resilienz_Paper.xlsx', sheet_name='Ergebnisse')

suchstrings.loc['Suchstring']=['jetzt aber wirklich','','','','','']
print(suchstrings.iloc[52,0])
with pd.ExcelWriter('example.xlsx', mode = 'w') as writer:
    suchstrings.to_excel(writer, sheet_name='Suchstrings', index=False)
    ergebnisse.to_excel(writer, sheet_name='Ergebnisse', index=False)