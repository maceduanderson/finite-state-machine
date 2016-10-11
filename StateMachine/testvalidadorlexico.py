import unittest
from ValidadorLexico import *

class Test_testvalidadorlexico(unittest.TestCase):

    def test_lexic_number_normal(self):
        args = '123456'
        self.assertTrue(lexic_number(args))

        args = '987654321'
        self.assertTrue(lexic_number(args))

        args = '123456789101112131415'
        self.assertTrue(lexic_number(args))

    def test_lexic_number_float(self):

        args = '123.456'
        self.assertTrue(lexic_number(args))
        args = '1.2345678910'
        self.assertTrue(lexic_number(args))
        args = '123456789.1'
        self.assertTrue(lexic_number(args))

    def test_lexic_number_error(self):

        args = '.456'
        self.assertFalse(lexic_number(args))

        args = '12345678.'
        self.assertFalse(lexic_number(args))

        args = '123.456.789'
        self.assertFalse(lexic_number(args))

    def test_lexic_number_limits(self):
        args = '.'
        self.assertFalse(lexic_number(args))
        args = '1'
        self.assertTrue(lexic_number(args))
        args = ''
        self.assertFalse(lexic_number(args))
        
    
    def test_lexic_ident_normal(self):
        args = 'teste123'
        self.assertTrue(lexic_ident(args))
        
        args = 'teste_123'
        self.assertTrue(lexic_ident(args))

        args = 'teste_'
        self.assertTrue(lexic_ident(args))

        args = 'teste123_'
        self.assertTrue(lexic_ident(args))


    def test_lexic_ident_error(self):
        
        args = '123'
        self.assertFalse(lexic_ident(args))

        args = 'teste space 123'
        self.assertFalse(lexic_ident(args))

        args = '*______*'
        self.assertFalse(lexic_ident(args))

    def test_lexic_ident_limits(self):

        args = ''
        self.assertFalse(lexic_ident(args))

        args = '_'
        self.assertFalse(lexic_ident(args))

        args = '1'
        self.assertFalse(lexic_ident(args))

        args = 'a'
        self.assertTrue(lexic_ident(args))

if __name__ == '__main__':
    unittest.main()
