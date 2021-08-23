#!/usr/bin/env python
# coding: utf-8

# ### Background 

# This notebook includes an example exercise about observing how the amount of data affects to the histogram made from that data. The exercise consists of a theory part and a practical part.

# # Example: Invariant mass histogram

# In this exercise the CMS (Compact Muon Solenoid) detector and the concept of invariant mass are introduced. With the real data collected by CMS detector, the effect of the amount of data on the histogram of that data is observed.

# ### CMS detector

# At CERN, particles are accelerated and collided with the LHC (Large Hadron Collider) particle accelerator. With the CMS detector, the new particles created in these collisions can be observed and measured. The picture below shows the inside of the CMS detector.
# 
# <img src="../../Images/CMS.jpg" alt="CMS-ilmaisin avattuna" style="height: 400px">
# 
# (Image: Domenico Salvagnin, https://commons.wikimedia.org/wiki/File:CMS@CERN.jpg)
# <br>
# <br>
# <br>

# ### Invariant mass

# Invariant mass $M$ is a value that can be calculated from the results of measurements from the CMS detector. Invariant mass is a mathematical concept, not a physical mass.
# 
# For example, let us take a situation where a particle A decays into two particles B and C. The invariant mass of the two particles B and C is determined by the equation
# 
# $$ M = \sqrt{(E_1 + E_2)^2-(\vec{p_1} + \vec{p_2})^2}, $$
# 
# where $E_1$ and $E_2$ are the energies of the decay products and $\vec{p_1}$ and $\vec{p_2}$ the momenta of the decay products.
# 
# The invariant mass can be used to determine the existence of the particle A. If particles B and C stem from the decay of particle A, their invariant mass equals the physical mass of particle A. If particles B and C stem from some other process than the decay of A (there are an enormous amount of processes in particle collisions), the invariant mass of B and C is something else.
# 
# So by determing the energies and the momenta of B and C, their invariant mass can be calculated. This can be done for large amounts of particle pairs, and in doing so we may show the existence of particle A.
# 
# In this exercise the values of the invariant masses are already calculated.

# ### Try it!

# Let us start by looking at the data collected by CMS detector. We will focus on the decay of Z-boson to two muons (muon and antimuon pair).
# 
# We will use the data collected in 2011 [1]. From the primary dataset, 10851 collision events where were exactly two muons have been selected in the file "Zmumu_Run2011A_masses.csv". (The selection has been done with the code that is openly available at https://github.com/tpmccauley/dimuon-filter.)
# 
# The file includes already-calculated values of the invariant masses of two muons for the 10851 events. A histogram is a great tool for observing these values. The histogram represents how many events there are within a certain range of values of $M$.
# 
# In the next exercise, the goal is to examine __how the amount of data used affects the histogram of that data.__
# <br>
# <br>
# <br>
# [1]  CMS collaboration (2016). DoubleMu primary dataset in AOD format from RunA of 2011 (/DoubleMu/Run2011A-12Oct2013-v1/AOD). CERN Open Data Portal. DOI: [10.7483/OPENDATA.CMS.RZ34.QR6N](http://doi.org/10.7483/OPENDATA.CMS.RZ34.QR6N).

# ### 1) Getting the file and the masses

# Let us start by importing the necessary Python modules the data. After that you can move to the part two. You might get a warning related to the _matplotlib_ module but you do not have to worry about that in this exercise.

# In[1]:


# Import the needed modules. Pandas is for the data-analysis, numpy for scientific calculation
# and matplotlib.pyplot for making plots. Modules are named as pd, np and plt.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a new DataFrame structure from the file "Zmumu_Run2011A_masses.csv"
dataset = pd.read_csv('../../Data/Zmumu_Run2011A_masses.csv')

# Create a Series structure (basically a list) and name it "invariant_mass".
# Save the column "M" from the "dataset" to the variable "invariant_mass".
invariant_mass = dataset['M']

# Create an empty list "selected", where the selected amount of invariant masses will be saved.
selected = []


# ### Selecting the amount of data

# The code below asks how many events will be selected for the histogram. After, the code plots the histogram of the selected invariant masses.
# 
# Examine how the amount of the data used affects the histogram. Which values of the invariant mass seem to come up the most? What can you conclude from those values?
# 
# By examining the code, predict what will happen if you enter a number bigger than 10851 for the amount of data. Try your prediction by running the code.

# In[ ]:


# Ask user to enter the number of events wanted. Save the number to the variable "amount".
amount = int(input('Enter the amount of events wanted: '))

# Check if user has selected more events than there are available.
# If not, select that amount of invariant masses from the variable "invariant_mass".
# Masses will be selected in order.
if amount > 10851:
    print('''You have tried to select more data than there are available in the file.
The histogram could not be drawn. The maximum amount events is 10851.''')
else:
    for f in range(amount):
        M = invariant_mass[f]
        selected.append(M)
    print('\n You selected {} invariant mass values from the whole dataset.'.format(amount))

# Jupyter Notebook uses "magic functions". With this function it is possible to plot
# the histogram straight to notebook.
get_ipython().run_line_magic('matplotlib', 'inline')

# Create the histogram from data in variable "selected". Set bins and range of the histogram.
plt.hist(selected, bins=120, range=(60,120))

# Set y-axis from 0 to 800.
axes = plt.gca()
axes.set_ylim([0,800])

# Name the axes and give a title.
plt.xlabel('Invariant mass [GeV]')
plt.ylabel('Number of events')
plt.title('Histogram of invariant masses of two muons\n')

# Empty the variable "selected" for the next run.
selected = []


# ### 3) Evolution of the histogram when the amount of data increases

# Let us observe with a series of images how the histogram will change when the amount of data is increased.
# 
# The code below will create 11 different histograms of invariant masses from the same data. Between every image, 1000 more values are added to the histogram. Observe the images and explain what you see.

# In[ ]:


# Loop where a new histogram is plotted after 1000 events until 10000 events have reached.
for a in range(0,10851,1000):
    T = invariant_mass[0:a]
    
    get_ipython().run_line_magic('matplotlib', 'inline')
    plt.hist(T, bins=120, range=(60,120))
    
    # Set y-axis from 0 to 800.
    axes = plt.gca()
    axes.set_ylim([0,800])
    
    plt.xlabel('Invariant mass [GeV]')
    plt.ylabel('Number of events')
    plt.title('Histogram of invariant masses of two muons for {} events\n'.format(len(T)))
    plt.show()


# In[ ]:




