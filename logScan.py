
# This imports RegEx just in case we don't know the format of the document the user chooses

import re

''' 
Import Optional PrettyTable Library
to install from the windows command line or linux/mac terminal
pip install prettytable
'''
try:
    from prettytable import PrettyTable
    PRETTY = True
except:
    PRETTY = False

print(' ')
print(' ')


# This function takes in the file the user picked 

logFile = input("What file would you like to analyze today? ")

# This invokes the dictionary

keywordDictionary = {}

# This searcges the file and analyzes each line of the user selected log file

with open(logFile) as logFile:
    for eachRow in logFile:
        
# Seperates the file where spaces occurs in the user selected file
        
        logSplitList = eachRow.split( )
        for logEntry in logSplitList:
            if 'worm' in logEntry.lower():
                try:
                    value = keywordDictionary[logEntry]
                    value += 1
                    keywordDictionary[logEntry] = value
                except:
                    keywordDictionary[logEntry] = 1

print(' ')
print(' ')


# This creates a table based on the search results 
if PRETTY:

    t = PrettyTable(['Worm Names', 'Occurrences'])

    for logEntry in sorted(keywordDictionary, key=keywordDictionary.get, reverse=True):
        count = keywordDictionary[logEntry]
        t.add_row([logEntry, count])                      
    
    t.align = "l" 
    
    tabularResults = t.get_string()
    print(tabularResults)      
    
else:
    print("please install prettyTable")
    
print(' ')
print(' ')
print("Program Terminated Normally")
print("Log file search complete ")