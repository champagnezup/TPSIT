import random

# si utilizza la classe come se fosse una struttura
class Node():
    def __init__(self, key):
        self.key = key
        self.left = None  # discendente sinistro
        self.right = None  # discendente destro

    def insertNode(self, k):
           if self.key is not None:
                if k > self.key:
                    if self.right is None:
                        self.right = Node(k)
                    else:
                        self.right.insertNode(k)

                elif k < self.key:
                    if self.left is None:
                        self.left = Node(k)
                    else:
                        self.left.insertNode(k)
           else:
               # root
               self.key = k


    def printTree(self, level = 0): # livello da cui inzierà a stampare iniziera da 0
        if self.left is not None:
            self.left.printTree(level + 1)

        print(f"livello: {level} -> {self.key}")

        if self.right is not None:
            self.right.printTree(level + 1)

    def findNode(self, k):
        if k > self.key:
            if self.right is None:
                return "nodo non trovato"
            self.right.findNode(k)

        elif k < self.key:
            if self.left is None:
                return "nodo non trovato"
            self.left.findNode(k)

        else:
            return "nodo trovato"


    def height(self):
        if self.left is None:
            hL = 0
        else:
            hL = self.left.height()

        if self.right is None:
            hR = 0
        else:
            hR = self.right.height()

        if hL > hR:
            return hL + 1
        else:
            return hR + 1




def balancedeTree(nodes): # passo una lista di chiavi casuali
    lunghezzaLista = len(nodes)

    if lunghezzaLista == 0:
        return None

    pM = lunghezzaLista // 2 # divisione intera

    root = Node(nodes[pM])

    root.left = balancedeTree(nodes[:pM])
    root.right = balancedeTree(nodes[pM + 1:])

    return root

def main():
    pass

if __name__ == "__main__":
    main()