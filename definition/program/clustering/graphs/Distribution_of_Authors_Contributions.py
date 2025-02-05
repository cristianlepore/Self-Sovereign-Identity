import matplotlib.pyplot as plt
import numpy as np
import random

# Data
authors = ["Tobin and Reed", "Andrieu et al.", "Ferdous et al.", "Mühle et al.", "Gilani et al.", "Naik and Jenkins", "Sheldrake", "Toth and Kalman", "eSSIF-Lab", "ToIP", "Sovrin", "BkThDVr", "Glöckler et al.", "Pava-Díaz et al.", "Satybaldy et al.", "Stokkink and Pouwelse", "Čučko et al.", "Allen"]

categories = {
    "Controllability":  [4/10, 3/5, 1/13, 1/9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3/10, 0, 0, 3/15, 0],
    "Foundational":     [0, 0, 4/13, 0, 6/12, 0, 4/5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Personal Data":    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6/10, 0, 0, 0, 0, 0, 0],
    "Agency":           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3/11, 0, 0, 0, 0, 0, 0, 0],
    "User":             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2/9, 0, 0, 0, 0, 0],
    "Portability":      [4/10, 0, 0, 3/9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4/10, 0, 0, 0, 0],
    "Sustainability":   [0, 0, 3/13, 0, 3/12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6/15, 0],
    "Security":         [3/10, 0, 3/13, 3/9, 3/12, 0, 0, 0, 0, 0, 4/11, 0, 0, 3/10, 0, 0, 2/15, 0],
    "Usability":        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2/10, 0, 0, 0, 0, 2/15, 0],
    "Flexibility":      [0, 0, 3/13, 0, 3/12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Autonomy":         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4/11, 0, 0, 0, 0, 0, 0, 0],
    "Technology":       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3/9, 0, 0, 0, 0, 0],
    "Operability":      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3/9, 0, 0, 0, 0, 0],
    "Zero-cost":        [0, 1/5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Acceptance":       [0, 1/5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Adoption":         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6/15, 0],
    "Compliance":       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2/9, 0, 0, 0, 0],
    "Privacy":          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2/15, 0],
}

# Convert dictionary values to a NumPy array for better handling
category_values = np.array(list(categories.values()))  # Shape: (num_categories, num_authors)

# Generate x, y, and size values based on real data
x, y, sizes = [], [], []
scaling_factor = 2500  # Adjust this to control bubble sizes

for j, category in enumerate(categories.keys()):
    for i, author in enumerate(authors):
        value = category_values[j, i]  # Get value from categories
        if value > 0:  # Only plot bubbles for nonzero values
            x.append(j)
            y.append(i)
            sizes.append(value * scaling_factor)  # Scale size for better visualization

# Create bubble chart
plt.figure(figsize=(12, 8))
plt.scatter(x, y, s=sizes, alpha=1, edgecolors='black', linewidths=0.5)

plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Labels and title
plt.xticks(ticks=range(len(categories)), labels=categories.keys(), rotation=45, ha='right')
plt.yticks(ticks=range(len(authors)), labels=authors)
plt.xlabel("Categories")
plt.ylabel("Authors")
plt.title("")

# Show chart
plt.show()
