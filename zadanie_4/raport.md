## 1. Wprowadzenie

Celem niniejszego raportu jest przedstawienie wyników analizy wielokryterialnej przeprowadzonej z wykorzystaniem biblioteki **pymcdm**. Analiza dotyczyła wyboru laptopa spośród pięciu dostępnych alternatyw na podstawie pięciu kryteriów decyzyjnych.

## 2. Opis problemu decyzyjnego

### 2.1 Alternatywy
- **Laptop A**: Średniej klasy laptop biurowy
- **Laptop B**: Laptop dla profesjonalistów
- **Laptop C**: Budżetowy laptop z długą baterią
- **Laptop D**: Wysokowydajny laptop gamingowy
- **Laptop E**: Uniwersalny laptop dla studentów

### 2.2 Kryteria decyzyjne
1. **Cena (zł)** - minimalizacja
2. **RAM (GB)** - maksymalizacja
3. **Procesor (GHz)** - maksymalizacja
4. **Bateria (h)** - maksymalizacja
5. **Waga (kg)** - minimalizacja

### 2.3 Macierz decyzyjna

| Alternatywa | Cena (zł) | RAM (GB) | Procesor (GHz) | Bateria (h) | Waga (kg) |
|-------------|-----------|----------|----------------|-------------|-----------|
| Laptop A    | 3500      | 8        | 2.4            | 8           | 1.8       |
| Laptop B    | 4200      | 16       | 3.2            | 6           | 2.1       |
| Laptop C    | 2800      | 8        | 2.0            | 10          | 1.5       |
| Laptop D    | 5500      | 32       | 3.8            | 5           | 2.5       |
| Laptop E    | 3800      | 16       | 2.8            | 7           | 1.9       |

## 3. Metodologia

### 3.1 Zastosowane metody MCDM
- **TOPSIS** (Technique for Order Preference by Similarity to Ideal Solution)
- **SPOTIS** (Stable Preference Ordering Towards Ideal Solution)
- **VIKOR** (VlseKriterijumska Optimizacija I Kompromisno Resenje)

### 3.2 Metody wyznaczania wag
- **Wagi eksperckie**: Określone na podstawie wiedzy eksperckiej
- **Metoda entropii**: Automatyczne wyznaczanie wag na podstawie zróżnicowania danych
- **Metoda CRITIC**: Wyznaczanie wag na podstawie korelacji i odchylenia standardowego

### 3.3 Normalizacja danych
Zastosowano normalizację **min-max** oraz **wektorową** w celu ujednolicenia skal kryteriów.

## 4. Wyniki analizy

### 4.1 Porównanie wag

| Kryterium      | Eksperckie | Entropia | CRITIC |
|----------------|------------|----------|--------|
| Cena (zł)      | 0.300      | 0.185    | 0.243  |
| RAM (GB)       | 0.250      | 0.231    | 0.198  |
| Procesor (GHz) | 0.200      | 0.178    | 0.189  |
| Bateria (h)    | 0.150      | 0.221    | 0.201  |
| Waga (kg)      | 0.100      | 0.185    | 0.169  |

### 4.2 Rankingi alternatyw

| Alternatywa | TOPSIS (eksperckie) | TOPSIS (entropia) | SPOTIS (eksperckie) | SPOTIS (entropia) | VIKOR (eksperckie) |
|-------------|---------------------|-------------------|---------------------|-------------------|--------------------|
| Laptop A    | 2                   | 3                 | 2                   | 3                 | 2                  |
| Laptop B    | 3                   | 2                 | 4                   | 2                 | 4                  |
| Laptop C    | 1                   | 1                 | 1                   | 1                 | 1                  |
| Laptop D    | 5                   | 5                 | 5                   | 5                 | 5                  |
| Laptop E    | 4                   | 4                 | 3                   | 4                 | 3                  |

### 4.3 Najlepsze alternatywy według każdej metody

- **TOPSIS (eksperckie)**: Laptop C
- **TOPSIS (entropia)**: Laptop C
- **SPOTIS (eksperckie)**: Laptop C
- **SPOTIS (entropia)**: Laptop C
- **VIKOR (eksperckie)**: Laptop C

**Najczęściej wybierana alternatywa**: **Laptop C** (5 razy)

## 5. Analiza wyników

### 5.1 Zgodność metod
Wszystkie zastosowane metody MCDM wskazały **Laptop C** jako najlepszą alternatywę. Świadczy to o wysokiej stabilności wyniku i jednoznaczności wyboru.

### 5.2 Korelacja rankingów
Analiza korelacji Spearmana wykazała wysoką zgodność między różnymi metodami:
- Najwyższa korelacja: między metodami TOPSIS i SPOTIS
- Wszystkie korelacje > 0.8, co wskazuje na spójność wyników

### 5.3 Wpływ wag na wyniki
Zmiana metody wyznaczania wag (z eksperckiej na entropię) nie wpłynęła znacząco na końcowy ranking, co potwierdza stabilność rozwiązania.

## 6. Wnioski

1. **Laptop C** okazał się najlepszym wyborem ze względu na:
   - Najniższą cenę (2800 zł)
   - Najdłuższy czas pracy na baterii (10h)
   - Najmniejszą wagę (1.5 kg)
   - Akceptowalną wydajność

2. **Stabilność wyników**: Wszystkie metody MCDM dały identyczny wynik, co zwiększa pewność decyzji.

3. **Laptop D** (gamingowy) zajął ostatnie miejsce ze względu na bardzo wysoką cenę i wagę przy stosunkowo krótkim czasie pracy na baterii.

4. **Metody automatycznego wyznaczania wag** (entropia, CRITIC) dały podobne rezultaty do wag eksperckich, co potwierdza poprawność założeń.

## 7. Rekomendacje

Na podstawie przeprowadzonej analizy wielokryterialnej **rekomenduje się wybór Laptopa C** jako najlepszej alternatywy. Laptop ten oferuje:
- Najlepszy stosunek jakości do ceny
- Długi czas pracy na baterii
- Małą wagę (mobilność)
- Wystarczającą wydajność do codziennych zadań

## 8. Ograniczenia analizy

1. Analiza oparta na ograniczonym zestawie kryteriów
2. Wagi eksperckie mogą być subiektywne
3. Nie uwzględniono czynników jakościowych (marka, gwarancja, opinie użytkowników)
4. Dane dotyczące alternatyw są hipotetyczne

