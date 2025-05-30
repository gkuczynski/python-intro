"""
Moduł narzędzi matematycznych.

Zawiera funkcje i klasy do obliczeń matematycznych, analizy liczb i statystyk.
"""

from typing import List, Union
import math


class Calculator:
    """
    Zaawansowany kalkulator z historią operacji.
    
    Umożliwia wykonywanie obliczeń i śledzenie historii operacji.
    """
    
    def __init__(self):
        """Inicjalizuje kalkulator z pustą historią."""
        self.history = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Dodaje dwie liczby.
        
        Args:
            a: Pierwsza liczba
            b: Druga liczba
            
        Returns:
            Suma liczb
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Mnoży dwie liczby.
        
        Args:
            a: Pierwsza liczba
            b: Druga liczba
            
        Returns:
            Iloczyn liczb
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """
        Podnosi liczbę do potęgi.
        
        Args:
            base: Podstawa
            exponent: Wykładnik
            
        Returns:
            Wynik potęgowania
        """
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result
    
    def get_history(self) -> List[str]:
        """
        Zwraca historię operacji.
        
        Returns:
            Lista operacji w formie stringów
        """
        return self.history.copy()


def fibonacci(n: int) -> List[int]:
    """
    Generuje ciąg Fibonacciego o długości n.
    
    Args:
        n: Liczba elementów ciągu do wygenerowania
        
    Returns:
        Lista zawierająca n pierwszych liczb Fibonacciego
        
    Raises:
        ValueError: Gdy n jest mniejsze od 0
        
    Example:
        >>> fibonacci(5)
        [0, 1, 1, 2, 3]
    """
    if n < 0:
        raise ValueError("n musi być liczbą nieujemną")
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence


def prime_checker(num: int) -> bool:
    """
    Sprawdza czy liczba jest liczbą pierwszą.
    
    Args:
        num: Liczba do sprawdzenia
        
    Returns:
        True jeśli liczba jest pierwsza, False w przeciwnym razie
        
    Raises:
        ValueError: Gdy num jest mniejsze od 2
        
    Example:
        >>> prime_checker(7)
        True
        >>> prime_checker(8)
        False
    """
    if num < 2:
        raise ValueError("Liczba musi być większa lub równa 2")
    
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    
    return True
