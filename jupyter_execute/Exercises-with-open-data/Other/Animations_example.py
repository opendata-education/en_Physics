#!/usr/bin/env python
# coding: utf-8

# ## An example notebook of how to use animations 

# One of the ways to use animations in notebooks is to just embed them with html. This works (at least) with .gif and .mp4 formats and below is an example of this. 

# 
# <video width = "648" height="380" src="https://i.imgur.com/ANP4cBj.mp4" controls loop>

# You can also generate it yourself. Let us create an animation from CMS open data to see how the histogram changes when the amount of data increases.

# NOTE: We recommend **NOT** to use plotly with jupyter. Slows down _dramatically_ to the point where nothing can be done.

# In[1]:


# All the required modules

import matplotlib.pyplot as plt
import matplotlib.animation
import pandas as pd

# This is needed to make the animation easily accessible and prettier
from IPython.display import HTML


# In[2]:


data = pd.read_csv('http://opendata.cern.ch/record/545/files/Dimuon_DoubleMu.csv')

iMass = data.M


# In[3]:


# Let us define the function that is going to upgrade the histogram
# variable num is basically the frame number
# The way this works is that this function calculates a new histogram for each frame 

def updt_hist(num, iMass):
    plt.cla()
    axes = plt.gca()
    axes.set_ylim(0,8000)
    axes.set_xlim(0,200)
    plt.hist(iMass[:num*480], bins = 350)
    


# Cells including animations are $\Large \textbf{  slow  }$ to run. The more frames the more time it takes to run, as it has to generate each frame.

# In[4]:


get_ipython().run_cell_magic('capture', '', 'fig = plt.figure()\n \n# fargs tells which variables the function (updt_hist) is going to take in, the empty variable is required\n# so the program knows that there are two variables used in the function. The other one is automatically\n# the current frame\nanim = matplotlib.animation.FuncAnimation(fig, updt_hist, frames = 200, fargs=(iMass, ))\n\n# anim.to_jshtml() changes the animation to (javascript)html, so it can be shown on Notebook\nHTML(anim.to_jshtml())')


# The above cell does not give output because of the ```%%capture``` magic command. This is done because otherwise we would get two different pictures of the animation.

# In[ ]:


HTML(anim.to_jshtml())


# In[ ]:




