import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creazione dei dati
data = {
    "25th": [
        "Existence and persistence", "Ownership and control", "Access and availability", 
        "Decentralization and Autonomy", "Persistence", "Portability", "Interoperability", 
        "Verifiability and authenticity", "Consent", "Security and protection", 
        "Privacy and minimal disclosure", "Cost", "Standard", "Usability and consistency", 
        "Transparency"
    ],
    "50th": [
        "Existence and persistence", "Ownership and control", "Access and availability", 
        "Decentralization and Autonomy", "Usability and consistency", "Transparency", "Portability", 
        "Consent", "Security and protection", "Privacy and minimal disclosure", 
        "Verifiability and authenticity", "Interoperability", "Persistence", "Cost", "Standard"
    ],
    "75th": [
        "Existence and persistence", "Ownership and control", "Access and availability", 
        "Transparency", "Portability", "Interoperability", "Consent", "Cost", "Standard", 
        "Decentralization and Autonomy", "Verifiability and authenticity", "Usability and consistency", 
        "Security and protection", "Privacy and minimal disclosure", "Persistence"
    ]
}

# Creazione del DataFrame
df = pd.DataFrame.from_dict(data, orient='index').transpose()

# Creazione della figura
plt.figure(figsize=(10, 6))
ax = plt.gca()

# Creazione della tabella grafica con colori
colors = sns.color_palette("pastel", len(df))
cell_colors = [[colors[i]] * len(df.columns) for i in range(len(df))]

ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', 
                 cellColours=cell_colors)

# Mostra l'immagine
table.auto_set_font_size(False)
table.set_fontsize(10)
plt.show()
