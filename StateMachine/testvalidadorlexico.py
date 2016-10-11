import unittest
from ValidadorLexico import *

class Test_testvalidadorlexico(unittest.TestCase):

    def test_lexicnumbernormal(self):
        args = '123456'
        self.assertTrue(lexinumber(args))

        args = '987654321'
        self.assertTrue(lexinumber(args))

        args = '123456789101112131415'
        self.assertTrue(lexinumber(args))

    def test_lexicnumberfloat(self):

        args = '123.456'
        self.assertTrue(lexinumber(args))
        args = '1.2345678910'
        self.assertTrue(lexinumber(args))
        args = '123456789.1'
        self.assertTrue(lexinumber(args))

    def test_lexicnumbererror(self):

        args = '.456'
        self.assertFalse(lexinumber(args))

        args = '12345678.'
        self.assertFalse(lexinumber(args))

        args = '123.456.789'
        self.assertFalse(lexinumber(args))

    def test_lexicnumberlimits(self):
        args = '.'
        self.assertFalse(lexinumber(args))
        args = '1'
        self.assertTrue(lexinumber(args))
        args = ''
        self.assertFalse(lexinumber(args))
        
    
    def test_lexicidentnormal(self):
        args = 'teste123'
        self.assertTrue(lexiident(args))
        
        args = 'teste_123'
        self.assertTrue(lexiident(args))

        args = 'teste_'
        self.assertTrue(lexiident(args))

        args = 'teste123_'
        self.assertTrue(lexiident(args))


    def test_lexicidenterror(self):
        
        args = '123'
        self.assertFalse(lexiident(args))

        args = 'teste space 123'
        self.assertFalse(lexiident(args))

        args = '*______*'
        self.assertFalse(lexiident(args))

    def test_lexicindentlimits(self):

        args = ''
        self.assertFalse(lexiident(args))

        args = '_'
        self.assertFalse(lexiident(args))

        args = '1'
        self.assertFalse(lexiident(args))

        args = 'a'
        self.assertTrue(lexiident(args))

if __name__ == '__main__':
    unittest.main()
