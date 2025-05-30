import re
import math
from datetime import datetime

def validate_email(email):
    """
    Sprawdza poprawność adresu e-mail.
    
    Args:
        email (str): Adres e-mail do sprawdzenia
        
    Returns:
        bool: True jeśli e-mail jest poprawny, False w przeciwnym przypadku
        
    Raises:
        TypeError: Jeśli email nie jest stringiem
    """
    if not isinstance(email, str):
        raise TypeError("Email musi być stringiem")
    
    if not email:
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def calculate_circle_area(radius):
    """
    Oblicza pole koła na podstawie promienia.
    
    Args:
        radius (float): Promień koła
        
    Returns:
        float: Pole koła
        
    Raises:
        ValueError: Jeśli promień jest ujemny
        TypeError: Jeśli promień nie jest liczbą
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Promień musi być liczbą")
    
    if radius < 0:
        raise ValueError("Promień nie może być ujemny")
    
    return math.pi * radius ** 2

def filter_even_numbers(numbers):
    """
    Filtruje listę, zwracając tylko liczby parzyste.
    
    Args:
        numbers (list): Lista liczb do przefiltrowania
        
    Returns:
        list: Lista zawierająca tylko liczby parzyste
        
    Raises:
        TypeError: Jeśli argument nie jest listą lub zawiera nie-liczby
    """
    if not isinstance(numbers, list):
        raise TypeError("Argument musi być listą")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("Wszystkie elementy listy muszą być liczbami")
    
    return [num for num in numbers if num % 2 == 0]

def convert_date_format(date_string, input_format="%Y-%m-%d", output_format="%d/%m/%Y"):
    """
    Konwertuje format daty z jednego na drugi.
    
    Args:
        date_string (str): Data w formacie wejściowym
        input_format (str): Format wejściowy (domyślnie "%Y-%m-%d")
        output_format (str): Format wyjściowy (domyślnie "%d/%m/%Y")
        
    Returns:
        str: Data w nowym formacie
        
    Raises:
        ValueError: Jeśli data nie pasuje do formatu
        TypeError: Jeśli argumenty nie są stringami
    """
    if not isinstance(date_string, str):
        raise TypeError("Data musi być stringiem")
    
    if not isinstance(input_format, str) or not isinstance(output_format, str):
        raise TypeError("Formaty muszą być stringami")
    
    try:
        date_obj = datetime.strptime(date_string, input_format)
        return date_obj.strftime(output_format)
    except ValueError as e:
        raise ValueError(f"Niepoprawny format daty: {e}")

def is_palindrome(text):
    """
    Sprawdza, czy tekst jest palindromem (ignoruje wielkość liter i spacje).
    
    Args:
        text (str): Tekst do sprawdzenia
        
    Returns:
        bool: True jeśli tekst jest palindromem, False w przeciwnym przypadku
        
    Raises:
        TypeError: Jeśli text nie jest stringiem
    """
    if not isinstance(text, str):
        raise TypeError("Tekst musi być stringiem")
    
    cleaned_text = ''.join(text.lower().split())
    
    return cleaned_text == cleaned_text[::-1]
