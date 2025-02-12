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

# Create the bar chart
plt.figure(figsize=(12, 8))  # Set the size of the plot
plt.barh(df["Attribute"], df["Value"], color='skyblue')  # Horizontal bar chart

# Add labels and title
plt.xlabel('Entropy')
plt.ylabel('Principles')
plt.title('')

# Invert the Y-axis to display bars from top to bottom
plt.gca().invert_yaxis()

# Adjust the layout for better display
plt.tight_layout()

# Display the plot
plt.show()
