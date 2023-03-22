# utiliziamo questa classe come se fosse una struttura
class Node():
    def __init__(self, key):
        self.key = key
        self.left = None # discendente sinistro
        self.right = None # discendente destro

def insertNode(root, key):

    if key > root.key:
        if root.right is None:
            root.right = Node(key)
        else:
            insertNode(root.right, key)
    elif key < root.key:
        if root.left is None:
            root.left = Node(key)
        else:
            insertNode(root.left, key)

    # il caso con l'uguale non può esistere

def printTree(root):
    if root.left:
        printTree(root.left)
    print(root.key),
    if root.right:
        printTree(root.right)


def main():

    root = Node(45) # istanzio un nodo
    insertNode(root, 56)
    insertNode(root, 40)
    insertNode(root, 12)
    insertNode(root, 57)
    insertNode(root, 1)

    printTree(root)

if __name__ == "__main__":
    main()