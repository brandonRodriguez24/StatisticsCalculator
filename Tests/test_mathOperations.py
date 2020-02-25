import unittest
from mathOperations.addition import Addition
from mathOperations.subtraction import Subtraction
from mathOperations.multiplication import Multiplication
from mathOperations.division import Division
from mathOperations.exponent import Exponent
from mathOperations.logarithm import Logarithm
from mathOperations.sqrRoot import SquareRoot


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))

    def test_MathOperations_multiplication(self):
        self.assertEqual(4, Multiplication.product(2, 2))

    def test_MathOperations_division(self):
        self.assertEqual(2, Division.quotient(10, 5))

    def test_MathOperations_exponent(self):
        self.assertEqual(16.0, Exponent.power(4, 2))

    def test_MathOperations_logarithm(self):
        self.assertEqual(0.0, Logarithm.logarithm(1, 2))

    def test_MathOperations_sqrRoot(self):
        self.assertEqual(3, SquareRoot.root(9))


if __name__ == '__main__':
    unittest.main()