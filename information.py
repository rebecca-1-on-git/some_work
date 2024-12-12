

class SearchStringEntry():
    def __init__(self, numResults = 0, journal = None, hitsNoMismatch = None):
        self.searchString = 'TITLE = ("resilience") AND ABSTRACT = ("company" OR "business" OR "firm" OR "enterprise" OR "corporation" OR "venture")'
        self.searchEngine = 'Universitätsbibliothek Stuttgart Katalog plus'
        self.numResults = numResults
        self.journal = journal
        self.hitsNoMismatch = hitsNoMismatch
        
    def getSearchString(self):
        return self.searchString
    
    def getSearchEngine(self):
        return self.searchEngine
    
    def getNumResults(self):
        return self.numResults
    
    def getJournal(self):
        return self.journal
    
    def getHitsNoMismatch(self):
        return self.hitsNoMismatch