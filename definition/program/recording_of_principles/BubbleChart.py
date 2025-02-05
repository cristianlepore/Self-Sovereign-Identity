import matplotlib.pyplot as plt
import numpy as np

autori = ["Tobin and Reed", "Andrieu et al.", "Ferdous et al.", "Mühle et al.", "Gilani et al.", "Naik and Jenkins", "Sheldrake", "Toth and Kalman", "eSSIF-Lab", "ToIP", "Sovrin", "BkThDVr", "Glöckler et al.", "Pava-Díaz et al.", "Satybaldy et al.", "Stokkink and Pouwelse", "Čučko et al.", "Allen"]

principi = ["Existence and Representation", "Ownership and Control", "Access and Availability", "Transparency", "Persistence", "Portability", "Interoperability", "Consent", "Security and Protection", "Privacy and Minimal Disclosure", "Standard", "Cost", "Usability and Consistency", "Decentralization and Autonomy", "Verifiability and Authenticity"]

dati = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # Tobin and Reed
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0],  # Andrieu et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],  # Ferdous et al.
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # Mühle et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],  # Gilani et al.
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],  # Naik and Jenkins
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Sheldrake
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1],  # Toth and Kalman
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0],  # eSSIF-Lab
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # ToIP
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],  # Sovrin
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # BkThDVr
    [0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],  # Glöckler et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # Pava-Díaz et al.
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],  # Satybaldy et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],  # Stokkink and Pouwelse
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Čučko et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],  # Allen
])

fig, ax = plt.subplots(figsize=(12, 8))

for i in range(len(autori)):
    for j in range(len(principi)):
        if dati[i, j] == 1:
            ax.scatter(j, i, s=100, color='blue', alpha=0.6)

ax.set_xticks(range(len(principi)))
ax.set_xticklabels(principi, rotation=45, ha="right")
ax.set_yticks(range(len(autori)))
ax.set_yticklabels(autori)

ax.set_title("")
plt.xlabel("Categories")
plt.ylabel("Authors")

plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
