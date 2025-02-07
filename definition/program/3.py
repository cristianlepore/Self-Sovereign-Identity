import matplotlib.pyplot as plt

# Dati: numero di gruppi per ogni step
steps = list(range(1, 16))
group_counts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Creazione del grafico
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(steps, group_counts, marker='o', linestyle='-', color='b', label='Numero di Gruppi')

# Personalizzazione del grafico
ax.set_title('Numero di Gruppi per Step', fontsize=16)
ax.set_xlabel('Steps', fontsize=14)
ax.set_ylabel('Numero di Gruppi', fontsize=14)
ax.set_xticks(steps)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(fontsize=12)

# Mostra il grafico
plt.tight_layout()
plt.show()
