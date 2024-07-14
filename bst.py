class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    @staticmethod
    def getRight(node):
        return node.right

    @staticmethod
    def getLeft(node):
        return node.left

    @staticmethod
    def _maxValue(node):
        value = node.value
        while node.right is not None:
            value = node.right.value
            node = node.right
        return value

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(value, self.root)

    def insert_recursive(self, value, node):
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recursive(value, node.right)
        else:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_recursive(value, node.left)

    def search(self, value):
        return self._search_recursive(value, self.root)

    def _search_recursive(self, value, node):
        if node is None or node.value == value:
            return node
        if value > node.value:
            return self._search_recursive(value, node.right)
        else:
            return self._search_recursive(value, node.left)

    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node is not None:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def min(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return node

    def max(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node

    def delete(self, value):
        self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        #Jeśli większy od node to szukamy po prawej
        if value > node.value:
            node.right = self._delete_recursive(node.right, value)
        #Jeśli mniejszy od node to szukamy po lewej
        elif value < node.value:
            node.left = self._delete_recursive(node.left, value)
        #Wartość znaleziona
        else:
            #Jeśli jedno dziecko lub zero dzieci
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            #Jeśli ma dwójke dzieci to szukamy inorder successor
            #Inorder successor to węzeł minimalny gdy zaczniemy poszukiwania od node.right
            node.value = self._maxValue(node.left)
            #A teraz usuwamy ten węzeł z którego wzięliśmy wartość
            node.left = self._delete_recursive(node.left, node.value)
        return node

    def clearTree(self):
        for node in self.postorder():
            self.delete(node)
        self.root = None

    def noTree(self):
        if self.root is None:
            return True


class Menu:

    def __init__(self):
        self.tree = BST()

    def presetTree(self):
        nodes = [5, 3, 4, 1, 8, 7]
        for node in nodes:
            self.tree.insert(node)

    def mainRoot(self):
        print("A - wstaw element do drzewa BST")
        print("B - usuń element z drzewa BST")
        print("C - wyczyść drzewo")
        print("D - wydrukuj drzewo przejściem preorder")
        print("E - wydrukuj drzewo przejściem inorder")
        print("F - wydrukuj drzewo przejściem postorder")
        if self.tree.noTree():
            print("G - stwórz drzewo przykładowe")
        print("X - zakończ działanie programu")
        choice = str(input())
        if choice == "A" or choice == "a":
            value = int(input("Podaj wartość węzła do dodania:\n"))
            self.tree.insert(value)
            print(f"Wstawiono element {value} do drzewa")
        elif choice == "B" or choice == "b":
            value = int(input("podaj wartość węzła do usunięcia:\n"))
            self.tree.delete(value)
            print(f"Usunięto element {value} z drzewa")
        elif choice == "C" or choice == "c":
            self.tree.clearTree()
        elif choice == "D" or choice == "d":
            print("Przejście po drzewie w kolejności preorder", self.tree.preorder())
        elif choice == "E" or choice == "e":
            print("Przejście po drzewie w kolejności inorder", self.tree.inorder())
        elif choice == "F" or choice == "f":
            print("Przejście po drzewie w kolejności postorder", self.tree.postorder())
        elif choice == "X" or choice == "x":
            #jakoś zrób wyłączanie programu idk, zrób żeby while(menu) sie wyjebało
            return
        if self.tree.noTree():
            if choice == "G" or choice == "g":
                self.presetTree()
