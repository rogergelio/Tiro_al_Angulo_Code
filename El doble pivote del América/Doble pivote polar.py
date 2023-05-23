# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 08:04:54 2023

@author: rogel
"""

#Importamos cosas
import matplotlib.pyplot as plt
from highlight_text import fig_text
import numpy as np
import pandas as pd
from mplsoccer import Radar, FontManager, grid, PyPizza, FontManager
import matplotlib.pyplot as plt

#Cargamos tipos de letras
font_normal = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/roboto/'
                          'Roboto%5Bwdth,wght%5D.ttf')
font_italic = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/roboto/'
                          'Roboto-Italic%5Bwdth,wght%5D.ttf')
font_bold = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
                        'RobotoSlab%5Bwght%5D.ttf')

#Importar datos
datos=pd.read_excel("C:/Users/rogel/OneDrive\Escritorio/Tiro al Ángulo/Escritos/El doble pivote del América/Richard V.S Fidalgo.xlsx")
datos.sort_values(by=['Statistic'])
datos
datos.sort_values(by=['Tipo'])
datos
params=[]
fidalgo=[]
richard=[]
for i in range(0,len(datos["Estadístico"])):
    params.append(datos["Estadístico"][i])
    fidalgo.append(int(datos["Percentil Fidalgo"][i]))
    richard.append(int(datos["Percentil Richard"][i]))

# pass True in that parameter-index whose values are to be adjusted
# here True values are passed for "\nTouches\nper Turnover" and "pAdj\nPress Regains" params
params_offset = [
    False, False, False, False, False, False,
    False, False, False, False, False, False,
    False, False, False, False, False, False, False
]

slice_colors = ["#1A78CF"] * 5 + ["#FF9300"] * 9 + ["#D70232"] * 5

# instantiate PyPizza class
baker = PyPizza(
    params=params,                  # list of parameters
    background_color="#000000",     # background color
    straight_line_color="#000000",  # color for straight lines
    straight_line_lw=1.5,             # linewidth for straight lines
    last_circle_lw=1,               # linewidth of last circle
    last_circle_color="#ffffff",    # color of last circle
    other_circle_ls="-.",           # linestyle for other circles
    other_circle_lw=1               # linewidth for other circles
)

# plot pizza
fig, ax = baker.make_pizza(
    fidalgo,                     # list of values
    compare_values=richard,    # comparison values
    figsize=(10, 12),             # adjust figsize according to your need
    color_blank_space=slice_colors,
    blank_alpha=0.25,                 # alpha for blank-space colors
    kwargs_slices=dict(
        facecolor="#eaec5f", edgecolor="#222222",
        zorder=2, linewidth=1
    ),                          # values to be used when plotting slices
    kwargs_compare=dict(
        facecolor="#1a4a88", edgecolor="#222222",
        zorder=2, linewidth=1,
    ),
    kwargs_params=dict(
        color="#ffffff", fontsize=14,
        fontproperties=font_normal.prop, va="center"
    ),                          # values to be used when adding parameter
    kwargs_values=dict(
        color="#000000", fontsize=14,
        fontproperties=font_normal.prop, zorder=3,
        bbox=dict(
            edgecolor="#000000", facecolor="#eaec5f",
            boxstyle="round,pad=0.2", lw=1
        )
    ),                          # values to be used when adding parameter-values labels
    kwargs_compare_values=dict(
        color="#ffffff", fontsize=12, fontproperties=font_normal.prop, zorder=3,
        bbox=dict(edgecolor="#ffffff", facecolor="#1a4a88", boxstyle="round,pad=0.2", lw=1)
    ),                          # values to be used when adding parameter-values labels
)


# adjust text for comparison-values-text
baker.adjust_texts(params_offset, offset=-0.17, adj_comp_values=True)

# add title
fig_text(
    0.515, 0.9, "<Álvaro Fidalgo > vs < Richard Sánchez>", size=20, fig=fig,
    highlight_textprops=[{"color": '#eaec5f'}, {"color": '#1a4a88'}],
    ha="center", fontproperties=font_bold.prop, color="#ffffff"
)

# add subtitle
fig.text(
    0.515, 0.922,
    "Rangos Percentiles",
    ha="center", fontproperties=font_bold.prop, color="#ffffff", size=25,
)

# add credits
CREDIT_1 = "Rogelio Torres"
CREDIT_2 = "Tiro al Ángulo"

fig.text(
    0.99, 0.005, f"{CREDIT_1}\n{CREDIT_2}", size=15,
    fontproperties=font_italic.prop, color="#ffffff",
    ha="right"
)

# add text
fig.text(
    0.34, 0.075, "   Ataque                      Defensa                         Posesión", 
    fontproperties=font_bold.prop, color="#ffffff", size=12
)

# add rectangles
fig.patches.extend([
    plt.Rectangle(
        (0.31, 0.07), 0.025, 0.021, fill=True, color="#1A78CF",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.462, 0.07), 0.025, 0.021, fill=True, color="#D70232",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.632, 0.07), 0.025, 0.021, fill=True, color="#FF9300",
        transform=fig.transFigure, figure=fig
    ),
])
slice_colors = ["#1A78CF"] * 5 + ["#FF9300"] * 9 + ["#D70232"] * 5
plt.show()