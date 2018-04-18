"""
# A Python script that reads in the Iris data set stored in the data subdirectory under
# the current project and then prints the four numerical values on 
# each row in a nice format on the screen. The printed data are for:
# petal length, petal width, sepal length and sepal width. 
# These values are listed with decimal places aligned, and 
# with a space between the columns.
# V1 = Sepal Width
# V2 = Sepal Length
# V3 = Petal Width
# V4 = Petal Length
# V5 = Group Classification(1, 2, 3)

An interesting observation from the next two plots confirms the existing observations on the 
Iris data set. There is a marked separation between setosa whereas, there seem not to be much 
separation among the versicolor and the virginica.
This observation further confirms the Fishers' Linear Discriminant relationship experiments. 
Explored Samples:(V2 vs V1) & (V4 vs V3)
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
#X = data.V2                     # Independent variables data
#Y = data.V1                     # Dependent variable data

"""
....
"""

### OK to here....

sns.lmplot("V1", "V2", data, hue="V5", legend_out=0)
plt.suptitle("????...PLOT")
plt.grid()

#pd.plot.hist(data.loc[:, "V2"])
#pd.DataFrame.plot.hist(data.loc[:, "V2"])
#pd.plotting.scatter_matrix(data.loc[:, "V1":"V4"], diagonal="hist")
#, col = "skyblue", xlab = "Sepal Lenght", main = 
#     "Histogram of Sepal Lenght of Iris Data")
plt.show()

