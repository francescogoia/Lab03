from dictionary import *
from richWord import *
import dataclasses

class MultiDictionary:

    def __init__(self):
       self.dizionari = {}       ## dizionario di oggetti Dictionary

    def add_dict(self, language):
        d = Dictionary()
        path = "resources/" + language + ".txt"
        d.loadDictionary(path)
        self.dizionari[language] = d


    def printDic(self, language):
        dizionario = self.dizionari[language]
        return dizionario.printAll()

    def searchWord(self, words, language):
        dizionario = self.dizionari[language]
        ## words è la lista di parole da controllare
        lista_reach_words = []
        for word in words.split():
            if self.dizionari[language]._dict.__contains__(word.lower()):
                rw = RichWord(word)
                rw.corretta = True
                lista_reach_words.append(rw)
            else:
                rw = RichWord(word)
                lista_reach_words.append(rw)
        return lista_reach_words

    def searchWordLinear(self, words, language):
        dizionario = self.dizionari[language]
        ## words è la lista di parole da controllare
        lista_reach_words = []
        for word in words.split():
            trovata = False
            for parola in dizionario._dict:
                if word.lower() == parola.lower():
                    rw = RichWord(word)
                    rw.corretta = True
                    lista_reach_words.append(rw)
                    trovata = True
                    break
                if trovata == False:
                    rw = RichWord(word)
                    lista_reach_words.append(rw)
        return lista_reach_words

def test():
    md = MultiDictionary()
    md.add_dict("Italian")
    md.printDic("Italian")

if __name__ == "__main__":
    test()


"""
è la classe che gestisce il programma, dictionary contiene il dizionario in una sola lingua,
richWord verifica se una parola è corretta o meno,
spellChecker riceve l'input e chiama multidictionary sulle parole

"""