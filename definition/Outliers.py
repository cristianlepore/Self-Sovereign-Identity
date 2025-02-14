import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from sklearn.cluster import DBSCAN

# Data Setup
autori = ["Tobin and Reed", "Andrieu et al.", "Ferdous et al.", "Mühle et al.", "Gilani et al.",
          "Naik and Jenkins", "Toth and Kalman", "eSSIF-Lab", "ToIP", "Sovrin",
          "BkThDVr", "Pava-Díaz et al.", "Satybaldy et al.",
          "Stokkink and Pouwelse", "Čučko et al.", "Allen"]

principi = ["Existence and representation", "Ownership and control", "Access and availability",
            "Transparency", "Persistence", "Portability", "Interoperability", "Consent",
            "Security and protection", "Privacy and minimal disclosure", "Standard", "Cost",
            "Usability and Consistency", "Decentralization and Autonomy",
            "Verifiability and Authenticity", "Self-generatable and independent", "Opt-in",
            "Opt-out", "Simple", "Non-repudiatable", "Reliable", "Equivalent", "Single Source",
            "Validity", "Freedom Information", "Auditability", "Integrity", "Effectiveness",
            "Efficiency", "Manageability", "Trust", "Scalable", "Equity and Inclusion",
            "Delegation"]

dati = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Tobin and Reed
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Andrieu et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Ferdous et al.
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Mühle et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Gilani et al.
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # Naik and Jenkins
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Toth and Kalman
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # eSSIF-Lab
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # ToIP
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],  # Sovrin
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # BkThDVr
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Pava-Díaz et al.
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],  # Satybaldy et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Stokkink and Pouwelse
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Čučko et al.
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Allen
])

# Convert to DataFrame
df = pd.DataFrame(dati, index=autori, columns=principi)

# Count occurrences of each principle (i.e., sum each column)
principle_counts = df.sum(axis=0).to_frame(name="Author_Count")

# 1 Z-Score Method
principle_counts["Z_Score"] = zscore(principle_counts["Author_Count"])
z_threshold = 2  # Change to 1.5 for a more sensitive detection
outliers_z = principle_counts[abs(principle_counts["Z_Score"]) > z_threshold]

# 2️ IQR Method
Q1 = principle_counts["Author_Count"].quantile(0.25)
Q3 = principle_counts["Author_Count"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_iqr = principle_counts[(principle_counts["Author_Count"] < lower_bound) |
                                (principle_counts["Author_Count"] > upper_bound)]

# 3️ DBSCAN Clustering
dbscan = DBSCAN(eps=3, min_samples=2)  # Adjust `eps` for better clustering
principle_counts["DBSCAN_Label"] = dbscan.fit_predict(principle_counts[["Author_Count"]])
outliers_dbscan = principle_counts[principle_counts["DBSCAN_Label"] == -1]

# Print Outliers
print("📌 Outliers (Z-Score):\n", outliers_z)
print("📌 Outliers (IQR Method):\n", outliers_iqr)
print("📌 Outliers (DBSCAN Clustering):\n", outliers_dbscan)

# Visualization

# Boxplot for Principle Mentions
plt.figure(figsize=(10, 5))
sns.boxplot(data=principle_counts["Author_Count"])
plt.title("Distribution of Principles Mentioned by Authors")
plt.ylabel("Number of Authors Mentioning the Principle")
plt.show()

# Z-score Outliers Scatter Plot
plt.figure(figsize=(12, 6))
sns.scatterplot(x=principle_counts.index, y=principle_counts["Author_Count"],
                hue=abs(principle_counts["Z_Score"]) > z_threshold, palette={True: "red", False: "blue"}, s=100)
plt.xticks(rotation=90)
plt.title("Z-Score Outliers (Red Indicates Outliers)")
plt.ylabel("Number of Authors")
plt.xlabel("Principles")
plt.show()

# IQR Outliers Scatter Plot
plt.figure(figsize=(12, 6))
sns.scatterplot(x=principle_counts.index, y=principle_counts["Author_Count"],
                hue=(principle_counts["Author_Count"] < lower_bound) | (principle_counts["Author_Count"] > upper_bound),
                palette={True: "red", False: "blue"}, s=100)
plt.xticks(rotation=90)
plt.title("IQR Outliers (Red Indicates Outliers)")
plt.ylabel("Number of Authors")
plt.xlabel("Principles")
plt.show()

#  DBSCAN Clustering Scatter Plot
plt.figure(figsize=(12, 6))
sns.scatterplot(x=principle_counts.index, y=principle_counts["Author_Count"],
                hue=principle_counts["DBSCAN_Label"], palette="coolwarm", s=100)
plt.xticks(rotation=90)
plt.title("Principle Occurrences (DBSCAN Outliers in Red)")
plt.ylabel("Number of Authors")
plt.xlabel("Principles")
plt.show()
