"""this code can be used to create the pie chart , use the reference image as shown"""
##CREATED BY ER. AJAY BHATTARAI ###
import matplotlib.pyplot as plt
import pandas as pd

# ------------------ User Inputs ------------------
fig_width = 16
fig_height = 10
fig_dpi = 300  # resolution

label_font_size = 6
title_font_size = 7
# -------------------------------------------------

# Data
data = {
    "Energy Source": ["Diesel", "Petrol", "Electricity", "Solar"],
    "Percentage": [30, 12, 29, 29]
}

# Create DataFrame
df = pd.DataFrame(data)

# High-contrast colors
colors = ['red', 'blue', 'green', 'orange']

# Set figure size and DPI
plt.figure(figsize=(fig_width, fig_height), dpi=fig_dpi)

# Pie chart
wedges, texts, autotexts = plt.pie(
    df["Percentage"],
    labels=df["Energy Source"],
    autopct='%1.1f%%',
    startangle=140,           ##easily change start angle
    colors=colors,
    pctdistance=0.7,
    labeldistance=1.05,
    wedgeprops={'edgecolor': 'black', 'linewidth': 0.1}          ##Enter line width to change the outer line width
)

# Customize text
for text in texts:
    text.set_fontsize(label_font_size)
    text.set_weight('bold')

for autotext in autotexts:
    autotext.set_fontsize(label_font_size)
    autotext.set_weight('bold')
    autotext.set_color('black')

# Title
plt.title("Energy Source Distribution (2023)", fontsize=title_font_size, weight='bold', family='serif')

# White background
plt.gca().set_facecolor('white')
plt.gcf().patch.set_facecolor('white')

# Equal aspect ratio ensures pie is circular
plt.axis('equal')

# Tight layout
plt.tight_layout()

# Display plot
plt.show()
