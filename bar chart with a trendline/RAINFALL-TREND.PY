### CREATED AND TESTED BY ER. AJAY BHATTARAI
'''This is a bar chart with a trendline showing annual rainfall (in mm) from the year 2000 to 2023.'''
import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array(list(range(2000, 2024)))
rainfall = np.array([
    1631, 1785, 1869, 1807, 1969, 1384, 1602, 2183, 1572, 1136,
    1387, 1582, 1032, 1413, 1452, 1127, 1487, 1628, 1403, 1724,
    2035, 1991, 1447, 1222
])

# Shift years so that 2000 = 0
years_base = years - 2000

# Linear regression using shifted years
slope, intercept = np.polyfit(years_base, rainfall, 1)
y_pred = slope * years_base + intercept

# Print regression values
print(f"Slope (mm/year): {slope:.4f}")
print(f"Intercept (rainfall in 2000): {intercept:.2f}")
print(f"Predicted rainfall in 2023: {slope * (2023 - 2000) + intercept:.2f}")

# Plot
plt.figure(figsize=(3, 2), dpi=300)
plt.bar(years, rainfall, color='royalblue', width=0.5, label='Annual Rainfall (mm)')
plt.plot(years, y_pred, color='red', linestyle='--', linewidth=0.5,
         label=f'Trendline: y = {slope:.2f}×(Year0) + {intercept:.2f}')

# Legend, labels, ticks
plt.legend(fontsize=3.5, loc='upper right', bbox_to_anchor=(1, 1), borderpad=0.1)
plt.xlabel('Year', fontsize=3.5, fontweight='bold', color='black', labelpad=2)
plt.ylabel('Rainfall (mm)', fontsize=3.5, fontweight='bold', color='black', labelpad=2)
plt.xticks(np.arange(years[0], years[-1]+1, 2), rotation=45, fontsize=3.5, color='black')
plt.yticks(fontsize=3.5, color='black')
plt.title('Rainfall across Madhesh Province', fontsize=4, fontweight='bold', color='black', pad=2)
plt.tick_params(axis='both', direction='inout', length=2, width=0.3, colors='black', pad=0.2)

# Spines styling
ax = plt.gca()
for spine, style in zip(['top', 'right', 'bottom', 'left'], ['--', '-.', ':', '-']):
    ax.spines[spine].set_visible(True)
    ax.spines[spine].set_linewidth(0.2)
    ax.spines[spine].set_linestyle(style)

plt.tight_layout()
plt.show()
