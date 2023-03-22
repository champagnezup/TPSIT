# TUTTO IN PYTHON E UN OGGETTO
def somma(a, b):
    return a + b

def main():
    x = somma(3, 5) # somma() chiamata alla funzione
    print(f"somma: {x}")

    print(somma) # ci stampa a video cosa e somma
    print()

    somma.descrizione = "La funzione calcola la somma"
    print(f"{somma.descrizione} \n{x}")

if __name__ == "__main__":
    main()