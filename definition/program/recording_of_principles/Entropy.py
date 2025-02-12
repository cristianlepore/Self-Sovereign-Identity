import matplotlib.pyplot as plt
import pandas as pd

# Data for the table
data = {
    "Attribute": [
        "Existence and representation", "Ownership and control", "Access and availability", 
        "Transparency", "Persistence", "Portability", "Interoperability", "Consent", 
        "Security and protection", "Privacy and minimal disclosure", "Standard", "Cost", 
        "Usability and Consistency", "Decentralization and Autonomy", "Verifiability and Authenticity", 
        "Self-generatable and independent", "Opt-in", "Opt-out", "Simple", "Non-repudiatable", 
        "Reliable", "Equivalent", "Single Source", "Validity", "Freedom Information", "Auditability", 
        "Integrity", "Effectiveness", "Efficiency", "Manageability", "Trust", "Scalable", 
        "Equity and Inclusion", "Delegation"
    ],
    "Value": [
        0.92, 0.50, 0.50, 0.85, 0.65, 0.65, 0.86, 0.50, 0.50, 0.19, 0.85, 0.92, 0.92, 0.85, 0.92, 
        0.23, 0.23, 0.23, 0.50, 0.23, 0.23, 0.50, 0.50, 0.23, 0.23, 0.23, 0.23, 0.23, 0.23, 0.23, 
        0.50, 0.65, 0.23, 0.23
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a figure and axis to display the table
fig, ax = plt.subplots(figsize=(10, 8))  # Size of the image
ax.axis('tight')  # Disable axis
ax.axis('off')  # Disable axis labels

# Create the table
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', colColours=['#f1f1f1']*2)

# Display the table
plt.show()
