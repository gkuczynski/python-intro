"""
Moduł do przetwarzania tekstu.

Zawiera funkcje i klasy do analizy, czyszczenia i manipulacji tekstem.
"""

from typing import Dict, List, Set
import re
from collections import Counter


class TextAnalyzer:
    """
    Analizator tekstu z zaawansowanymi funkcjami statystycznymi.
    
    Umożliwia analizę tekstu pod kątem różnych metryk i statystyk.
    """
    
    def __init__(self, text: str = ""):
        """
        Inicjalizuje analizator tekstu.
        
        Args:
            text: Tekst do analizy
        """
        self.text = text
    
    def set_text(self, text: str) -> None:
        """
        Ustawia nowy tekst do analizy.
        
        Args:
            text: Nowy tekst
        """
        self.text = text
    
    def word_count(self) -> int:
        """
        Zlicza liczbę słów w tekście.
        
        Returns:
            Liczba słów
        """
        return len(self.text.split())
    
    def char_count(self, include_spaces: bool = True) -> int:
        """
        Zlicza liczbę znaków w tekście.
        
        Args:
            include_spaces: Czy liczyć spacje
            
        Returns:
            Liczba znaków
        """
        if include_spaces:
            return len(self.text)
        return len(self.text.replace(' ', ''))
    
    def sentence_count(self) -> int:
        """
        Zlicza liczbę zdań w tekście.
        
        Returns:
            Liczba zdań
        """
        sentences = re.split(r'[.!?]+', self.text)
        return len([s for s in sentences if s.strip()])


def clean_text(text: str, remove_punctuation: bool = True, to_lowercase: bool = True) -> str:
    """
    Czyści tekst z niepotrzebnych znaków.
    
    Args:
        text: Tekst do wyczyszczenia
        remove_punctuation: Czy usunąć znaki interpunkcyjne
        to_lowercase: Czy zamienić na małe litery
        
    Returns:
        Wyczyszczony tekst
        
    Example:
        >>> clean_text("Hello, World!")
        "hello world"
    """
    cleaned = text
    
    if to_lowercase:
        cleaned = cleaned.lower()
    
    if remove_punctuation:
        cleaned = re.sub(r'[^\w\s]', '', cleaned)
    
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    
    return cleaned


def word_frequency(text: str, top_n: int = None) -> Dict[str, int]:
    """
    Zlicza częstotliwość występowania słów w tekście.
    
    Args:
        text: Tekst do analizy
        top_n: Liczba najczęstszych słów do zwrócenia (None = wszystkie)
        
    Returns:
        Słownik z częstotliwością słów
        
    Example:
        >>> word_frequency("hello world hello")
        {'hello': 2, 'world': 1}
    """
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    
    counter = Counter(words)
    
    if top_n is not None:
        return dict(counter.most_common(top_n))
    
    return dict(counter)
