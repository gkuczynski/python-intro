"""
My Awesome Library - Biblioteka narzędziowa do przetwarzania danych, obliczeń matematycznych i tekstu.

Wersja: 1.0.0
Autor: Grzegorz
Licencja: MIT
"""

from .data_utils import DataProcessor, convert_to_dict, filter_data
from .math_tools import Calculator, fibonacci, prime_checker
from .text_processing import TextAnalyzer, clean_text, word_frequency

__version__ = "1.0.0"
__author__ = "Grzegorz"
__email__ = "test@test.test"

__all__ = [
    'DataProcessor', 'convert_to_dict', 'filter_data',
    'Calculator', 'fibonacci', 'prime_checker',
    'TextAnalyzer', 'clean_text', 'word_frequency'
]
