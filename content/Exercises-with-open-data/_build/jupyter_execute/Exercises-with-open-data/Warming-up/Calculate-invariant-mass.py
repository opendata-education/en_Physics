#!/usr/bin/env python
# coding: utf-8

# # Calculating the invariant mass

# In this example we show how to calculate the __invariant mass__ with the CMS open data. The invariant mass is an important concept for particle physicists when looking for new particles.
# 
# The following CSV files include already calculated values for invariant masses:
#     - dielectron.csv
#     - DoubleMuRun2011A.csv
#     - Jpsimumu_Run2011A.csv
#     - Ymumu_Run2011A.csv
#     
# For example, with the files _Zmumu_\__Run2011A.csv_ and _Zee_\__Run2011A.csv_ it is easy to calculate the values of the invariant masses. Let us start the calculation by importing the necessary Python modules and getting the data. In this example, we will use the file _Zmumu_\__Run2011A.csv_, which includes collision events selected from the primary dataset [1] with the specific selection criteria [2].
# 
# <br>
# <br>
# [1]  CMS collaboration (2016). DoubleMu primary dataset in AOD format from RunA of 2011 (/DoubleMu/Run2011A-12Oct2013-v1/AOD). CERN Open Data Portal. DOI: [10.7483/OPENDATA.CMS.RZ34.QR6N](http://doi.org/10.7483/OPENDATA.CMS.RZ34.QR6N).
# <br>
# [2] Thomas McCauley (2016). Zmumu. Jupyter Notebook file. https://github.com/tpmccauley/cmsopendata-jupyter/blob/hst-0.1/Zmumu.ipynb.

# ### Getting the data

# In[1]:


# Import the necessary modules. Pandas is for the data-analysis and numpy for scientific calculation.
# Name these to "pd" and "np".
import pandas as pd
import numpy as np

# Create a new DataFrame structure from the file "Zmumu_Run2011A.csv". Name it as "dataset".
dataset = pd.read_csv('../../Data/Zmumu_Run2011A.csv')


# We can check the content that we saved to the variable _dataset_ by printing the 5 first rows with the following code:

# In[ ]:


dataset.head()


# ### Performing the calculation

# Let us use the following expression for the invariant mass $M$ in the calculation:
# 
# $$M = \sqrt{2p_{T1}p_{T2}(\cosh(\eta_1-\eta_2)-\cos(\phi_1-\phi_2))}.$$
# 
# In the expression $p_T$ is the component of the momentum which is perpendicular to the beam axis, $\eta$ is the pseudorapidity (angle) and $\phi$ the azimuthal angle.
# 
# In the calculation below we will use the _numpy_ module which was named as _np_ in the first code cell. With _numpy_ it is possible to use mathematical commands like _sqrt_ and _cosh_ by calling first the name of the module (_np_) and then the command separated by a dot. So for example, the square root can be called by writing _np.sqrt( )_.
# 
# The _pt1_, _pt2_, _eta1_, _eta2_, _phi1_ and _phi2_ refer to the columns of the data. The code has to be told from where the values will be taken. So for example, if you want to get the column _pt1_, you have to write _dataset.pt1_.
# 
# Now we are ready to calculate the values of the invariant masses for the different events. _Numpy_ will automatically calculate the values for all of the events when we give the calculation in the following form, so the equation given is calculated for all of the rows.

# In[ ]:


invariant_mass = np.sqrt(2*dataset.pt1*dataset.pt2*(np.cosh(dataset.eta1-dataset.eta2) - np.cos(dataset.phi1-dataset.phi2)))


# After the calculation we can check which values were saved in the variable _invariant_mass_ by printing the content of the variable:

# In[ ]:


print(invariant_mass)


# If you wish to add calculated values as a new column to your data set see an example [here](https://github.com/cms-opendata-education/cms-jupyter-materials-english/blob/master/Introduction-to-jupyter/Add-column-to-dataframe.ipynb).
