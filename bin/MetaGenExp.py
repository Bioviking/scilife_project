# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:11:55 2017

@author: Admin
"""

from collections import OrderedDict
from math import log, sqrt

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from six.moves import cStringIO as StringIO

from bokeh.plotting import figure, show, output_file

file3 = '../data/ryno_project/LMO_time_series_Metadata_to_Barbel_mod.txt'

'''
antibiotics = """
bacteria,                        penicillin, streptomycin, neomycin, gram
Mycobacterium tuberculosis,      800,        5,            2,        negative
Salmonella schottmuelleri,       10,         0.8,          0.09,     negative
Proteus vulgaris,                3,          0.1,          0.1,      negative
Klebsiella pneumoniae,           850,        1.2,          1,        negative
Brucella abortus,                1,          2,            0.02,     negative
Pseudomonas aeruginosa,          850,        2,            0.4,      negative
Escherichia coli,                100,        0.4,          0.1,      negative
Salmonella (Eberthella) typhosa, 1,          0.4,          0.008,    negative
Aerobacter aerogenes,            870,        1,            1.6,      negative
Brucella antracis,               0.001,      0.01,         0.007,    positive
Streptococcus fecalis,           1,          1,            0.1,      positive
Staphylococcus aureus,           0.03,       0.03,         0.001,    positive
Staphylococcus albus,            0.007,      0.1,          0.001,    positive
Streptococcus hemolyticus,       0.001,      14,           10,       positive
Streptococcus viridans,          0.005,      10,           40,       positive
Diplococcus pneumoniae,          0.005,      11,           10,       positive
"""
'''
drug_color = OrderedDict([
    ("Penicillin",   "#0d3362"),
    ("Streptomycin", "#c64737"),
    ("Neomycin",     "black"  ),
])

gram_color = {
    "positive" : "#aeaeb8",
    "negative" : "#e69584",
}
'''
df = pd.read_csv(StringIO(antibiotics),
                 skiprows=1,
                 skipinitialspace=True,
                 engine='python')
'''

#Parsing on the Year Month and Day Columns. To get the correct Date format.
df = pd.read_table(file3, parse_dates=[[2, 3, 4]],index_col='Year_Month_Day' ) #,parse_dates=[] index_col='Date'
#print(df.head())
print(df.info())



###################################Full Dataset###############
#Removing the redunant Date column as it is not the correct format
df1 = df.iloc[:,2::]
print(df1.head(50))
print(df1.info())



#Parsing on the Date column. Some of the dates have the wrong format
#df1 = df.iloc[:,4::]
#print(df1.head())
'''
df1.plot(kind='box', subplots= True)
plt.show()
plt.clf()
'''





####################################TEMPERATURE###################
#Resampled and using the Year_Month_Day column
df1['Temperature'].resample('2M').mean().plot()
plt.title('Temperature vs Time')
plt.xlabel('Time (Year_Month_Day)')
plt.ylabel('Temperature (C)')
plt.tight_layout()
plt.savefig('../results/plots/2017-08-16/temperatureplot01.png')
plt.show()
plt.clf()


###################################Salinity#######################
##month period with NaN from 2011-07 to 2011-10-05
#No salinity records for 2012-02, 2013-03,

#print(df1['Salinity'].info())
#print(df1['Salinity'].head())

################Display missing Data
#df1['Salinity'].loc['2011-04': '2011-10'].plot()
#df1['Salinity'].loc['2012-04': '2012-10'].plot()
#print(df1['Salinity'].loc['2012-04': '2012-10'])
#plt.show()
#plt.clf()

salty_time= df1['Salinity']['2011-03-25':'2014-08-20']
print(salty_time)

salty_timeb= salty_time.resample('W').mean().interpolate(how='linear')
twoweeks_max= salty_timeb.resample('M').mean().interpolate(how='linear')
print(twoweeks_max)
sm_twoweekff= twoweeks_max.rolling(window=1).mean()
sm_twoweekff.plot()

plt.title('Salinity vs Time - Forwardfill of gaps')
plt.xlabel('Time (Year_Month_Day)')
plt.ylabel('Salinity')
plt.tight_layout()
plt.savefig('../results/plots/2017-08-16/salinityplot01A.png')
plt.show()
plt.clf()



untwoweeks_max = salty_time.resample('2W').max()
print(untwoweeks_max)
sm_twoweeksbf= untwoweeks_max.rolling(window=1).mean().bfill()
sm_twoweeksbf.plot()

plt.title('Salinity vs Time - Backfill of gaps ')
plt.xlabel('Time (Year_Month_Day)')
plt.ylabel('Salinity')
plt.tight_layout()
plt.savefig('../results/plots/2017-08-16/salinityplot01B.png')
plt.show()
plt.clf()
'''
df1['Salinity'].resample('M').mean().plot()
plt.ylabel('Salinity')
plt.show()
plt.clf()
'''


'''
######################Radial plot continued

width = 800
height = 800
inner_radius = 90
outer_radius = 300 - 10

minr = sqrt(log(.001 * 1E4))
maxr = sqrt(log(1000 * 1E4))
a = (outer_radius - inner_radius) / (minr - maxr)
b = inner_radius - a * maxr

def rad(mic):
    return a * np.sqrt(np.log(mic * 1E4)) + b

big_angle = 2.0 * np.pi / (len(df) + 1)
small_angle = big_angle / 7

p = figure(plot_width=width, plot_height=height, title="",
    x_axis_type=None, y_axis_type=None,
    x_range=(-420, 420), y_range=(-420, 420),
    min_border=0, outline_line_color="black",
    background_fill_color="#f0e1d2", border_fill_color="#f0e1d2",
    toolbar_sticky=False)

p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

# annular wedges
angles = np.pi/2 - big_angle/2 - df.index.to_series()*big_angle
colors = [gram_color[gram] for gram in df.gram]
p.annular_wedge(
    0, 0, inner_radius, outer_radius, -big_angle+angles, angles, color=colors,
)

# small wedges
p.annular_wedge(0, 0, inner_radius, rad(df.penicillin),
                -big_angle+angles+5*small_angle, -big_angle+angles+6*small_angle,
                color=drug_color['Penicillin'])
p.annular_wedge(0, 0, inner_radius, rad(df.streptomycin),
                -big_angle+angles+3*small_angle, -big_angle+angles+4*small_angle,
                color=drug_color['Streptomycin'])
p.annular_wedge(0, 0, inner_radius, rad(df.neomycin),
                -big_angle+angles+1*small_angle, -big_angle+angles+2*small_angle,
                color=drug_color['Neomycin'])

# circular axes and lables
labels = np.power(10.0, np.arange(-3, 4))
radii = a * np.sqrt(np.log(labels * 1E4)) + b
p.circle(0, 0, radius=radii, fill_color=None, line_color="white")
p.text(0, radii[:-1], [str(r) for r in labels[:-1]],
       text_font_size="8pt", text_align="center", text_baseline="middle")

# radial axes
p.annular_wedge(0, 0, inner_radius-10, outer_radius+10,
                -big_angle+angles, -big_angle+angles, color="black")

# bacteria labels
xr = radii[0]*np.cos(np.array(-big_angle/2 + angles))
yr = radii[0]*np.sin(np.array(-big_angle/2 + angles))
label_angle=np.array(-big_angle/2+angles)
label_angle[label_angle < -np.pi/2] += np.pi # easier to read labels on the left side
p.text(xr, yr, df.bacteria, angle=label_angle,
       text_font_size="9pt", text_align="center", text_baseline="middle")

# OK, these hand drawn legends are pretty clunky, will be improved in future release
p.circle([-40, -40], [-370, -390], color=list(gram_color.values()), radius=5)
p.text([-30, -30], [-370, -390], text=["Gram-" + gr for gr in gram_color.keys()],
       text_font_size="7pt", text_align="left", text_baseline="middle")

p.rect([-40, -40, -40], [18, 0, -18], width=30, height=13,
       color=list(drug_color.values()))
p.text([-15, -15, -15], [18, 0, -18], text=list(drug_color),
       text_font_size="9pt", text_align="left", text_baseline="middle")

output_file("burtin.html", title="burtin.py example")

show(p)
'''