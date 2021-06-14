# The purpose of this script is to search for words or strings in a txt document
# The text document should be in the same folder that this script resides
#
# This script will prompt the user for a file to process.
# It will open the file and iterate through each line of the file, catch and report any errors that occur.
# For each line in the file:
# If the line identifies a specific worm that was detected, then record the unique name of the worm.
# Keep track of the number of occurrences of each unique worm.
# Once all the lines have been processed produce a prettytable result that includes the name of each unique worm and number of occurrences that were identified.
# The prettytable will format the results by highest occurring worms
#
#
# Note: the best way I found for this to work is by:
# First, downloading Python in Ubuntu https://phoenixnap.com/kb/how-to-install-python-3-ubuntu
# Second, downloading and installing Wing IDE in Ubuntu https://wingware.com/doc/install/linux-installation-detail
# Third, install PIP on Ubuntu https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/
# Fourth, downloading and installing PrettyTables in Ubuntu https://pypi.org/project/prettytable/
#
#
# This script is an amalgamation of scripts found all around

# This imports RegEx just in case we don't know the format of the document the user chooses

import re

# This imports PrettyTable, it should be installed locally
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


# This function ask the user to type in the file of their choice

logFile = input("What file would you like to analyze today? ")

# This invokes the dictionary

keywordDictionary = {}

# This searches the file and analyzes each line of the user selected log file

with open(logFile) as logFile:
    for eachRow in logFile:
        
# Seperates the file where spaces occurs in the user selected file
# Substitute the word 'worm' for any other word you chose to search for
        
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
# You can change the table headers 'Worm Names' 'Occurences' to anythoing you want
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
