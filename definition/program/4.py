import matplotlib.pyplot as plt

# Dati
steps = list(range(0, 14 + 1))
group_counts = [0, 12, 3, 6, 1, 2, 2, 6, 1, 1, 1, 1, 1, 1, 1]

# Creazione del grafico
plt.figure(figsize=(8, 5))
plt.plot(steps, group_counts, marker='o', linestyle='-', color='b', label='Cambiamenti per step')

# Etichette e titolo
plt.xlabel('Step')
plt.ylabel('Numero di cambiamenti')
plt.title('Variazioni tra colonne consecutive')
plt.xticks(steps)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Mostra il grafico
plt.show()
