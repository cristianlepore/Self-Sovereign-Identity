import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dati basati sulla prima immagine
principles = [
    "Access and availability", "Existence and persistence", "Security and protection", "Interoperability", "Ownership and control", "Persistence", "Cost", "Standard", "Usability and consistency", "Transparency", "Consent", "Decentralization and Autonomy", "Privacy and minimal disclosure",
    "Verifiability and Authenticity", "Portability"
]

steps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Valori del gruppo a cui ogni principio appartiene in ogni step (estratti dalla tabella della prima immagine)
group_assignments = [
    [0,1,1,3,4,4,4,4,4,4,4,4,4,4,4],  # Access and availability
    [0,1,2,2,2,2,2,2,2,2,2,2,2,2,2],  # Existence and persistence
    [0,0,0,0,0,0,0,7,7,7,7,7,7,7,7],  # Security and protection
    [0,1,1,3,3,5,5,3,3,3,3,3,3,13,13], # Interoperability
    [0,1,2,2,2,2,2,2,2,2,2,2,12,12,12], # Ownership and control
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # Persistence
    [0,1,1,3,3,3,6,5,5,5,5,5,5,5,5],  # Cost
    [0,1,1,3,3,3,6,5,5,5,5,5,5,5,14],  # Standard
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],  # Usability and consistency
    [0,1,1,3,3,3,3,6,6,6,6,6,6,6,6],  # Transparency
    [0,1,2,2,2,2,2,2,2,2,10,10,10,10,10],  # Consent
    [0,1,1,1,1,1,1,1,8,8,8,8,8,8,8],  # Decentralization and Autonomy
    [0,0,0,0,0,0,0,0,0,0,0,11,11,11,11],  # Privacy and minimal disclosure
    [0,1,1,1,1,1,1,1,1,9,9,9,9,9,9],  # Verifiability and Authenticity
    [0,1,1,3,3,5,5,3,3,3,3,3,3,3,3]  # Portability
]

# Creazione del grafico
fig, ax = plt.subplots(figsize=(15, 10))
for i, principle in enumerate(principles):
    ax.plot(steps, group_assignments[i], marker="o", label=principle, alpha=0.8, linewidth=2)

# Personalizzazione
ax.set_title("Group Assignment of Principles Across Steps", fontsize=16, weight='bold')
ax.set_xlabel("Steps", fontsize=14)
ax.set_ylabel("Group", fontsize=14)
ax.set_xticks(steps)
ax.set_yticks(range(0, 15))
ax.grid(visible=True, alpha=0.3)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()
