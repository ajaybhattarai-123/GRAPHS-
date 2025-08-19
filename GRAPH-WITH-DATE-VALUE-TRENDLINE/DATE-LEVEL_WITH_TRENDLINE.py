'''This code takes groundwater level data from an Excel file and makes a clear, 
good-looking graph. It shows the changes over time, adds a smooth trendline, titles,
 labels, legend, and even a light watermark with the district name plus a small note about the data source.'''
##CREATED BY ER. AJAY BHATTARAI ###
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

####This script plots groundwater levels from Excel, adds a trendline, and produces 
# a styled, labeled visualization with a watermark and data source note.###

# Set global font and style
plt.style.use('seaborn-v0_8-darkgrid')
rcParams['font.family'] = 'Segoe UI'
rcParams['axes.titleweight'] = 'bold'
rcParams['axes.labelweight'] = 'bold'

# Ask user for district and well location
district = input("Enter the district name: ").strip().title()
well_location = input("Enter the well location: ").strip().title()

# Path to your Excel file
file_path = r"C:\Users\ajayb\OneDrive - Tribhuvan University\Desktop\MADHESH-WORK\GRAPH-FOR-SIR-pc.xlsx"

# Read the sheet named 'SAPTARI'
df = pd.read_excel(file_path, sheet_name='DHANUSHA', header=None)

# Extract the dates (first row) and groundwater levels (second row)
dates = df.iloc[0].tolist()
gw_levels = df.iloc[1].tolist()

# Create figure with beautiful aesthetics
plt.figure(figsize=(16, 9), dpi=120)
ax = plt.gca()

# Set background color
fig = plt.gcf()
fig.set_facecolor('#f5f5f5')
ax.set_facecolor('#ffffff')

# Main plot with reduced line thickness and no value labels
main_line, = plt.plot(dates, gw_levels, 
                     marker='o', 
                     markersize=6,
                     markerfacecolor='white',
                     markeredgewidth=1.5,
                     linestyle='-', 
                     linewidth=1.5,
                     color='#3498db', 
                     alpha=0.9,
                     label=f'{well_location} (Observed)')

# Calculate and plot CONTINUOUS trendline (modified part)
x_numeric = np.arange(len(dates))
y = np.array(gw_levels)
coefficients = np.polyfit(x_numeric, y, 1)
poly_eqn = np.poly1d(coefficients)
# Generate more points for smoother line
x_continuous = np.linspace(min(x_numeric), max(x_numeric), 500)
trendline = poly_eqn(x_continuous)
# Convert back to dates for plotting
date_range = pd.date_range(start=dates[0], end=dates[-1], periods=500)

trend_line, = plt.plot(date_range, trendline, 
                      color='#e74c3c', 
                      linestyle='-',  # Changed from '--' to '-' for solid line
                      linewidth=1.8,  # Slightly thicker for visibility
                      alpha=0.8,
                      label='Trendline')

# Rest of your original code remains exactly the same...
# Add title and labels with enhanced styling
plt.title(f'Groundwater Level Monitoring\nDistrict: {district} | Location: {well_location}', 
          fontsize=16, pad=20, color='#2c3e50')
plt.xlabel('Year', fontsize=14, labelpad=10, color='#34495e')
plt.ylabel('Groundwater Level', fontsize=14, labelpad=10, color='#34495e')

# Customize ticks
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# Add grid customization
ax.grid(which='major', linestyle='-', linewidth='0.5', color='#d4d4d4')
ax.grid(which='minor', linestyle=':', linewidth='0.5', color='#e6e6e6')
ax.minorticks_on()

# Customize legend
legend = plt.legend(framealpha=1, 
                    facecolor='white', 
                    edgecolor='#bdc3c7',
                    fontsize=12,
                    loc='best',
                    shadow=True)
legend.get_frame().set_linewidth(1.5)

# Add a subtle watermark
plt.text(0.5, 0.5, district, 
         transform=ax.transAxes,
         fontsize=120, color='#f0f0f0',
         ha='center', va='center', alpha=0.2,
         zorder=-1)

# Customize spines
for spine in ax.spines.values():
    spine.set_color('#bdc3c7')
    spine.set_linewidth(1.5)

# Adjust layout
plt.tight_layout(pad=3)

# Add footer note
plt.figtext(0.5, 0.01, "Data Source: Groundwater Resource and Development Board | Visualization by Ajay Bhattarai", 
            ha="center", fontsize=10, color="#7f8c8d")

plt.show()