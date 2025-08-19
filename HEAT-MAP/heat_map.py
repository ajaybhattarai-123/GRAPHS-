'''THIS CODE GENERALLY GENERATES THE HEAT MAP, AS SHOWN IN THE REFERENCE IMAGE '''
import matplotlib.pyplot as plt
import numpy as np

# ---------------- USER SETTINGS ---------------- #
# Example data (list of lists)
'''
data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
'''

###     TESTING      ###
# Example of very lengthy data (20x20)
data = [
    [np.random.randint(0, 100) for _ in range(20)]
    for _ in range(20)
]


### TESTING COMPLETED ###

# Figure settings
dpi = 150               # Image DPI
width = 16             # Figure width in inches
height = 10            # Figure height in inches
cmap_choice = "RdYlBu"  # Colormap: try 'viridis', 'plasma', 'coolwarm', etc.

# Font sizes
title_font = 12
xlabel_font = 10
ylabel_font = 10
xtick_font = 8
ytick_font = 8
colorbar_font = 8
# ------------------------------------------------ #

# Convert list to numpy array
data_array = np.array(data)

# Create figure
plt.figure(figsize=(width, height), dpi=dpi)

# Generate heatmap
heatmap = plt.imshow(data_array, cmap=cmap_choice, aspect='auto')

# Add colorbar
cbar = plt.colorbar(heatmap)
cbar.ax.tick_params(labelsize=colorbar_font)

# Add title and labels
plt.title("Heatmap Visualization", fontsize=title_font, fontweight='bold')
plt.xlabel("X-axis", fontsize=xlabel_font)
plt.ylabel("Y-axis", fontsize=ylabel_font)

# Customize ticks
plt.xticks(range(data_array.shape[1]), fontsize=xtick_font)
plt.yticks(range(data_array.shape[0]), fontsize=ytick_font)

# Show grid lines (optional)
plt.grid(False)

# Tight layout
plt.tight_layout()

# Show the plot
plt.show()
