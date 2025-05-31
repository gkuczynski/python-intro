import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("=== DEMONSTRACJA BIBLIOTEK PANDAS I MATPLOTLIB ===")
print()

# PANDAS - Przykład 1: Podstawowe operacje na danych

print("1. PANDAS - Analiza danych sprzedażowych")
print("-" * 40)

# Tworzenie prostego DataFrame
data = {
    'Miesiąc': ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj'],
    'Sprzedaż': [1200, 1350, 1180, 1420, 1580],
    'Koszty': [800, 900, 850, 950, 1000]
}

df = pd.DataFrame(data)
print("Dane sprzedażowe:")
print(df)

# Obliczanie zysku
df['Zysk'] = df['Sprzedaż'] - df['Koszty']
print("\nDane z obliczonym zyskiem:")
print(df)

# Podstawowe statystyki
print(f"\nŚrednia sprzedaż: {df['Sprzedaż'].mean():.2f}")
print(f"Maksymalny zysk: {df['Zysk'].max()}")
print(f"Miesiąc z najwyższym zyskiem: {df.loc[df['Zysk'].idxmax(), 'Miesiąc']}")

print()

# PANDAS - Przykład 2: Filtrowanie danych

print("2. PANDAS - Filtrowanie danych")
print("-" * 40)

# Filtrowanie miesięcy z zyskiem powyżej 400
wysokie_zyski = df[df['Zysk'] > 400]
print("Miesiące z zyskiem powyżej 400:")
print(wysokie_zyski[['Miesiąc', 'Zysk']])

print()

# MATPLOTLIB - Przykład 1: Wykres słupkowy

print("3. MATPLOTLIB - Wykres słupkowy")
print("-" * 40)

plt.figure(figsize=(10, 6))
plt.bar(df['Miesiąc'], df['Sprzedaż'], color='lightblue', label='Sprzedaż')
plt.bar(df['Miesiąc'], df['Koszty'], color='lightcoral', label='Koszty')
plt.title('Sprzedaż i koszty według miesięcy')
plt.xlabel('Miesiąc')
plt.ylabel('Wartość (PLN)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('wykres_sprzedaz.png')
plt.show()

print("Wykres zapisany jako 'wykres_sprzedaz.png'")
print()

# MATPLOTLIB - Przykład 2: Wykres liniowy

print("4. MATPLOTLIB - Wykres liniowy")
print("-" * 40)

plt.figure(figsize=(8, 5))
plt.plot(df['Miesiąc'], df['Zysk'], marker='o', linewidth=2, color='green')
plt.title('Trend zysku w czasie')
plt.xlabel('Miesiąc')
plt.ylabel('Zysk (PLN)')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('wykres_zysk.png')
plt.show()

print("Wykres zapisany jako 'wykres_zysk.png'")


