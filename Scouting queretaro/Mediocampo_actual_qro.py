# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:46:54 2023

@author: rogel
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 16:27:28 2023

@author: rogel
"""

#Importar librerias
import numpy as np
import pandas as pd
from mplsoccer import Radar, FontManager, grid
import matplotlib.pyplot as plt

#Importar datos
datos=pd.read_excel("C:/Users/rogel/OneDrive/Escritorio/Tiro al Ángulo/Escritos/Scouting queretaro/Jugadores/Comparacion.xlsx")
params=[]
jh=[]
ke=[]
rl=[]
fs=[]
for i in range(0,len(datos["Statistic"])):
    params.append(datos["Statistic"][i])
    jh.append(int(datos["Percentile Jorge Hernandez"][i]))
    ke.append(int(datos["Percentile Kevin Escamilla"][i]))
    rl.append(int(datos["Percentile Rodrigo López"][i]))
    fs.append(int(datos["Percentile Fernando"][i]))
    
#Add data

# The lower and upper boundaries for the statistics
low =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
high = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
len(high)

lower_is_better = [] #Flips statistic

#Instanciar radar
radar = Radar(params, low, high,
              lower_is_better=lower_is_better,
              # whether to round any of the labels to integers instead of decimal places
              round_int=[False]*len(params),
              num_rings=5,  # the number of concentric circles (excluding center circle)
              # if the ring_width is more than the center_circle_radius then
              # the center circle radius will be wider than the width of the concentric circles
              ring_width=1, center_circle_radius=1)

#Fuentes
URL1 = ('https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/'
        'SourceSerifPro-Regular.ttf')
serif_regular = FontManager(URL1)
URL2 = ('https://raw.githubusercontent.com/googlefonts/SourceSerifProGFVersion/main/fonts/'
        'SourceSerifPro-ExtraLight.ttf')
serif_extra_light = FontManager(URL2)
URL3 = ('https://raw.githubusercontent.com/google/fonts/main/ofl/rubikmonoone/'
        'RubikMonoOne-Regular.ttf')
rubik_regular = FontManager(URL3)
URL4 = 'https://raw.githubusercontent.com/googlefonts/roboto/main/src/hinted/Roboto-Thin.ttf'
robotto_thin = FontManager(URL4)
URL5 = ('https://raw.githubusercontent.com/google/fonts/main/apache/robotoslab/'
        'RobotoSlab%5Bwght%5D.ttf')
robotto_bold = FontManager(URL5)

#Valores de jugadores

#3 jugadores con titulos
# creating the figure using the grid function from mplsoccer:

fig, axs = grid(figheight=12, grid_height=0.915, title_height=0.06, endnote_height=0.025,
                title_space=0, endnote_space=0, grid_key='radar', axis=False)
# plot radar
fig.set_facecolor('#070707')    
radar.setup_axis(ax=axs['radar'], facecolor='None')  # format axis as a radar
rings_inner = radar.draw_circles(ax=axs['radar'], facecolor='#444444', edgecolor='#0d0d0d')
radar_output = radar.draw_radar_compare(jh, ke, ax=axs['radar'],
                                        kwargs_radar={'facecolor': '#def200', 'alpha': 0.6},
                                        kwargs_compare={'facecolor': '#0404d8', 'alpha': 0.6})
                                                        
radar3, vertices3 = radar.draw_radar_solid(rl, ax=axs["radar"],
                                           kwargs={'facecolor': '#bd1717',
                                                   'alpha': 0.6,
                                                   'edgecolor': '#d47474',
                                                   'lw': 1})
radar_poly, radar_poly2, vertices1, vertices2 = radar_output
range_labels = radar.draw_range_labels(ax=axs['radar'], fontsize=10,color='#ffffff')
param_labels = radar.draw_param_labels(ax=axs['radar'], fontsize=15,color='#ffffff')

# adding the endnote and title text (these axes range from 0-1, i.e. 0, 0 is the bottom left)
# Note we are slightly offsetting the text from the edges by 0.01 (1%, e.g. 0.99)
endnote_text = axs['endnote'].text(0.99, 0.5, 'Rogelio Torres | Sanje Analytica', 
                                   fontproperties=robotto_thin.prop, ha='right', va='center', fontsize=15, color="#ffffff")
title1_text = axs['title'].text(0.01, 0.85, 'Jorge Hernández',  color='#def200',
                                fontproperties=robotto_bold.prop, ha='left', va='center', fontsize=25)
title2_text = axs['title'].text(0.01, 0.25, 'Querétaro', 
                                fontproperties=robotto_thin.prop,
                                ha='left', va='center', color='#def200', fontsize=20,)
title3_text = axs['title'].text(0.99, 0.85, 'Kevin Escamilla', 
                                fontproperties=robotto_bold.prop,
                                ha='right', va='center', color='#5e5eff',fontsize=25)
title4_text = axs['title'].text(0.99, 0.25, 'Querétaro', 
                                fontproperties=robotto_thin.prop,
                                ha='right', va='center', color='#5e5eff', fontsize=20)
title5_text = axs['title'].text(0.6, 0.85, 'Rodrigo López', 
                                fontproperties=robotto_bold.prop,
                                ha='right', va='center', color='#bd1717',fontsize=25)
title6_text = axs['title'].text(0.55, 0.25, 'Querétaro', 
                                fontproperties=robotto_thin.prop,
                                ha='right', va='center', color='#bd1717', fontsize=20)
fig
