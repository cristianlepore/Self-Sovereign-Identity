import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import os

# Funzione principale
def kmeans_clustering(file_path, n_clusters):
    """
    Applica l'algoritmo K-Means a un dataset CSV.

    :param file_path: Percorso al file CSV.
    :param n_clusters: Numero di cluster (k).
    """
    # Read and load data
    data = pd.read_csv(file_path)
    
    # Seleziona colonne numeriche
    numerical_columns = data.select_dtypes(include=[np.number]).dropna(axis=1, how='all')
    
    # Riempi i valori NaN con 0 (se necessario)
    cleaned_data = numerical_columns.fillna(0)
    
    # Applica K-Means
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
    clusters = kmeans.fit_predict(cleaned_data)
    
    # Aggiungi i risultati dei cluster al dataset originale
    data['Clustering'] = clusters
    
    # Salva il dataset con i cluster in un nuovo file
    output_file = "Output.csv"
    data.to_csv(output_file, index=False)
    print(f"Clustering completed! Results saved in: {output_file}")
    print(data[['Clustering']].value_counts().sort_index())

# Esegui il programma
if __name__ == "__main__":
    # Percorso della cartella Download
    # Settare il percorso corretto per la propria configurazione
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads/SSI_principles/Definition/Program")
    file_path = os.path.join(download_folder, "Input.csv")
    
    # Numero di cluster (k)
    n_clusters = 5
    
    # Esegui la funzione
    kmeans_clustering(file_path, n_clusters)
