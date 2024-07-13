class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None

    def __str__(self):
        return str(self.value)


def getLeft(node1):
    return node1.left


def getRight(node):
    return node.right


def _maxValue(node):
    value = node.value
    while node.right is not None:
        value = node.right.value
        node = node.right
    return value


class BST:
    def __init__(self, root):
        self.root = Node(root)

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
            node.value = _maxValue(node.left)
            #A teraz usuwamy ten węzeł z którego wzięliśmy wartość
            node.left = self._delete_recursive(node.left, node.value)
        return node

    def clearTree(self):
        for node in self.postorder():
            self.delete(node)

