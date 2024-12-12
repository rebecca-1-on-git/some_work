import re

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