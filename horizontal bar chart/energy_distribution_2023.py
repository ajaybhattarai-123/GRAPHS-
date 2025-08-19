import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ------------------ User Configurable Parameters ------------------
fig_width = 8       # figure width in inches
fig_height = 6      # figure height in inches
fig_dpi = 300       # resolution for publication

# Font settings (user can set different fonts for each element)
title_font = {'family': 'serif', 'size': 10, 'weight': 'bold', 'color': 'black'}
xlabel_font = {'family': 'sans-serif', 'size': 8, 'weight': 'bold'}
ylabel_font = {'family': 'monospace', 'size': 8, 'weight': 'bold'}
tick_font = {'family': 'serif', 'size': 6}
bar_label_font = {'family': 'sans-serif', 'size': 6, 'weight': 'bold', 'color': 'black'}
# -----------------------------------------------------------------

# Data
data = {
    "Energy Source": ["Diesel", "Petrol", "Electricity", "Solar"],
    "Percentage": [75.77, 1.22, 22.5, 0.51]
}

# Create DataFrame
df = pd.DataFrame(data)
df = df.sort_values(by="Percentage", ascending=True)

# Set figure size and DPI
plt.figure(figsize=(fig_width, fig_height), dpi=fig_dpi)

# Color palette
colors = sns.color_palette("Spectral", len(df))

# Horizontal bar plot
bars = plt.barh(df["Energy Source"], df["Percentage"], color=colors, edgecolor='black', height=0.6)

# Add percentage labels
for bar in bars:
    width_bar = bar.get_width()
    plt.text(width_bar + 0.5, bar.get_y() + bar.get_height()/2,
             f'{width_bar:.2f}%', va='center', **bar_label_font)

# Labels and title
plt.xlabel("Share of Energy Sources (%)", **xlabel_font)
plt.ylabel("Energy Source", **ylabel_font)
plt.title("Energy Source Distribution (2023)", **title_font)

# Customize tick labels
plt.xticks(fontsize=tick_font['size'], family=tick_font['family'])
plt.yticks(fontsize=tick_font['size'], family=tick_font['family'])

# Gridlines for clarity
plt.grid(axis='x', linestyle='--', alpha=0.6)

# White background
plt.gca().set_facecolor('white')
plt.gcf().patch.set_facecolor('white')

# Remove top and right spines
sns.despine(left=True, bottom=False)

# Adjust x-axis limit for space for labels
plt.xlim(0, max(df["Percentage"])*1.15)

# Tight layout
plt.tight_layout()

# Display plot
plt.show()
