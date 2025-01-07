class Publication():
    def __init__(self, title = None, author = None, year = None, abstract = None, journal = None, rating = None):
        self.title = title
        self.author = author
        self.year = year
        self.abstract = abstract
        self.journal = journal
        self.rating = rating
    
    def getTitle(self):
        return self.title
    
    def getYear(self):
        return self.year
    
    def getRating(self):
        return self.rating
    
    def getJournal(self):
        return self.journal
    
    def getAuthor(self):
        return self.author