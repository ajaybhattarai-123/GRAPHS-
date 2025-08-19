'''THIS CODE CAN BE USED TO CREATE THE TIME SERIES GRAPH AS SHOWN IN THE SAMPLE IMAGE'''
##CREATED BY ER. AJAY BHATTARAI ###
import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
                  2008, 2009, 2010, 2011, 2012,2013, 2015])
recharge = np.array([1.43, 2.12, 1.29, 1.74, 1.67, 1.94, 2.16, 2.08,
                     1.91, 1.83, 1.29, 1.18, 1.27, 0.86,1.59])

# Fit a linear trendline
z = np.polyfit(years, recharge, 1)
p = np.poly1d(z)
trendline = p(years)

# Create figure
plt.figure(figsize=(6, 4), dpi=300)
ax = plt.gca()

# Background and grid
ax.set_facecolor('#fefcfb')
plt.grid(True, linestyle=':', linewidth=0.4, color='gray', alpha=0.3)

# Line plot
plt.plot(years, recharge, color='#d7263d', linewidth=1.5, linestyle='-', label='(GWL)max-(GWL)min', zorder=3)

# Trendline
plt.plot(years, trendline, color='#007f5f', linestyle='--', linewidth=1, label='Trendline', zorder=2)

# Gradient-like marker colors
colors = plt.cm.viridis((recharge - min(recharge)) / (max(recharge) - min(recharge)))
plt.scatter(years, recharge, color=colors, edgecolor='black', s=35, linewidth=0.4, zorder=4)

# Annotate
for x, y in zip(years, recharge):
    plt.text(x, y + 0.05, f'{y:.2f}', ha='center', va='bottom', fontsize=4.5, color='#333333')

# Title and labels
plt.title('Temporal Change in Difference of Max-GWL and Min GWL|Madhesh province', fontsize=6.5, fontweight='bold', color='#102542', pad=6)
plt.xlabel('Year', fontsize=5.5, fontweight='bold', color='black')
plt.ylabel('Difference of Max-GWL vs Min-GWL', fontsize=5.5, fontweight='bold', color='black')

# Ticks
plt.xticks(years, fontsize=4.5, color='#222222', rotation=30)
plt.yticks(fontsize=4.5, color='#222222')

# Spines
for spine in ax.spines.values():
    spine.set_linewidth(0.25)
    spine.set_color('#999999')

# Legend
plt.legend(fontsize=4.5, loc='upper right', frameon=False)

# Tight layout
plt.tight_layout()
plt.show()
