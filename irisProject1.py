"""
# A Python script that reads in the Iris data set stored in the data subdirectory under
# the current project and then prints the four numerical values on 
# each row in a nice format on the screen. The printed data are for:
# petal length, petal width, sepal length and sepal width. 
# These values are listed with decimal places aligned, and 
# with a space between the columns.

This stage turns out to be the most crucial stage of the data analysis as a window is now open
to view and then manipulate the dataset as needed. 
"""
# Francis Adepoju. March 31 - April 28 2018      
# End of Module Project
# Investigating the Iris_flower_data_set
# http://python-for-multivariate-analysis.readthedocs.io/   ....python book" 
# http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
# https://en.wikipedia.org/wiki/Iris_flower_data_set
# A script for plotting multivariate tabular data as gridded scatter plots.

#import pandas.plotting.scatter_matrix as pd2 and all necessary libraries for this analytics
#import os
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#from sklearn.preprocessing import scale
#from sklearn.decomposition import PCA
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
#from scipy import stats
#from IPython.display import display, HTML

np.set_printoptions(suppress=True)

# number of max rows to print for a dataframe:
DISPLAY_MAX_ROWS = 25
pd.set_option('display.max_rows', DISPLAY_MAX_ROWS)

# Read in the data file from csv kept in /data directory
#data = pd.read_csv("data/iris.csv", header = 0)... no listed header in the file
data = pd.read_csv('data/iris.csv', delimiter=',', header=None)   

# Rename the columns to be similar to R naming convention for easy access...
data.columns = [ "V"+str(i) for i in range(1, len(data.columns)+1) ]
data.V5 = data.V5.astype(str)   # Column 5 holds the Group name as type string
X = data.V2                     # Independent variables data
Y = data.V1                     # Dependent variable data
# Print pre-set array of data indicated by DISPLAY_MAX_ROWS in line 35
print(data)
