import requests
import json
import getRandomWord
from getRandomWord import printRandomWord
r = requests.get('https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_alpha_arrays.json')
EnglishDictionaryJson=json.loads(r.text)

r = requests.get('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt')
topTenThousandWords = r.text.split()

for n in topTenThousandWords:
    if n in EnglishDictionaryJson[ord(n[0].lower())-97]:
        EnglishDictionaryJson[ord(n[0].lower())-97].pop(n)

totalSize=0
for x in EnglishDictionaryJson:
    totalSize+=len(x)


print(printRandomWord(EnglishDictionaryJson))