

import unittest

from . import lib 

class TestLib(unittest.TestCase):
    
    def test_add_integer(self):
        #AAA -Arrange,Act, ASSERT
        a = 59
        b = 80
        #Act -faire l action

        resultat = lib.add(a, b)

        self.assertEqual(resultat,139)
        


        # a=59,b= 80

        #139
    def test_add_float(self):
        resultat = lib.add(1.5 ,2.7)
        self.assertEqual(resultat,4.2)
  
    def test_div_integer(self):
        resultat = lib.div(6, 3)
        self.assertEqual(resultat, 2)
        
    def test_div_by_zero_raises_exception(self):
    
        self.assertRaises(ZeroDivisionError, lambda : lib.div(8, 0))
        
        
        