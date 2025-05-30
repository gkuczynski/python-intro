"""Testy dla modułu text_processing."""

import unittest
from my_awesome_lib.text_processing import TextAnalyzer, clean_text, word_frequency


class TestTextAnalyzer(unittest.TestCase):
    """Testy dla klasy TextAnalyzer."""
    
    def setUp(self):
        """Przygotowanie analizatora testowego."""
        self.analyzer = TextAnalyzer("Hello world! How are you? I am fine.")
    
    def test_word_count(self):
        """Test liczenia słów."""
        result = self.analyzer.word_count()
        self.assertEqual(result, 8)
    
    def test_char_count_with_spaces(self):
        """Test liczenia znaków ze spacjami."""
        result = self.analyzer.char_count(include_spaces=True)
        self.assertEqual(result, len("Hello world! How are you? I am fine."))
    
    def test_char_count_without_spaces(self):
        """Test liczenia znaków bez spacji."""
        result = self.analyzer.char_count(include_spaces=False)
        expected = len("Hello world! How are you? I am fine.".replace(' ', ''))
        self.assertEqual(result, expected)
    
    def test_sentence_count(self):
        """Test liczenia zdań."""
        result = self.analyzer.sentence_count()
        self.assertEqual(result, 3)
    
    def test_set_text(self):
        """Test ustawiania nowego tekstu."""
        new_text = "New text for testing."
        self.analyzer.set_text(new_text)
        self.assertEqual(self.analyzer.text, new_text)


class TestCleanText(unittest.TestCase):
    """Testy dla funkcji clean_text."""
    
    def test_clean_text_default(self):
        """Test domyślnego czyszczenia tekstu."""
        text = "Hello, World!"
        result = clean_text(text)
        expected = "hello world"
        self.assertEqual(result, expected)
    
    def test_clean_text_keep_punctuation(self):
        """Test czyszczenia z zachowaniem interpunkcji."""
        text = "Hello, World!"
        result = clean_text(text, remove_punctuation=False)
        expected = "hello, world!"
        self.assertEqual(result, expected)
    
    def test_clean_text_keep_case(self):
        """Test czyszczenia z zachowaniem wielkości liter."""
        text = "Hello, World!"
        result = clean_text(text, to_lowercase=False)
        expected = "Hello World"
        self.assertEqual(result, expected)


class TestWordFrequency(unittest.TestCase):
    """Testy dla funkcji word_frequency."""
    
    def test_word_frequency_basic(self):
        """Test podstawowego liczenia częstotliwości."""
        text = "hello world hello"
        result = word_frequency(text)
        expected = {'hello': 2, 'world': 1}
        self.assertEqual(result, expected)
    
    def test_word_frequency_top_n(self):
        """Test ograniczenia do top N słów."""
        text = "a b c a b a"
        result = word_frequency(text, top_n=2)
        expected = {'a': 3, 'b': 2}
        self.assertEqual(result, expected)
    
    def test_word_frequency_empty_text(self):
        """Test dla pustego tekstu."""
        result = word_frequency("")
        self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main()
