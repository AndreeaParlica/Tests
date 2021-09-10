#!/usr/bin/env python3
# important: Pasi pentru a executa fisierul cu succes:
    # 1. create env
    # 2. install pytest in the env
    # 3. run in terminal python -m pytest teste - pentru a executa pytest ca modul, adauga current directory to sys.path
# ca python sa-l gaseasca cand importa modulul Assignment

import unittest
from Assignment import CalculatorAssing


class TestCalculatorAssign(unittest.TestCase):

    def test_division_by_zero(self):
        """Makes sure ZeroDivisionError is raised when necessary"""
        self.calc = CalculatorAssing()
        self.assertRaises(ZeroDivisionError, self.calc.divisionNumbers, 10, 0)

    def test_add(self):
        """Test case function for addition"""
        self.calc = CalculatorAssing()
        result = self.calc.addNumbers(10, 8)
        expected = 18
        self.assertEqual(result, expected)

    def test_sub(self):
        """Test case function for subtraction"""
        self.calc = CalculatorAssing()
        result = self.calc.substractionNumebers(10, 8)
        expected = 2
        self.assertEqual(result, expected)

    def test_mul(self):
        """Test case function for multiplication"""
        self.calc = CalculatorAssing()
        result = self.calc.multiplicationNumbers(10, 8)
        expected = 80
        self.assertEqual(result, expected)

    def test_div(self):
        """Test case function for division"""
        self.calc = CalculatorAssing()
        result = self.calc.divisionNumbers(10, 8)
        expected = 1.25
        self.assertEqual(result, expected)

    def test_isString(self):
        """Test case function for string value"""
        self.calc = CalculatorAssing()
        self.assertRaises(TypeError, self.calc.divisionNumbers, 10, "x")


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestCalculatorAssign))
    return test_suite


mySuite = suite()

runner = unittest.TextTestRunner()
runner.run(mySuite)
