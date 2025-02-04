import matplotlib.pyplot as plt
import numpy as np

# Data
concepts = [
    "Controllability", "Foundational", "Personal Data", "Agency", "User",
    "Portability", "Sustainability", "Security", "Usability", "Flexibility",
    "Autonomy", "Technology", "Operability", "Zero-cost", "Acceptance", "Adoption", "Compliance", "Privacy"
]

# Occurrence of unique principles (right side)
principles = np.array([7, 7, 6, 3, 2, 4, 5, 5, 5, 3, 4, 3, 3, 1, 1, 6, 2, 1])

# Occurrence of unique articles (left side, but positive values)
articles = np.array([6, 5, 1, 2, 1, 5, 7, 8, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1])

# Indices for the Y-axis
y = np.arange(len(concepts))

plt.figure(figsize=(12, 8))

# Horizontal bars (bidirectional with positive values)
bars1 = plt.barh(y, principles, color='skyblue', edgecolor='black', label="Unique principles", height=0.6)
bars2 = plt.barh(y, -articles, color='salmon', edgecolor='black', label="Unique articles", height=0.6)  # Flipping direction

# Add dashed grid lines for each row
for i in y:
    plt.axhline(i, color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Add value labels inside bars (without bold)
for bar in bars1:
    plt.text(bar.get_width() - 0.5, bar.get_y() + bar.get_height()/2, str(int(bar.get_width())), 
             va='center', ha='right', fontsize=10, color='black')

for bar in bars2:
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, str(abs(int(bar.get_width()))), 
             va='center', ha='left', fontsize=10, color='black')

# Labels and title
plt.xlabel("")  # Remove X-axis label
plt.ylabel("Categories")
plt.title("Number of occurrences")
plt.yticks(y, concepts)
plt.xticks([])  # Remove X-axis numbers
plt.axvline(0, color='black', linewidth=1)  # Vertical reference line at 0
plt.legend()
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show the chart
plt.show()
