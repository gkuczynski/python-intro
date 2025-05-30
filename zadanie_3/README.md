# My Awesome Library

Biblioteka narzędziowa do przetwarzania danych, obliczeń matematycznych i analizy tekstu w języku Python.

## 📋 Opis

My Awesome Library to wszechstronna biblioteka programistyczna zawierająca narzędzia do:
- **Przetwarzania danych** - ładowanie, transformacja i filtrowanie danych
- **Obliczeń matematycznych** - zaawansowane operacje matematyczne i analiza liczb
- **Analizy tekstu** - czyszczenie, analiza i statystyki tekstowe

## 🚀 Instalacja

### Instalacja z repozytorium GitHub
git clone https://github.com/gkuczynski/my-awesome-lib.git \
cd my-awesome-lib \
pip install -e .


## 📖 Użycie

### Przetwarzanie danych
from my_awesome_lib import DataProcessor, convert_to_dict, filter_data

#### Użycie klasy DataProcessor
processor = DataProcessor() \
processor.load_from_list() \
doubled = processor.transform(lambda x: x * 2) \
print(doubled) #

#### Konwersja list na słownik
result = convert_to_dict(['a', 'b', 'c'], ) \
print(result) # {'a': 1, 'b': 2, 'c': 3} 

#### Filtrowanie danych
data = [{'age': 25}, {'age': 30}, {'age': 20}] \
adults = filter_data(data, lambda x: x['age'] >= 25) \
print(adults) # [{'age': 25}, {'age': 30}]


### Obliczenia matematyczne

#### Użycie kalkulatora z historią
calc = Calculator() \
result = calc.add(5, 3) \
print(result) # 8 \
print(calc.get_history()) # ['5 + 3 = 8']

#### Generowanie ciągu Fibonacciego
fib_sequence = fibonacci(10) \
print(fib_sequence)

#### Sprawdzanie liczb pierwszych
is_prime = prime_checker(17) \
print(is_prime) # True

### Analiza tekstu
from my_awesome_lib import TextAnalyzer, clean_text, word_frequency

#### Analiza tekstu
analyzer = TextAnalyzer("Hello world! How are you?") \
print(analyzer.word_count()) # 5 \
print(analyzer.sentence_count()) # 2

#### Czyszczenie tekstu
cleaned = clean_text("Hello, World!") \
print(cleaned) # "hello world"

#### Analiza częstotliwości słów
freq = word_frequency("hello world hello python world") \
print(freq) # {'hello': 2, 'world': 2, 'python': 1}

## 📄 Licencja

Ten projekt jest licencjonowany na licencji MIT - zobacz plik [LICENSE](LICENSE) po szczegóły.

## ✨ Autor

- **Grzegorz** - [gkuczynski](https://github.com/gkuczynski)