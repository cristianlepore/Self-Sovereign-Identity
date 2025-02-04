import matplotlib.pyplot as plt
import numpy as np

# Dati estratti dalla tabella
autori = ["Tobin and Reed", "Andrieu et al.", "Ferdous et al.", "Mühle et al.", "Gilani et al.", "Naik and Jenkins", "Sheldrake", "Toth and Kalman", "eSSIF-Lab", "ToIP", "Sovrin", "BkThDVr", "Glöckler et al.", "Pava-Díaz et al.", "Satybaldy et al.", "Stokkink and Pouwelse", "Čučko et al.", "Allen"]

principi = ["Existence and representation", "Consent", "Ownership and control", "Security and protection", "Persistence", "Privacy and minimal disclosure", "Access and availability", "Transparency", "Portability", "Interoperability", "Cost", "Standard", "Decentralization and Autonomy", "Verifiability and Authenticity", "Usability and consistency"]

# Mappatura della tabella in formato binario (1 se il principio è presente per l'autore, altrimenti 0)
dati = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # Tobin and Reed
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],  # Andrieu et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Ferdous et al.
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # Mühle et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],  # Gilani et al.
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],  # Naik and Jenkins
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Sheldrake
    [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],  # Toth and Kalman
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # eSSIF-Lab
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # ToIP
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1],  # Sovrin
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],  # BkThDVr
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],  # Glöckler et al.
    [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1],  # Pava-Díaz et al.
    [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],  # Satybaldy et al.
    [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],  # Stokkink and Pouwelse
    [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],  # Čučko et al.
    [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],  # Allen
])

# Creazione del grafico
fig, ax = plt.subplots(figsize=(12, 8))

# Creazione delle bolle
for i in range(len(autori)):
    for j in range(len(principi)):
        if dati[i, j] == 1:
            ax.scatter(j, i, s=100, color='blue', alpha=0.6)

# Etichette degli assi
ax.set_xticks(range(len(principi)))
ax.set_xticklabels(principi, rotation=45, ha="right")
ax.set_yticks(range(len(autori)))
ax.set_yticklabels(autori)

# Titolo del grafico
ax.set_title("Distribuzione dei Principi tra gli Autori")

plt.xlabel("Categories")
plt.ylabel("Papers")
# Mostrare il grafico
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
