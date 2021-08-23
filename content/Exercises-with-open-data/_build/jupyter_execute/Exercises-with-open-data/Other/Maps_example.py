#!/usr/bin/env python
# coding: utf-8

# ## An example notebook of how to use (heat)maps with Python

# In this notebook you will see an example of using maps. The data used is openly available at https://www.opendatani.gov.uk. The goal of this example is to plot a heatmap of trees with over 90cm diameter in Belfast and with their condition being either "Dead" or "Poor".

# In[1]:


# First import pandas to be able to read csv-format data
import pandas as pd


# In[2]:


data = pd.read_csv('https://www.belfastcity.gov.uk/getmedia/262a1f01-f219-4780-835e-7a833bdd1e1c/odTrees.csv',low_memory=False)

data.head(10)


# In[3]:


# Folium module includes maps, and HeatMap is needed to generate a heatmap
import folium
from folium.plugins import HeatMap


# In[ ]:


# Choose the relevant data
diam = data[(data['DIAMETERinCENTIMETRES'] > 90) & ((diam['CONDITION'] == 'Dead') | (data['CONDITION'] == 'Poor'))]


# In[ ]:


# Folium's HeatMap-function requires the coordinates to be pairs of coordinates in a list: [[LAT,LON]]
coords = []

# Let's iterate thru the dataframe that has the data we want and append the coordinates to coords-list
for index, row in diam.iterrows():
    coords.append([row['LATITUDE'],row['LONGITUDE']])


# In[ ]:


# m is now a folium.Map, with center being at [54.5,-5.85] (Belfast), tiles changes the mapstyle. With world_copy_jump = True 
# the map is scrollable all the way around and the data moves with it as well
# control_scale = True shows the scale at the bottom left
m = folium.Map([54.5, -5.85], tiles='openstreetmap', zoom_start=10, world_copy_jump = True, control_scale = True)

# Generates the heatmap, with each node being radius 15, and a list of coordinates being the first argument.
# add_to(map) tells you to which map the heatmap layer is going to be added to
HeatMap(coords, radius = 15).add_to(m)

m

