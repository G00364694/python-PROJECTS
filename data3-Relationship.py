"""
# A Python script that reads in the Iris data set stored in the data subdirectory under
# the current project and then prints the four numerical values on 
# each row in a nice format on the screen. The printed data are for:
# petal length, petal width, sepal length and sepal width. 
# These values are listed with decimal places aligned, and 
# with a space between the columns.
# H1 = Sepal Length
# H2 = Sepal Width
# H3 = Petal Length
# H4 = Petal Width
# H5 = Group Classification(1, 2, 3)

An interesting observation from the next two plots confirms the existing observations on the 
Iris data set. There is a marked separation between setosa whereas, there seem not to be much 
separation among the versicolor and the virginica.
This observation further confirms the Fishers' Linear Discriminant relationship experiments. 
Explored Samples:(H1 vs H2) & (H3 vs H4)
"""
# Francis Adepoju. March 31 - April 28 2018      
# End of Module Project
# Investigating the Iris_flower_data_set
# http://python-for-multivariate-analysis.readthedocs.io/   ....python book" 
# http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
# https://en.wikipedia.org/wiki/Iris_flower_data_set
# A script for plotting multivariate tabular data as gridded scatter plots.

#import all necessary libraries for this analytics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.set_printoptions(suppress=True)

# Sample number of rows to print for a dataframe [0 <= n <= 150]
DISPLAY_MAX_ROWS = 40
pd.set_option('display.max_rows', DISPLAY_MAX_ROWS)

# Read in the data file from csv kept in /data directory
#data = pd.read_csv("data/iris.csv", header = 0)... no listed header in the file
data = pd.read_csv('data/iris.csv', delimiter=',', header=None)   

# Rename the columns to be similar to R naming convention for easy access...
data.columns = [ "H"+str(i) for i in range(1, len(data.columns)+1) ]
data.H5 = data.H5.astype(str)   # Column 5 holds the Group name as type string

"""
An interesting observation of group clustering are revelaled in these two plots 
of the Iris data set. The iris setosa are more closesly clustered and further from the other two 
loosely compacted and closely related species -  the versicolor and the virginica.
"""
# Plot H1 vs H2: Sepal Length vs Width, NO REGRESSION
sns.lmplot("H1", "H2", data, hue="H5", legend_out=0, fit_reg=False)
plt.set_cmap('inferno')
plt.suptitle("Sepal Length vs. Sepal Width")
plt.grid()
# Plot H3 vs H4: Petal Length vs Width, NO REGRESSION
sns.lmplot("H3", "H4", data, hue="H5", legend_out=0, fit_reg=False)
plt.set_cmap('inferno')
plt.suptitle("Petal Length vs. Petal Width")
plt.grid()
# Render the plots 
plt.show()

