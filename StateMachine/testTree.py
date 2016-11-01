import unittest
from Tree import *

class Test_testTree(unittest.TestCase):
    def test_str_to_tree(self):
        arg = "teste=250+325;"
        arvore = str_expr_to_tree(arg)
        printTree(arvore)
        self.assertEqual(arvore.getNodeValue(), "=")
        self.assertEqual(arvore.getLeftChild().getNodeValue(), "teste")
        arvore = arvore.getRightChild()
        self.assertEqual(arvore.getNodeValue(), "+")
    
    def test_tree_to_list(self):
        arg = "teste=250+325;"
        arvore = str_expr_to_tree(arg)
        printTree(arvore)
        expected = [ "teste", "=", "250", "+", "325", ";"]
        found = tree_to_list(arvore)
        print(found)
        self.assertListEqual(expected, found)

if __name__ == '__main__':
    unittest.main()
