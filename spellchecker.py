import time

from multiDictionary import *

class SpellChecker:

    def __init__(self):
        self.multiDict = MultiDictionary()

    def handleSentence(self, txtIn, language):
        self.multiDict.add_dict(language)
        testo = replaceChars(txtIn)
        t0 = time.time()
        resoconto_contains = self.multiDict.searchWord(testo, language)
        t1 = time.time()
        tempo = t1 - t0
        risultato = printSearchWord("funzione_contains", tempo, resoconto_contains)+"\n"
        t0 = time.time()
        resoconto_lineare = self.multiDict.searchWordLinear(testo, language)
        t1 = time.time()
        tempo = t1-t0
        risultato += printSearchWord("ricerca lineare", tempo, resoconto_lineare)+"\n"


        return risultato



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~?"
    for c in chars:
        text = text.replace(c, "")
    return text

def printSearchWord(tipologia, tempo, lista_spellchecker):
    risultato = ""
    risultato += tipologia +"\n"
    risultato += str(tempo) +"\n"
    for parola in lista_spellchecker:
        if parola.corretta == False:
            if risultato != "":
                risultato += "\n"
            risultato += parola._parola
    return risultato
