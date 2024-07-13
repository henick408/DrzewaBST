from bst import *


tree = BST(5)

tree.insert(3)
tree.insert(4)
tree.insert(1)
tree.insert(8)
tree.insert(7)


print(tree.preorder())
print(tree.inorder())
print(tree.postorder())

tree.clearTree()

print(tree.preorder())
print(tree.inorder())
print(tree.postorder())

