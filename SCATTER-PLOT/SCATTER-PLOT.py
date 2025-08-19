'''THIS CODE CAN BE USED TO PLOT THE SCATTER PLOT'''
##CREATED BY ER. AJAY BHATTARAI ###
import matplotlib.pyplot as plt

# ---------------- DATA ---------------- #
x = [1, 2, 3, 4, 5, 6, 7,10,15,30,24,11,65,15,18]
y = [10, 15, 7, 20, 12, 25, 18,25,30,64,51,24,84,75,95]

# ---------------- FIGURE SETTINGS ---------------- #
dpi = 120
fig_width = 10  # inches
fig_height = 6  # inches
bg_color = 'white'  # figure background

# ---------------- SCATTER SETTINGS ---------------- #
point_color = 'red'      # color of scatter points
point_size = 80          # size of scatter points
point_marker = 'o'       # marker style, e.g., 'o', 's', '^'

# ---------------- TITLE & AXIS ---------------- #
title_text = 'My Scatter Plot'
x_label = 'X Axis Label'
y_label = 'Y Axis Label'

# Fonts
title_fontsize = 20
title_fontweight = 'bold'
axis_label_fontsize = 16
tick_fontsize = 14
font_family = 'Arial'

# ---------------- GRID ---------------- #
show_grid = True
grid_color = 'grey'
grid_style = '--'
grid_alpha = 0.5

# ---------------- PLOT CREATION ---------------- #
plt.figure(figsize=(fig_width, fig_height), dpi=dpi, facecolor=bg_color)

# Scatter plot
plt.scatter(x, y, color=point_color, s=point_size, marker=point_marker)

# Titles and labels
plt.title(title_text, fontsize=title_fontsize, fontweight=title_fontweight, fontname=font_family)
plt.xlabel(x_label, fontsize=axis_label_fontsize, fontname=font_family)
plt.ylabel(y_label, fontsize=axis_label_fontsize, fontname=font_family)

# Ticks
plt.xticks(fontsize=tick_fontsize, fontname=font_family)
plt.yticks(fontsize=tick_fontsize, fontname=font_family)

# Grid
if show_grid:
    plt.grid(True, color=grid_color, linestyle=grid_style, alpha=grid_alpha)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
