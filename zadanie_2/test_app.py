import unittest
from unittest.mock import patch
from app import (
    validate_email, 
    calculate_circle_area, 
    filter_even_numbers, 
    convert_date_format, 
    is_palindrome
)
import math

class TestApp(unittest.TestCase):
    
    def setUp(self):
        """Przygotowanie środowiska testowego przed każdym testem."""
        self.valid_emails = [
            "test@example.com",
            "user.name@domain.co.uk",
            "test123@test-domain.org"
        ]
        self.invalid_emails = [
            "invalid-email",
            "@domain.com",
            "test@",
            "test.domain.com"
        ]
        
    def test_validate_email_valid_cases(self):
        """Test poprawnych adresów e-mail."""
        for email in self.valid_emails:
            with self.subTest(email=email):
                self.assertTrue(validate_email(email))
    
    def test_validate_email_invalid_cases(self):
        """Test niepoprawnych adresów e-mail."""
        for email in self.invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(validate_email(email))
    
    def test_validate_email_edge_cases(self):
        """Test przypadków brzegowych dla walidacji e-mail."""
        self.assertFalse(validate_email(""))
        self.assertFalse(validate_email(" "))
        
    def test_validate_email_type_error(self):
        """Test błędu typu dla walidacji e-mail."""
        with self.assertRaises(TypeError):
            validate_email(123)
        with self.assertRaises(TypeError):
            validate_email(None)
    
    def test_calculate_circle_area_positive_radius(self):
        """Test obliczania pola koła dla dodatnich promieni."""
        self.assertAlmostEqual(calculate_circle_area(1), math.pi, places=5)
        self.assertAlmostEqual(calculate_circle_area(2), 4 * math.pi, places=5)
        self.assertAlmostEqual(calculate_circle_area(0.5), 0.25 * math.pi, places=5)
    
    def test_calculate_circle_area_zero_radius(self):
        """Test obliczania pola koła dla promienia zero."""
        self.assertEqual(calculate_circle_area(0), 0)
    
    def test_calculate_circle_area_negative_radius(self):
        """Test błędu dla ujemnego promienia."""
        with self.assertRaises(ValueError):
            calculate_circle_area(-1)
        with self.assertRaises(ValueError):
            calculate_circle_area(-0.5)
    
    def test_calculate_circle_area_type_error(self):
        """Test błędu typu dla obliczania pola koła."""
        with self.assertRaises(TypeError):
            calculate_circle_area("2")
        with self.assertRaises(TypeError):
            calculate_circle_area(None)
    
    def test_filter_even_numbers_mixed_list(self):
        """Test filtrowania listy z liczbami parzystymi i nieparzystymi."""
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])
        self.assertEqual(filter_even_numbers([2, 4, 6]), [2, 4, 6])
    
    def test_filter_even_numbers_empty_list(self):
        """Test filtrowania pustej listy."""
        self.assertEqual(filter_even_numbers([]), [])
    
    def test_filter_even_numbers_float_numbers(self):
        """Test filtrowania listy z liczbami zmiennoprzecinkowymi."""
        self.assertEqual(filter_even_numbers([1.0, 2.0, 3.0, 4.0]), [2.0, 4.0])
    
    def test_filter_even_numbers_type_error(self):
        """Test błędu typu dla filtrowania liczb."""
        with self.assertRaises(TypeError):
            filter_even_numbers("not a list")
        with self.assertRaises(TypeError):
            filter_even_numbers([1, 2, "3", 4])
    
    def test_convert_date_format_default_formats(self):
        """Test konwersji daty z domyślnymi formatami."""
        result = convert_date_format("2023-12-25")
        self.assertEqual(result, "25/12/2023")
    
    def test_convert_date_format_custom_formats(self):
        """Test konwersji daty z niestandardowymi formatami."""
        result = convert_date_format("25/12/2023", "%d/%m/%Y", "%Y-%m-%d")
        self.assertEqual(result, "2023-12-25")
        
        result = convert_date_format("2023-12-25", "%Y-%m-%d", "%B %d, %Y")
        self.assertEqual(result, "December 25, 2023")
    
    def test_convert_date_format_invalid_date(self):
        """Test błędu dla niepoprawnej daty."""
        with self.assertRaises(ValueError):
            convert_date_format("2023-13-25") 
        with self.assertRaises(ValueError):
            convert_date_format("invalid-date")
    
    def test_convert_date_format_type_error(self):
        """Test błędu typu dla konwersji daty."""
        with self.assertRaises(TypeError):
            convert_date_format(20231225)
        with self.assertRaises(TypeError):
            convert_date_format("2023-12-25", 123)
    
    def test_is_palindrome_simple_cases(self):
        """Test prostych palindromów."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
    
    def test_is_palindrome_case_insensitive(self):
        """Test palindromów z różną wielkością liter."""
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("Level"))
        self.assertTrue(is_palindrome("MadAm"))
    
    def test_is_palindrome_with_spaces(self):
        """Test palindromów ze spacjami."""
        self.assertTrue(is_palindrome("race car"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Was it a rat I saw"))
    
    def test_is_palindrome_edge_cases(self):
        """Test przypadków brzegowych dla palindromów."""
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a")) 
        self.assertTrue(is_palindrome(" ")) 
    
    def test_is_palindrome_type_error(self):
        """Test błędu typu dla palindromów."""
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome(None)

class TestParametrized(unittest.TestCase):
    
    def test_validate_email_parametrized(self):
        """Test parametryzowany dla walidacji e-mail."""
        test_cases = [
            ("test@example.com", True),
            ("invalid-email", False),
            ("user@domain.co.uk", True),
            ("@domain.com", False),
            ("", False)
        ]
        
        for email, expected in test_cases:
            with self.subTest(email=email, expected=expected):
                self.assertEqual(validate_email(email), expected)
    
    def test_calculate_circle_area_parametrized(self):
        """Test parametryzowany dla obliczania pola koła."""
        test_cases = [
            (1, math.pi),
            (2, 4 * math.pi),
            (0, 0),
            (0.5, 0.25 * math.pi)
        ]
        
        for radius, expected in test_cases:
            with self.subTest(radius=radius, expected=expected):
                self.assertAlmostEqual(calculate_circle_area(radius), expected, places=5)

if __name__ == '__main__':
    unittest.main(verbosity=2)
