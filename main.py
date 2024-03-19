import spellchecker

sc = spellchecker.SpellChecker()

contatore_ita = 0
contatore_eng = 0
contatore_spa = 0

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        risultato = sc.handleSentence(txtIn,"Italian")
        print(risultato)
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        risultato = sc.handleSentence(txtIn,"English")
        print(risultato)
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        risultato = sc.handleSentence(txtIn,"Spanish")
        print(risultato)
        continue

    if int(txtIn) == 4:
        break


