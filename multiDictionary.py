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

    def searchWordDicotomic(self, words, language):
        dizionario = self.dizionari[language]
        ## words è la lista di parole da controllare
        lista_reach_words = []
        for word in words.split():
            indice_trovata = ricerca_Dicotomica(dizionario._dict, word)
            if indice_trovata != -1:
                rw = RichWord(word)
                rw.corretta = True
                lista_reach_words.append(rw)
            else:
                rw = RichWord(word)
                lista_reach_words.append(rw)
        return lista_reach_words

def ricerca_Dicotomica(lista, target):
    """
    restituisce l'indice dell'elemento cercato
    :param lista:
    :param low: indice iniziale
    :param high:indice di arrivo (per la prima iterazione len(lista) -1
    :param target:oggetto da cercare
    :return:indice dell'elemento
    """
    low = 0
    high = len(lista) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if lista[mid] == target:
            return mid
        elif lista[mid] < target:
            low = mid + 1

        else:
            high = mid - 1
    return -1

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