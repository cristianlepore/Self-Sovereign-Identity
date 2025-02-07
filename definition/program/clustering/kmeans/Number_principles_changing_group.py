import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data for first chart: number of clusters per step
steps = np.array(list(range(1, 16)))
group_counts_clusters = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

# Data for second chart: principles changing group
group_counts_principles = np.array([12, 3, 6, 1, 2, 2, 6, 1, 1, 1, 1, 1, 1, 1, 1])

# Generate smooth curve using cubic spline interpolation for the second dataset
smooth_steps = np.linspace(steps.min(), steps.max(), 300)  # More points for smoothness
spline = make_interp_spline(steps, group_counts_principles, k=3)  # k=3 for cubic smoothing
smooth_counts = spline(smooth_steps)

# Create the combined plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot first dataset (clusters per step)
ax.plot(steps, group_counts_clusters, marker='o', linestyle='-', color='b', label='Number of Clusters')

# Plot second dataset (principles changing group) with smooth curve
ax.plot(smooth_steps, smooth_counts, linestyle='-', color='r', label='Principles that changed group')
ax.scatter(steps, group_counts_principles, color='r', marker='o') 

# Customize the plot
ax.set_xlabel('Values of the parameter k', fontsize=14)
ax.set_ylabel('Count', fontsize=14)
ax.set_xticks(steps)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()
