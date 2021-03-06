
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[2]:


import matplotlib as mpl
# Default parameters for matplotlib plots
mpl.rcParams['xtick.labelsize'] = 8
mpl.rcParams['ytick.labelsize'] = 8
mpl.rcParams['axes.facecolor'] = 'w'
mpl.rcParams['lines.linewidth'] = 2
#mpl.rcParams['axes.grid'] = True
#mpl.rcParams['grid.color'] = (0.8, 0.8, 0.8)
mpl.rcParams['xtick.top'] = False
mpl.rcParams['xtick.bottom'] = True
mpl.rcParams['ytick.left'] = True
mpl.rcParams['grid.linestyle'] = '--'
mpl.rcParams['legend.fontsize'] = 8
mpl.rcParams['legend.facecolor'] = [1,1,1]
mpl.rcParams['legend.framealpha'] = 0.75
mpl.rcParams['axes.labelsize'] = 8
mpl.rcParams['axes.linewidth'] = 1
mpl.rcParams['axes.edgecolor'] = 'k'


# In[4]:


data = {'years':[2002, 2003, 2004, 2005, 2006, 2007,
                 2008, 2009, 2010, 2011, 2012, 2013,
                 2014, 2015, 2016, 2017, 2018],
        'sas':[1870, 1830, 1980, 1950, 2030, 2230,
               2400, 2420, 2550, 2630, 3010, 3200,
               3000, 3140, 3180, 3260, 2270],
        'sasmd':[146, 161, 200, 273, 221, 267, 320,
                 311, 375, 442, 447, 602, 507, 536,
                 640, 644, 495]}

df = pd.DataFrame(data)

fig, ax1 = plt.subplots(figsize=(4, 2.5))
#ax1.plot(df['years'], df['sasmd'] / df['sas'] * 100, 's',
         #color=sns.color_palette('colorblind')[0])
ax1.plot(df['years'], df['sasmd'] / df['sas'] * 100, 'o',
         color='black', markersize=5)
ax1.set_xlabel('Year')
ax1.set_ylabel('Percentage of Publications/%')
ax1.set_xticks([2002, 2006, 2010, 2014, 2018])
ax1.set_yticks([0, 10, 20])
plt.tight_layout()
plt.savefig('./reports/figures/chem_data_py.pdf', format="pdf", bbox_inches = 'tight')
plt.close()
