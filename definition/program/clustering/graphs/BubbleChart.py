import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Recreating the data from the table in the image (simplified for example)
data = {
        "Existence and persistence":    [4, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "Ownership and control":        [5, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "Consent":                      [5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        "Access and availability":      [0, 3, 0, 1, 0, 3, 0, 2, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        "Security and protection":      [0, 0, 1, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        "Persistence":                  [1, 1, 1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        "Privacy and minimal disclosure":[2, 1, 1, 0, 1, 0, 0, 4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        "Portability":                  [0, 0, 1, 0, 0, 2, 1, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 0],
        "Transparency":                 [0, 0, 0, 0, 0, 3, 3, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        "Interoperability":             [0, 0, 0, 0, 0, 3, 1, 0, 1, 2, 1, 1, 0, 0, 0, 1, 1, 0],
        "Cost":                         [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
        "Standard":                     [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
        "Decentralization and Autonomy":[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        "Verifiability and Authenticity":[0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "Usability and consistency":    [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}

categories = [
    "Controllability", "Foundational", "Personal Data", "Agency", "User",
    "Portability", "Sustainability", "Security", "Usability", "Flexibility",
    "Autonomy", "Technology", "Operability", "Zero-cost", "Acceptance", "Adoption", "Compliance", "Privacy",
]

df = pd.DataFrame(data, index=categories)

# Creating the Bubble Chart
x, y = np.meshgrid(range(df.shape[1]), range(df.shape[0]))
bubble_sizes = df.values * 100

plt.figure(figsize=(12, 6))
plt.scatter(x, y, s=bubble_sizes, alpha=0.5, c="blue")
plt.xticks(range(df.shape[1]), df.columns, rotation=45, ha="right")
plt.yticks(range(df.shape[0]), df.index)
plt.title("")
plt.xlabel("Principles")
plt.ylabel("Categories")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
