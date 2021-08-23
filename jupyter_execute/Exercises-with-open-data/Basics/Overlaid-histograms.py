#!/usr/bin/env python
# coding: utf-8

# # Importing a CMS open data file and creating overlaid histograms to analyze data

# This activity will help you practice with Jupyter Notebook. It is recommended that you select *Kernel $\rightarrow$ Restart & Clear Output* before going through the notebook. This way you may start fresh without previous outputs.
# 
# Select a data file to analyze from [opendata.cern.ch](http://opendata.cern.ch/record/545).
# For this example, download Dimuon_DoubleMu.csv and save it to a folder named *Data*. Note, there are other files available, but the file must be comma separated values (.csv). If the file name has spaces between the words replace them with underscores.
# 
# Boxes, like this, that give instruction but not code, can be created by pressing "b" and selecting "Markdown" from the dropdown menu above. To enter code, select "Code" from the dropdown menu. Cell content may be copied from other sources, pasted, and edited.
# 
# First, you will need to import the packages pandas and matplotlib.pyplot to be able to read files and plot histogram.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# After finishing a code box, press *Ctrl + Enter* at the same time to run the code. An asterisk will appear in the *In[ ]* while the command is being processed. Wait until a number appears in that location before proceeding. 
# Possible error messages will appear in pink and will indicate information regarding the error. 
# 
# To use the file you have downloaded, it must be saved into a variable. Type the file location and name exactly as it appears on your computer. In this example, the file is located in a folder named *Data*. The path is therefore  *../../Data/Dimuon_DoubleMu.csv*.  
# 
# Save the data into the variable *dataset* and check the contents of the first 5 rows.

# In[2]:


dataset = pd.read_csv('../../Data/Dimuon_DoubleMu.csv')

dataset.head()


# In this example, the invariant mass is of particular interest. Save the invariant mass column from the *dataset* into a variable called *invariant_mass* by using the column heading as it appears in the table, e.g. *M*. If your dataset does not contain invariant masses by default you must first [calculate them](https://github.com/cms-opendata-education/cms-jupyter-materials-english/blob/master/Exercises-with-open-data/Calculate-invariant-mass.ipynb). Plot a histogram, stating which variable to plot, setting the number of bins and range.
# In the example below, we use 50 bins and plot from 0 to 200 GeV. 

# In[ ]:


invariant_mass = dataset['M']

plt.hist(invariant_mass, bins=50, range=(0,200))
plt.show()


# The number of bins and range can be varied in order to analyze the data more clearly. Below are commands to replot the graph with a title and axis labels.

# In[ ]:


plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of events')
plt.title('The histogram of the invariant masses of two muons \n')

plt.hist(invariant_mass, bins=50, range=(0,200))
plt.show()


# The graph above demonstrates background events below approximately 50 GeV and a peak at approximately 90 GeV.
# 
# 
# Mathematical operations, such as addition or subtraction, may be performed on the data by defining new variables which allows the data to be further sorted. In the example below, the original data is divided into two new datasets based on the energy of the collision. Each dataset is given a name and organized in this case by high energy (> 150 GeV) and low energy (< 150 GeV).
# 

# In[ ]:


newsethighE = dataset[dataset.E1+dataset.E2>150]
newsetlowE = dataset[dataset.E1+dataset.E2<150]


# The new data sets can be plotted separately as was done previously or on one plot. The two histograms can be overlaid by adjusting the transparency using the 'alpha' argument. Labels for each data set are included in the legend located in the upper right corner. We can also change the range to focus on the event of interest.

# In[ ]:


plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of events')
plt.title('The invariant masses of two muons comparing high and low energy\n')
plt.hist(newsetlowE ['M'], bins=50, range=(80,100),alpha=0.5, label='Low E')
plt.hist(newsethighE ['M'], bins=50, range=(80,100),alpha=0.5, label='High E')
plt.legend (loc='upper right')
plt.show()


# What do you think will happen if you change the value of energy limit? Try it out by changing the limits in *newsethighE* and *newsetlowE*.
