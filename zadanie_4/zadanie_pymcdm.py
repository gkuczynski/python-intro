import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR
from pymcdm.normalizations import minmax_normalization, vector_normalization
from pymcdm.weights import entropy_weighting, critic_weighting
from pymcdm.helpers import rrankdata
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

def main():
    """Główna funkcja wykonująca analizę wielokryterialną"""
    
    print("="*60)
    print("ANALIZA WIELOKRYTERIALNA - WYBÓR LAPTOPA")
    print("Biblioteka: pymcdm")
    print("="*60)
    
    # 1. PRZYGOTOWANIE DANYCH
    print("\n1. PRZYGOTOWANIE DANYCH DECYZYJNYCH")
    print("-" * 40)
    
    # Macierz decyzyjna - wybór laptopa
    # Kryteria: Cena (zł), RAM (GB), Procesor (GHz), Bateria (h), Waga (kg)
    alternatives = np.array([
        [3500, 8, 2.4, 8, 1.8],   # Laptop A
        [4200, 16, 3.2, 6, 2.1],  # Laptop B
        [2800, 8, 2.0, 10, 1.5],  # Laptop C
        [5500, 32, 3.8, 5, 2.5],  # Laptop D
        [3800, 16, 2.8, 7, 1.9]   # Laptop E
    ])
    
    # Nazwy alternatyw i kryteriów
    alt_names = ['Laptop A', 'Laptop B', 'Laptop C', 'Laptop D', 'Laptop E']
    criteria_names = ['Cena (zł)', 'RAM (GB)', 'Procesor (GHz)', 'Bateria (h)', 'Waga (kg)']
    
    # Typy kryteriów (1 = maksymalizacja, -1 = minimalizacja)
    types = np.array([-1, 1, 1, 1, -1])  # Cena i waga minimalizowane
    
    # Wagi eksperckie
    weights_expert = np.array([0.3, 0.25, 0.2, 0.15, 0.1])
    
    # Wyświetlenie danych
    df = pd.DataFrame(alternatives, index=alt_names, columns=criteria_names)
    print("Macierz decyzyjna:")
    print(df)
    print(f"\nWagi eksperckie: {weights_expert}")
    print(f"Typy kryteriów: {types}")
    print("(-1 = minimalizacja, 1 = maksymalizacja)")
    
    # 2. NORMALIZACJA DANYCH
    print("\n\n2. NORMALIZACJA DANYCH")
    print("-" * 40)
    
    # Normalizacja min-max
    normalized_minmax = minmax_normalization(alternatives)
    df_norm_minmax = pd.DataFrame(normalized_minmax, index=alt_names, columns=criteria_names)
    print("Macierz po normalizacji min-max:")
    print(df_norm_minmax.round(3))
    
    # Normalizacja wektorowa
    normalized_vector = vector_normalization(alternatives)
    df_norm_vector = pd.DataFrame(normalized_vector, index=alt_names, columns=criteria_names)
    print("\nMacierz po normalizacji wektorowej:")
    print(df_norm_vector.round(3))
    
    # 3. WYZNACZANIE WAG
    print("\n\n3. WYZNACZANIE WAG RÓŻNYMI METODAMI")
    print("-" * 40)
    
    # Wagi metodą entropii
    weights_entropy = entropy_weighting(alternatives)
    print(f"Wagi metodą entropii: {weights_entropy.round(3)}")
    
    # Wagi metodą CRITIC
    weights_critic = critic_weighting(alternatives)
    print(f"Wagi metodą CRITIC: {weights_critic.round(3)}")
    
    # Porównanie wag
    weights_comparison = pd.DataFrame({
        'Eksperckie': weights_expert,
        'Entropia': weights_entropy,
        'CRITIC': weights_critic
    }, index=criteria_names)
    print("\nPorównanie wag:")
    print(weights_comparison.round(3))
    
    # 4. METODY MCDM
    print("\n\n4. ZASTOSOWANIE METOD MCDM")
    print("-" * 40)
    
    # TOPSIS
    print("\n4.1 METODA TOPSIS")
    topsis = TOPSIS()
    
    # TOPSIS z wagami eksperckimi
    topsis_scores_expert = topsis(alternatives, weights_expert, types)
    topsis_ranking_expert = rrankdata(topsis_scores_expert)
    
    print("TOPSIS (wagi eksperckie):")
    topsis_results_expert = pd.DataFrame({
        'Alternatywa': alt_names,
        'Wynik': topsis_scores_expert.round(3),
        'Ranking': topsis_ranking_expert.astype(int)
    })
    print(topsis_results_expert.sort_values('Ranking'))
    
    # TOPSIS z wagami entropii
    topsis_scores_entropy = topsis(alternatives, weights_entropy, types)
    topsis_ranking_entropy = rrankdata(topsis_scores_entropy)
    
    print("\nTOPSIS (wagi entropii):")
    topsis_results_entropy = pd.DataFrame({
        'Alternatywa': alt_names,
        'Wynik': topsis_scores_entropy.round(3),
        'Ranking': topsis_ranking_entropy.astype(int)
    })
    print(topsis_results_entropy.sort_values('Ranking'))
    
    # SPOTIS
    print("\n4.2 METODA SPOTIS")
    spotis = SPOTIS()
    
    # SPOTIS z wagami eksperckimi
    spotis_scores_expert = spotis(alternatives, weights_expert, types)
    spotis_ranking_expert = rrankdata(spotis_scores_expert, reverse=True)
    
    print("SPOTIS (wagi eksperckie):")
    spotis_results_expert = pd.DataFrame({
        'Alternatywa': alt_names,
        'Wynik': spotis_scores_expert.round(3),
        'Ranking': spotis_ranking_expert.astype(int)
    })
    print(spotis_results_expert.sort_values('Ranking'))
    
    # SPOTIS z wagami entropii
    spotis_scores_entropy = spotis(alternatives, weights_entropy, types)
    spotis_ranking_entropy = rrankdata(spotis_scores_entropy, reverse=True)
    
    print("\nSPOTIS (wagi entropii):")
    spotis_results_entropy = pd.DataFrame({
        'Alternatywa': alt_names,
        'Wynik': spotis_scores_entropy.round(3),
        'Ranking': spotis_ranking_entropy.astype(int)
    })
    print(spotis_results_entropy.sort_values('Ranking'))
    
    # VIKOR
    print("\n4.3 METODA VIKOR (OPCJONALNIE)")
    vikor = VIKOR()
    
    vikor_scores_expert = vikor(alternatives, weights_expert, types)
    vikor_ranking_expert = rrankdata(vikor_scores_expert, reverse=True)
    
    print("VIKOR (wagi eksperckie):")
    vikor_results_expert = pd.DataFrame({
        'Alternatywa': alt_names,
        'Wynik': vikor_scores_expert.round(3),
        'Ranking': vikor_ranking_expert.astype(int)
    })
    print(vikor_results_expert.sort_values('Ranking'))
    
    # 5. PORÓWNANIE WYNIKÓW
    print("\n\n5. PORÓWNANIE WYNIKÓW")
    print("-" * 40)
    
    # Tabela porównawcza rankingów
    comparison_df = pd.DataFrame({
        'Alternatywa': alt_names,
        'TOPSIS (eksperckie)': topsis_ranking_expert.astype(int),
        'TOPSIS (entropia)': topsis_ranking_entropy.astype(int),
        'SPOTIS (eksperckie)': spotis_ranking_expert.astype(int),
        'SPOTIS (entropia)': spotis_ranking_entropy.astype(int),
        'VIKOR (eksperckie)': vikor_ranking_expert.astype(int)
    })
    
    print("Porównanie rankingów wszystkich metod:")
    print(comparison_df)
    
    # Najlepsze alternatywy
    print("\nNajlepsza alternatywa według każdej metody:")
    methods_rankings = [
        topsis_ranking_expert, topsis_ranking_entropy, 
        spotis_ranking_expert, spotis_ranking_entropy, 
        vikor_ranking_expert
    ]
    method_names = [
        'TOPSIS (eksperckie)', 'TOPSIS (entropia)', 
        'SPOTIS (eksperckie)', 'SPOTIS (entropia)', 
        'VIKOR (eksperckie)'
    ]
    
    best_alternatives = {}
    for method, ranking in zip(method_names, methods_rankings):
        best_alt_idx = np.argmin(ranking)
        best_alternatives[method] = alt_names[best_alt_idx]
        print(f"{method}: {alt_names[best_alt_idx]}")
    
    # Najczęściej wybierana alternatywa
    most_common = Counter(best_alternatives.values()).most_common(1)[0]
    print(f"\nNAJCZĘŚCIEJ WYBIERANA: {most_common[0]} ({most_common[1]} razy)")
    
    # 6. ANALIZA KORELACJI
    print("\n\n6. ANALIZA KORELACJI RANKINGÓW")
    print("-" * 40)
    
    print("Korelacja Spearmana między rankingami:")
    for i in range(len(methods_rankings)):
        for j in range(i+1, len(methods_rankings)):
            corr, p_value = spearmanr(methods_rankings[i], methods_rankings[j])
            print(f"{method_names[i]} vs {method_names[j]}: {corr:.3f} (p={p_value:.3f})")
    
    # 7. WIZUALIZACJA
    print("\n\n7. GENEROWANIE WIZUALIZACJI")
    print("-" * 40)
    
    # Wykres porównania rankingów
    plt.figure(figsize=(12, 8))
    rankings_matrix = np.array(methods_rankings).T
    
    for i, alt in enumerate(alt_names):
        plt.plot(method_names, rankings_matrix[i], marker='o', linewidth=2, label=alt)
    
    plt.ylabel('Pozycja w rankingu')
    plt.title('Porównanie rankingów różnych metod MCDM')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.gca().invert_yaxis()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('ranking_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("Zapisano wykres: ranking_comparison.png")
    
    # Mapa cieplna rankingów
    plt.figure(figsize=(10, 6))
    ranking_heatmap = comparison_df.set_index('Alternatywa').iloc[:, :5]
    sns.heatmap(ranking_heatmap, annot=True, cmap='RdYlGn_r', center=3, 
                cbar_kws={'label': 'Pozycja w rankingu'})
    plt.title('Mapa cieplna rankingów - różne metody MCDM')
    plt.tight_layout()
    plt.savefig('ranking_heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("Zapisano mapę cieplną: ranking_heatmap.png")
    
    return comparison_df, weights_comparison, best_alternatives

if __name__ == "__main__":
    main()
