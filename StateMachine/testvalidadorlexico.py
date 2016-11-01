import unittest
from ValidadorLexico import *

class Test_testvalidadorlexico(unittest.TestCase):

    def test_lexic_number_normal(self):
        args = '123456'
        isfinal, recognizedstr = lexic_number(args)
        self.assertTrue(isfinal)
        self.assertEqual(args, recognizedstr)
        
        args = '987654321'
        isfinal, recognizedstr = lexic_number(args)
        self.assertTrue(isfinal)
        self.assertEqual(args, recognizedstr)

        args = '123456789101112131415'
        isfinal, recognizedstr = lexic_number(args)
        self.assertTrue(isfinal)
        self.assertEqual(args, recognizedstr)

    def test_lexic_number_float(self):

        args = '123.456'
        isfinal, recognizedstr = lexic_number(args)
        self.assertTrue(isfinal)
        self.assertEqual(args, recognizedstr)

        args = '1.2345678910'
        isfinal, recognizedstr = lexic_number(args)
        self.assertTrue(isfinal)
        self.assertEqual(args, recognizedstr)

        args = '123456789.1'
        isfinal, recognizedstr = lexic_number(args)
        self.assertTrue(isfinal)
        self.assertEqual(args, recognizedstr)

    def test_lexic_number_error(self):
        pass


    def test_lexic_number_limits(self):
        args = '.'
        isfinal, recognizedstr = lexic_number(args)
        self.assertFalse(isfinal)
        args = '1'
        isfinal, recognizedstr = lexic_number(args)
        self.assertTrue(isfinal)
        self.assertEqual(args, recognizedstr)        
    
    def test_lexic_ident_normal(self):
        args = 'teste123'
        isfinal, recognizedstr = lexic_ident(args)
        self.assertTrue(isfinal)
        self.assertEqual(args, recognizedstr)     
        
        args = 'teste_123'
        isfinal, recognizedstr = lexic_ident(args)
        self.assertTrue(isfinal)
        self.assertEqual(args, recognizedstr)  


    def test_lexic_ident_error(self):
        pass    
    

    def test_lexic_ident_limits(self):
        args = 'a'
        isfinal, recognizedstr = lexic_ident(args)
        self.assertTrue(isfinal)
        self.assertEqual(args, recognizedstr)  

if __name__ == '__main__':
    unittest.main()
