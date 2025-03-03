import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

# Definizione dei vettori Word2Vec simulati per i concetti
portability = np.array([-0.25, 0.75, 0.33, -0.12, 0.61])
trust_infra = np.array([0.42, -0.13, 0.68, 0.21, -0.33])
credential_ex = np.array([0.37, 0.81, 0.29, -0.15, 0.57])

# Calcolo della similarità coseno
similarities = cosine_similarity([portability], [trust_infra, credential_ex])[0]

# Creazione del grafico
labels = ["Trust Infrastructure", "Credential Exchange"]
scores = similarities

plt.figure(figsize=(6,4))
plt.bar(labels, scores, color=['blue', 'green'])
plt.ylim(0, 1)
plt.xlabel("ToIP Layers")
plt.ylabel("Cosine Similarity")
plt.title("Mapping della Portabilità di SSI su ToIP")
plt.show()
