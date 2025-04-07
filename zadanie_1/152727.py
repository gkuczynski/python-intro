# 1. Funkcja zip()
tabela_1 = [0, 1, 2, 3, 4]
tabela_2 = [5, 6, 7, 8, 9]

print(list(zip(tabela_1, tabela_2)))

# Funkcja zip() służy do łączenia wielu iterowalnych obiektów (np. list, krotek) w pary.
# Zwraca iterator z elementami połączonymi według indeksu.
# https://docs.python.org/3/library/functions.html#zip

# 2. Moduł random
import random
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(lista))

# Moduł random pozwala generować liczby losowe, wybierać losowe elementy z sekwencji itp.
# https://docs.python.org/3/library/random.html

# 3. Wyjątek ValueError
try:
  nowaLiczba = int(input("Podaj liczbę: "))
  print(f"Wpisana liczba to: {nowaLiczba}")
except ValueError:
  print(f"Wpisano: {nowaLiczba}, należy wpisać liczbę całkowitą")

# ValueError jest zgłaszany, gdy funkcja otrzymuje prawidłowy typ danych,
# ale jego wartość jest nieodpowiednia
# https://docs.python.org/3/library/exceptions.html#ValueError

