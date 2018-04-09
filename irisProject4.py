"""
#
# A Python script that reads in the Iris data set stored in the data subdirectory under
# the current project and then prints the four numerical values on 
# each row in a nice format on the screen. The printed data are for:
# petal length, petal width, sepal length and sepal width. 
# These values are listed with decimal places aligned, and 
# with a space between the columns.
"""
# Francis Adepoju. March 31 - April 28 2018      
# End of Module Project
# Investigating the Iris_flower_data_set
# http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
# https://en.wikipedia.org/wiki/Iris_flower_data_set
# A script for plotting multivariate tabular data as gridded scatter plots.

import os
import pandas as pd
#import pandas.plotting.scatter_matrix as pd2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from scipy import stats
from IPython.display import display, HTML

# Figures inline in notebook
#% matplotlib inline

np.set_printoptions(suppress=True)

# number of max rows to print for a dataframe:
DISPLAY_MAX_ROWS = 20
pd.set_option('display.max_rows', DISPLAY_MAX_ROWS)

# Useful to have for quick experimentation....
# %qtconsole

# Read in the data file
#inFile = r'data/iris.csv'
data = pd.read_csv('data/iris.csv', delimiter=',', header=None)        #data = pd.read_csv("data/iris.csv", header = 0)
# Rename the columns to be similar to R naming convention for easy access...
data.columns = [ "V"+str(i) for i in range(1, len(data.columns)+1) ]
data.V5 = data.V5.astype(str)
#X = data.loc["V2":]      # Independent variables data
X = data.V2                   # Independent variables data
Y = data.V1                 # Dependent variable data
#print(data)
### OK to here....

data.loc[:, "V1":"V4"]
#colors = ("green", "blue", "red")
#pd.plotting.scatter_matrix(data.loc[:, "V1":"V4"], diagonal="hist")
#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.legend(loc=2)
# plt.tight_layout()
# plt.show()

### OK to here....

sns.lmplot("V1", "V2", data, hue="V5", legend_out=0)
plt.suptitle("????...PLOT")
plt.grid()
plt.show()

