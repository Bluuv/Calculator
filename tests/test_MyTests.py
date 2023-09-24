import unittest
import sys
import os
import src 
#import src.calculator
from src.calculator import addition, divison, multiplication, substraction, powerRaise, sqrtRoot

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(r"E:\\ROX\\_PROGRAMMING\\Projects\\Calculator\\src")



class MyTests(unittest.TestCase):
    def test_addition(self):
        res = addition(3, 5)
        self.assertEqual(res, 8)
        res = addition(-250.5, -10.2)
        self.assertEqual(res, -260.7)
    
    def test_substraction(self):
        res = substraction(10,6)
        self.assertEqual(res,4)
        res = substraction(6,9)
        self.assertEqual(res,-3)
        res = substraction(10.2,6.7)
        self.assertAlmostEqual(res,3.5)
    
    def test_multiplication(self):
        res = multiplication(10,6)
        self.assertEqual(res,60)
        res = multiplication(2.5,3)
        self.assertEqual(res,7.5)
        res = multiplication(10,-2.5)
        self.assertEqual(res,-25)

    def test_divison(self):
        res = divison(50,2)
        self.assertEqual(res,25)
        res = divison(7.5,-2.5)
        self.assertEqual(res,-3)
        res = divison(10,0)
        self.assertTrue(res,"Cannot divide by zero")

    def test_powerRaise(self):
        res = powerRaise(3,2)
        self.assertEqual(res,9)
        res = powerRaise(-6,2)
        self.assertEqual(res,36)
        res = powerRaise(2,-2)
        self.assertEqual(res,0.25)
        res = powerRaise(81,0.75)
        self.assertEqual(res,27)
    
    def test_sqrtRoot(self):
        res = sqrtRoot(81)
        self.assertEqual(res,9)
        res = sqrtRoot(-81)
        self.assertTrue(res,"Invalid Input")
        res = sqrtRoot(4.84)
        self.assertEqual(res,2.2)
   

if __name__ == '__main__':
    unittest.main()