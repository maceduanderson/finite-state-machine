from ValidadorLexico import *

class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())

def tree_to_list(tree):
    if tree is None:        
        return []
    return tree_to_list(tree.getLeftChild()) + [tree.getNodeValue()] + tree_to_list(tree.getRightChild())

def str_expr_to_tree(expr):

    marcador = 0
    root  = None
    for x in range(0, len(expr)):
        
        if is_atrib_operator(expr[x]):
            root = BinaryTree(expr[x])
            arvore = root
            arvore.insertLeft(expr[marcador:x])
            marcador = x + 1
                
        if is_arithmetic_operator(expr[x]):
            arvore.insertRight(expr[x])
            arvore = arvore.getRightChild()
            arvore.insertLeft(expr[marcador:x])
            marcador = x + 1
        if is_pv(expr[x]):
            arvore.insertRight(expr[x])                
    arvore.insertRight(expr[marcador:x])
    return root
