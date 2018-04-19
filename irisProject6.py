

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

Summaries are generated here: The the Maximum, Minimum and Arithmetic Mean of the data set...
"""
# Francis Adepoju. March 31 - April 28 2018      
# End of Module Project
# Investigating the Iris_flower_data_set
# http://python-for-multivariate-analysis.readthedocs.io/   ....python book"    
# http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
# https://en.wikipedia.org/wiki/Iris_flower_data_set
# A script for plotting multivariate tabular data as gridded scatter plots.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.set_printoptions(suppress=True)

# Sample number of rows to print for a dataframe [0 <= n <= 150]
DISPLAY_MAX_ROWS = 50
pd.set_option('display.max_rows', DISPLAY_MAX_ROWS)

# Read in the data file from csv kept in /data directory
#data = pd.read_csv("data/iris.csv", header = 0)... no listed header in the file
data = pd.read_csv('data/iris.csv', delimiter=',', header=None)   

# Rename the columns HEADERS to be similar to R naming convention for easy internal access...
data.columns = [ "H"+str(i) for i in range(1, len(data.columns)+1) ]
data.H5 = data.H5.astype(str)

#X = data.H2                     # Independent variables data
#Y = data.H1                     # Dependent variable data
print(data)
print("*****************************************************")
print("*                                                   *")
print("* Displaying Summary Statistics.... for input data  *")
print("*                                                   *")
print("*****************************************************")
print("")
# from group data assigned to variable x as shown below...
x = data.loc[:, "H1":"H4"]
y = data.loc[:, "H5"]

# Compute the Maximum, Minimum and Arithmetic Mean of the data set
def printMeanAndSDByGroup(variables, groupVariable):
    data_groupby = variables.groupby(groupVariable)
    #print("")
    print("## Total Sample Size:", len(data))
    #print("")
    print(pd.DataFrame(data_groupby.apply(len)))
    print("")
    print("")
    print("## Maximum values of data sets by columns:")
    print(np.max(x))
    print("")
    print("")
    print("## Minimum values of data sets by columns:")
    print(np.min(x))
    print("")
    print("")
    print("## Mean values of data sets by groups:")
    print(data_groupby.apply(np.mean))
    print("")
    print("")

    # Manually compute the group Mean to re-confirm
    print("## Manually compute the group Mean to re-confirm")
    print("## Summary/Average of data sets by groups:")
    print(data_groupby.apply(np.sum)/50)
    print("")
    print("")
    
# Calculating Summary Statistics
printMeanAndSDByGroup(x, y)
print("")
