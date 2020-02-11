import unittest
from Calculator.calculator218 import Calculator

class TestCalculator218(unittest.TestCase):

    def test_addition(self):
        result= Calculator.addition(10,5)
        self.assertEqual(result, 15)

    def test_subtraction(self):
        result=Calculator.subtraction(20,10)
        self.assertEqual(result,10)

    def test_multiplication(self):
        result=Calculator.multiplication(2,8)
        self.assertEqual(result,16)

    def test_division(self):
        result=Calculator.division(20,10)
        self.assertEqual(result,2)

    def test_squared(self):
        result=Calculator.squared(10)
        self.assertEqual(result,100)

    def test_squareRoot(self):
        result=Calculator.squareRoot(9)
        self.assertEqual(result,3)

if __name__=='__main__':
    unittest.main()


