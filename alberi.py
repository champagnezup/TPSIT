import random

# utiliziamo questa classe come se fosse una struttura
class Node():
    def __init__(self, key):
        self.key = key
        self.left = None # discendente sinistro
        self.right = None # discendente destro

    def insertNode(self, key):
        if self.key is not None:
            if key > self.key:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insertNode(key)

            elif key < self.key:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insertNode(key)

        else:
            self.key = key

    def printTree(self, level = 0): # il livello sara inizializzato a 0
        if self.left is not None:
            self.left.printTree(level + 1)

        print(f"Livello: {level} -> {self.key}")

        if self.right is not None:
            self.right.printTree(level + 1)

    # algoritmo di ricerca di una key in un albero
    def findNode(self, key):
        if key > self.key:
            # andiamo a destra
            if self.right == None:
                return f"nodo {key} non trovato"
            return self.right.findNode(key)

        elif key < self.key:
            #andiamo a sinistra
            if self.left == None:
                return f"nodo {key} non trovato"
            return self.left.findNode(key)

        else:
            return f"nodo {key} trovato"

    # metodo che calcola l'altezza del nostro albero
    def height(self):

        if self.left is None:
            hLeft = 0
        else:
            hLeft = self.left.height()

        if self.right is None:
            hRight = 0
        else:
            hRight = self.left.height()

        if hLeft > hRight:
            return hLeft + 1 # il + 1 si riferisce al nodo su cui ci troviamo
        else:
            return hRight + 1


#funzione data una lista di numeri qualunque inserisce questa lista di chiavi in un albero sicuramete bilanciato
def balancedTree(nodes):
    # nodes deve contenre valori ordinati CRESCENTI

    lunghezzaLista = len(nodes) # luneghezza della lista

    if lunghezzaLista == 0:#se la lunghezza e' 0 significa che la lista e' vuota
        return None


    # il nodes che utilizzero da qua in poi sarà diverso cioè ordinato
    puntoMedio = lunghezzaLista // 2 # // divisione intera
    print(f"nodo di mezzo: {puntoMedio}")
    root = Node(nodes[puntoMedio])#creare al root un nodo con la key punto medio

    root.left = balancedTree(nodes[:puntoMedio])
    root.right = balancedTree(nodes[puntoMedio + 1:])

    return root

def main():
    listKey = list(range(0, 40, 5)) # da 0 a 40 saltanto di 5
    random.shuffle(listKey)

    listKey.sort() #ordina la lista 
    root = balancedTree(listKey)
    root.printTree()
    print(f"altezza albero: {root.height() - 1}") # perche conta anche il root

    # in python tutto e una classe
    root.altezza = 5
    print(root.altezza)


if __name__ == "__main__":
    main()