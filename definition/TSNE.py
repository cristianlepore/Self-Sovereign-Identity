import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

# Definizione delle features (principi)
principi = ["Existence and representation", "Ownership and control", "Access and availability", 
            "Transparency", "Persistence", "Portability", "Interoperability", "Consent", 
            "Security and protection", "Privacy and minimal disclosure", "Standard", "Cost", 
            "Usability and Consistency", "Decentralization and Autonomy", "Verifiability and Authenticity", 
            "Self-generatable and independent", "Opt-in", "Opt-out", "Simple", "Non-repudiatable", 
            "Reliable", "Equivalent", "Single Source", "Validity", "Freedom Information", "Auditability", 
            "Integrity", "Effectiveness", "Efficiency", "Manageability", "Trust", "Scalable", 
            "Equity and Inclusion", "Delegation"]

dati = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Tobin and Reed
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Andrieu et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Ferdous et al.
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Mühle et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Gilani et al.
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # Naik and Jenkins
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Sheldrake
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Toth and Kalman
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # eSSIF-Lab
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # ToIP
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],  # Sovrin
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # BkThDVr
    [0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],  # Glöckler et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Pava-Díaz et al.
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],  # Satybaldy et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Stokkink and Pouwelse
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Čučko et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Allen
])

# TRASPOSIZIONE per applicare t-SNE alle FEATURES invece che agli autori
dati_T = dati.T  # Ora le righe sono le features (principi)

# Applichiamo t-SNE per ridurre a 2 dimensioni
tsne = TSNE(n_components=2, perplexity=5, random_state=42)  
dati_tsne = tsne.fit_transform(dati_T)

# Clusterizzazione con K-Means
num_clusters = 2  # Modifica questo valore se necessario
kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
clusters = kmeans.fit_predict(dati_tsne)

# Creiamo il plot con i cluster
plt.figure(figsize=(12, 8))
colors = ["red", "blue", "green", "purple", "orange", "brown"]  # Espandibile se servono più colori

for i in range(num_clusters):
    plt.scatter(dati_tsne[clusters == i, 0], dati_tsne[clusters == i, 1], 
                s=100, color=colors[i % len(colors)], label=f"Cluster {i+1}")

# Aggiungiamo le etichette delle features (principi)
for i, principio in enumerate(principi[:len(dati_T)]):  
    plt.text(dati_tsne[i, 0], dati_tsne[i, 1], principio, fontsize=9, ha='right')

plt.xlabel("Dimensione 1")
plt.ylabel("Dimensione 2")
plt.title(f"Visualizzazione t-SNE delle Features con {num_clusters} Clusters (K-Means)")
plt.legend()
plt.show()
