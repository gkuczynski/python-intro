"""Testy dla modułu math_tools."""

import unittest
from my_awesome_lib.math_tools import Calculator, fibonacci, prime_checker


class TestCalculator(unittest.TestCase):
    """Testy dla klasy Calculator."""
    
    def setUp(self):
        """Przygotowanie kalkulatora testowego."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test dodawania."""
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)
        self.assertIn("5 + 3 = 8", self.calc.get_history())
    
    def test_multiply(self):
        """Test mnożenia."""
        result = self.calc.multiply(4, 6)
        self.assertEqual(result, 24)
        self.assertIn("4 * 6 = 24", self.calc.get_history())
    
    def test_power(self):
        """Test potęgowania."""
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)
        self.assertIn("2 ^ 3 = 8", self.calc.get_history())
    
    def test_history(self):
        """Test historii operacji."""
        self.calc.add(1, 2)
        self.calc.multiply(3, 4)
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)


class TestFibonacci(unittest.TestCase):
    """Testy dla funkcji fibonacci."""
    
    def test_fibonacci_zero(self):
        """Test ciągu Fibonacciego dla n=0."""
        result = fibonacci(0)
        self.assertEqual(result, [])
    
    def test_fibonacci_one(self):
        """Test ciągu Fibonacciego dla n=1."""
        result = fibonacci(1)
        self.assertEqual(result, [0])
    
    def test_fibonacci_five(self):
        """Test ciągu Fibonacciego dla n=5."""
        result = fibonacci(5)
        expected = [0, 1, 1, 2, 3]
        self.assertEqual(result, expected)
    
    def test_fibonacci_negative(self):
        """Test błędu dla ujemnego n."""
        with self.assertRaises(ValueError):
            fibonacci(-1)


class TestPrimeChecker(unittest.TestCase):
    """Testy dla funkcji prime_checker."""
    
    def test_prime_checker_prime_numbers(self):
        """Test liczb pierwszych."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        for prime in primes:
            self.assertTrue(prime_checker(prime))
    
    def test_prime_checker_composite_numbers(self):
        """Test liczb złożonych."""
        composites = [4, 6, 8, 9, 10, 12, 14, 15]
        for composite in composites:
            self.assertFalse(prime_checker(composite))
    
    def test_prime_checker_invalid_input(self):
        """Test błędu dla nieprawidłowych danych."""
        with self.assertRaises(ValueError):
            prime_checker(1)
        with self.assertRaises(ValueError):
            prime_checker(0)


if __name__ == '__main__':
    unittest.main()
