import random

def printRandomWord(alphabeticallySortedDictionary):
    randomLetterIndex=alphabeticallySortedDictionary[round(random.uniform(0, 1)*25)]
    indexLetterList = list(randomLetterIndex.keys())
    randomWord=indexLetterList[round(random.uniform(0,1)*len(indexLetterList))]
    return randomWord
    
