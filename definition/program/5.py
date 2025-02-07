import matplotlib.pyplot as plt
import numpy as np

# Definizione dei principi e degli step
principles = [
    "Access and availability", "Existence and persistence", "Security and protection", "Interoperability", 
    "Ownership and control", "Persistence", "Cost", "Standard", "Usability and consistency", "Transparency", 
    "Consent", "Decentralization and Autonomy", "Privacy and minimal disclosure", "Verifiability and Authenticity", "Portability"
]

steps = list(range(1, 16))

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

# Identifica i cambiamenti tra step e step
change_points = []
for step in range(len(steps) - 1):
    for i, principle in enumerate(principles):
        if group_assignments[i][step] != group_assignments[i][step + 1]:
            change_points.append((step + 1, i))

# Visualizza i cambiamenti in un grafico
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter([x[0] for x in change_points], [x[1] for x in change_points], color='red', label='Changes')
ax.set_xticks(steps)
ax.set_yticks(range(len(principles)))
ax.set_yticklabels(principles)
ax.set_xlabel("Steps")
ax.set_ylabel("Principles")
ax.set_title("Changes in Principles Across Steps")
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Stampa i cambiamenti
changes = {}
for step in range(len(steps) - 1):
    changed_principles = []
    for i, principle in enumerate(principles):
        if group_assignments[i][step] != group_assignments[i][step + 1]:
            changed_principles.append(principle)
    changes[f"Step {steps[step]} -> Step {steps[step + 1]}"] = changed_principles

for transition, changed in changes.items():
    print(f"{transition}: {', '.join(changed) if changed else 'No changes'}")
