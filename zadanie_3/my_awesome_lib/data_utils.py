"""
Moduł narzędzi do przetwarzania danych.

Zawiera funkcje i klasy do manipulacji, konwersji i filtrowania danych.
"""

from typing import List, Dict, Any, Union, Callable
import json
import csv
from pathlib import Path


class DataProcessor:
    """
    Klasa do zaawansowanego przetwarzania danych.
    
    Umożliwia ładowanie, transformację i eksport danych w różnych formatach.
    """
    
    def __init__(self):
        """Inicjalizuje procesor danych."""
        self.data = []
    
    def load_from_list(self, data: List[Any]) -> None:
        """
        Ładuje dane z listy.
        
        Args:
            data: Lista danych do załadowania
            
        Raises:
            TypeError: Gdy data nie jest listą
        """
        if not isinstance(data, list):
            raise TypeError("Dane muszą być w formie listy")
        self.data = data.copy()
    
    def load_from_csv(self, filepath: Union[str, Path]) -> None:
        """
        Ładuje dane z pliku CSV.
        
        Args:
            filepath: Ścieżka do pliku CSV
            
        Raises:
            FileNotFoundError: Gdy plik nie istnieje
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.data = list(reader)
    
    def transform(self, func: Callable) -> List[Any]:
        """
        Transformuje dane używając podanej funkcji.
        
        Args:
            func: Funkcja transformująca
            
        Returns:
            Lista transformowanych danych
        """
        return [func(item) for item in self.data]


def convert_to_dict(keys: List[str], values: List[Any]) -> Dict[str, Any]:
    """
    Konwertuje listy kluczy i wartości na słownik.
    
    Args:
        keys: Lista kluczy
        values: Lista wartości
        
    Returns:
        Słownik utworzony z kluczy i wartości
        
    Raises:
        ValueError: Gdy listy mają różne długości
        
    Example:
        >>> convert_to_dict(['a', 'b'], [1, 2])
        {'a': 1, 'b': 2}
    """
    if len(keys) != len(values):
        raise ValueError("Listy kluczy i wartości muszą mieć tę samą długość")
    return dict(zip(keys, values))


def filter_data(data: List[Dict[str, Any]], condition: Callable[[Dict], bool]) -> List[Dict[str, Any]]:
    """
    Filtruje listę słowników według podanego warunku.
    
    Args:
        data: Lista słowników do przefiltrowania
        condition: Funkcja zwracająca bool dla każdego elementu
        
    Returns:
        Lista przefiltrowanych słowników
        
    Example:
        >>> data = [{'age': 25}, {'age': 30}]
        >>> filter_data(data, lambda x: x['age'] > 27)
        [{'age': 30}]
    """
    return [item for item in data if condition(item)]
