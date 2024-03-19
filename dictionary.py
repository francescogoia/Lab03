class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        file_diz = open(path, "r", encoding="utf-8")
        for righe in file_diz:
            parola = righe.strip()
            self._dict.append(parola)
        file_diz.close()

    def printAll(self):
        risultato = ""
        for parola in self._dict:
            if risultato != "":
                risultato += "\n"
            risultato += parola
        return risultato

    def __repr__(self):
        risultato = ""
        for parola in self._dict:
            if risultato != "":
                risultato += "\n"
            risultato += parola
        return risultato

    @property
    def dict(self):
        return self._dict

def test():
    d = Dictionary()
    d.loadDictionary("resources/Italian.txt")
    print(d.printAll())

if __name__ == "__main__" :
    test()