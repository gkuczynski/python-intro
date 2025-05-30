"""Testy dla modułu data_utils."""

import unittest
from my_awesome_lib.data_utils import DataProcessor, convert_to_dict, filter_data


class TestDataProcessor(unittest.TestCase):
    """Testy dla klasy DataProcessor."""
    
    def setUp(self):
        """Przygotowanie danych testowych."""
        self.processor = DataProcessor()
    
    def test_load_from_list(self):
        """Test ładowania danych z listy."""
        test_data = [1, 2, 3, 4, 5]
        self.processor.load_from_list(test_data)
        self.assertEqual(self.processor.data, test_data)
    
    def test_load_from_list_invalid_type(self):
        """Test błędu przy nieprawidłowym typie danych."""
        with self.assertRaises(TypeError):
            self.processor.load_from_list("not a list")
    
    def test_transform(self):
        """Test transformacji danych."""
        self.processor.load_from_list([1, 2, 3])
        result = self.processor.transform(lambda x: x * 2)
        self.assertEqual(result, [2, 4, 6])


class TestConvertToDict(unittest.TestCase):
    """Testy dla funkcji convert_to_dict."""
    
    def test_convert_to_dict_success(self):
        """Test poprawnej konwersji."""
        keys = ['a', 'b', 'c']
        values = [1, 2, 3]
        result = convert_to_dict(keys, values)
        expected = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(result, expected)
    
    def test_convert_to_dict_different_lengths(self):
        """Test błędu przy różnych długościach list."""
        keys = ['a', 'b']
        values = [1, 2, 3]
        with self.assertRaises(ValueError):
            convert_to_dict(keys, values)


class TestFilterData(unittest.TestCase):
    """Testy dla funkcji filter_data."""
    
    def test_filter_data_success(self):
        """Test poprawnego filtrowania."""
        data = [{'age': 25}, {'age': 30}, {'age': 20}]
        result = filter_data(data, lambda x: x['age'] > 22)
        expected = [{'age': 25}, {'age': 30}]
        self.assertEqual(result, expected)
    
    def test_filter_data_empty_result(self):
        """Test filtrowania zwracającego pustą listę."""
        data = [{'age': 25}, {'age': 30}]
        result = filter_data(data, lambda x: x['age'] > 50)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
