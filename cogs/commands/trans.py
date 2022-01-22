import sys
import requests


def translate(word):

     syn_list = []
     try:
         res = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word)
         wtype = res.json()[0]['meanings'][0]['partOfSpeech']
         syn_list = res.json()[0]['meanings'][0]['definitions'][0]['synonyms']
         return wtype,syn_list
     #print(wt#ype)
     except KeyError as ke:
         print(ke)
     return None,None

