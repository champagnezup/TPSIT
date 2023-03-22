def readFile(nameFile):
    startList = []

    with open(nameFile) as f:
        [startList.append(line[:-1]) for line in f.readlines()]

    f.close()

    return startList

def assegnaIdentificativoCelle(lista):
    listaIdentificativo = []
    cont = 0
    s = ""

    for i in lista:
        for j in i:
            if j != '1':
                s += str(cont)
                cont += 1
            else:
                s+= 'X'
        
        listaIdentificativo.append(s)
        s = ""

    # SB: print(listaIdentificativo)
    return listaIdentificativo



def main():
    # salvataggio della nostra matrice in una lista
    startList = readFile("mappa.csv")
    print(startList)

    listaIdentificativo = assegnaIdentificativoCelle(startList)
    print(listaIdentificativo)

    lunghezzaLista = len(listaIdentificativo[1])
    altezzaLista = len(listaIdentificativo)


if __name__ == "__main__":
    main()