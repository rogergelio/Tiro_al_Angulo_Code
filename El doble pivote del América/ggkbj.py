# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 19:03:39 2023

@author: rogel
"""
from urllib.request import urlopen
import matplotlib.pyplot as plt
from PIL import Image
from mplsoccer import PyPizza, add_image, FontManager
import pandas as pd
import numpy as np

#1) Leer datos
data=pd.read_excel("C:/Users/rogel/OneDrive/Escritorio/Tiro al Ángulo/Escritos/La chofis/Chofis.xlsx")

#2) Creando columnas de la gráfica
statistic=[]
percentile=[]

for i in range(0, len(data)):
    #2.1) llenar la columna de estadistico
    statistic.append(str(data["Statistic"][i])) #Usamos string porque son palabras
    #2.2) llenar la columna de percentil
    percentile.append(int(data["Percentile"][i])) #Usamos int porque son de los que le gustan a luis

#Sacamos la fuente
font_normal = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/roboto/'
                          'Roboto%5Bwdth,wght%5D.ttf')
font_italic = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/roboto/'
                          'Roboto-Italic%5Bwdth,wght%5D.ttf')
font_bold = FontManager('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
                        'RobotoSlab%5Bwght%5D.ttf')

#Saca la imagen del jugador
#Para hacerla circulo https://www.fotor.com/features/circle-crop/
fdj_cropped = Image.open("C:/Users/rogel/OneDrive/Escritorio/Tiro al Ángulo/Escritos/La chofis/Chofinho.png")

#Asignamos el valor a params
params=statistic
#Nos dice cuantos hay
len(statistic)
# value list
values=percentile
# color for the slices and text

#3) Le damos colores link: https://www.color-hex.com/color/ffffff
slice_colors = ["#8fce00"] * 5 + ["#6a329f"] * 5 + ["#fff2cc"] * 9
text_colors = ["#000000"] * 10 + ["#000000"] * 9

# Crea un radar vacío
baker = PyPizza(
    params=params,                  # list of parameters
    background_color="#222222",     # background color
    straight_line_color="#000000",  # color for straight lines
    straight_line_lw=1,             # linewidth for straight lines
    last_circle_color="#000000",    # color for last line
    last_circle_lw=1,               # linewidth of last circle
    other_circle_lw=0,              # linewidth for other circles
    inner_circle_size=15            # size of inner circle
)

#Agregamos datos (el corazón de luis [o su alma])
fig, ax = baker.make_pizza(
    values,                          # list of values
    figsize=(8, 10),                # adjust the figsize according to your need
    color_blank_space="same",        # use the same color to fill blank space
    slice_colors=slice_colors,       # color for individual slices
    value_colors=text_colors,        # color for the value-text
    value_bck_colors=slice_colors,   # color for the blank spaces
    blank_alpha=0.4,                 # alpha for blank-space colors
    kwargs_slices=dict(
        edgecolor="#000000", zorder=2, linewidth=1
    ),              
    #Aquí se mueven los títulos (lo que va afuera y es palabra)                
    # values to be used when plotting slices
    kwargs_params=dict(
        color="#F2F2F2", 
        fontproperties=font_normal.prop, va="center", fontsize=15,
    ),                               # values to be used when adding parameter labels
    kwargs_values=dict( #Aquí se mueven los valores (lo que va adentro y es número) 
        color="#F2F2F2", 
        fontproperties=font_normal.prop, zorder=3, fontsize=9.5,
        bbox=dict(
            edgecolor="#000000", facecolor="cornflowerblue",
            boxstyle="round,pad=0.2", lw=1
        )
    )                                # values to be used when adding parameter-values labels
)

# add title
fig.text(
    0.515, 0.975, "Chofis Lopez - Pachuca", size=16,
    ha="center", fontproperties=font_bold.prop, color="#F2F2F2"
)

# add subtitle
fig.text(
    0.515, 0.955,
    "Percentile Rank vs Top-Five League Midfielders | Season 2020-21",
    size=13,
    ha="center", fontproperties=font_bold.prop, color="#F2F2F2"
)

# Agregar valores de créditos
CREDIT_1 = "data: statsbomb viz fbref"
CREDIT_2 = "inspired by: @Worville, @FootballSlices, @somazerofc & @Soumyaj15209314"

#Meter los créditos
fig.text(
    0.99, 0.02, f"{CREDIT_1}\n{CREDIT_2}", size=9,
    fontproperties=font_italic.prop, color="#F2F2F2",
    ha="right"
)

# add text
fig.text(
    0.34, 0.93, "Attacking                 Defending                   Posession", size=14,
    fontproperties=font_bold.prop, color="#F2F2F2"
)

# add rectangles
fig.patches.extend([
    plt.Rectangle(
        (0.31, 0.9225), 0.025, 0.021, fill=True, color="#8fce00",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.462, 0.9225), 0.025, 0.021, fill=True, color="#6a329f",
        transform=fig.transFigure, figure=fig
    ),
    plt.Rectangle(
        (0.632, 0.9225), 0.025, 0.021, fill=True, color="#fff2cc",
        transform=fig.transFigure, figure=fig
    ),
])

# add image
ax_image = add_image(
    fdj_cropped, fig, left=0.4478, bottom=0.4315, width=0.13, height=0.127
)   # these values might differ when you are plotting

plt.show()