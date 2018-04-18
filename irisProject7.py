

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

Distributions are generated here... Standard Deviation, Variance within Group,
Covariance within Groups, Coefficient of Correlation withing Group for all Samples...
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
#print("Displaying Summary Statistics.... for data")


# Means and Variances Per Group 
# from group data assigned to variable x as shown below...
x = data.loc[:, "V1":"V4"]
y = data.loc[:, "V5"]
#ax.legend(loc="best", bbox_to_anchor=(0.2, 1))
#plt.show()

# Calculate the mean and standard deviations
def printMeanAndSDByGroup(variables, groupVariable):
    data_groupby = variables.groupby(groupVariable)
    #print("## Means:")
    display(data_groupby.apply(np.mean))
    print("\n## Standard Deviations:")
    display(data_groupby.apply(np.std))
    print("\n## Sample Sizes:")

    display(pd.DataFrame(data_groupby.apply(len)))

#...Plot 6  = Calculating Summary Statistics
printMeanAndSDByGroup(x, y)
#print("")
#print ("Means for groups")
#print(x.apply(np.mean))
x.apply(np.mean)
#print ("Variances for groups")
#print(x.apply(np.std))
print("")
# Between-groups Variance and Within-groups Variance for a Variable
def calcWithinGroupsVariance(variable, groupvariable):
    # find out how many values the group variable can take
    levels = sorted(set(groupvariable))
    numlevels = len(levels)
    # get the mean and standard deviation for each group:
    numtotal = 0
    denomtotal = 0
    for leveli in levels:
        levelidata = variable[groupvariable==leveli]
        levelilength = len(levelidata)
        print('Level= ', leveli)
        print('Level Length= ', levelilength) 
        # get the standard deviation for group i:
        sdi = np.std(levelidata)
        numi = (levelilength)*sdi**2
        denomi = levelilength
        numtotal = numtotal + numi
        denomtotal = denomtotal + denomi
    # calculate the within-groups variance
    vw = numtotal / (denomtotal - numlevels)
    return vw


print("Variance within sesota     - GRP 1 is: ", calcWithinGroupsVariance(x.V1, y))   
print("Variance within versiculum - GRP 2 is: ", calcWithinGroupsVariance(x.V2, y))
print("Variance within seticulum  - GRP 3 is: ", calcWithinGroupsVariance(x.V3, y))
print("")

def calcBetweenGroupsVariance(variable, groupvariable):
    # find out how many values the group variable can take
    levels = sorted(set((groupvariable)))
    numlevels = len(levels)
    # calculate the overall grand mean:
    grandmean = np.mean(variable)
    # get the mean and standard deviation for each group:
    numtotal = 0
    denomtotal = 0
    for leveli in levels:
        levelidata = variable[groupvariable==leveli]
        levelilength = len(levelidata)
        print('Level= ', leveli)
        print('Level Length= ', levelilength)
        # get the mean and standard deviation for group i:
        meani = np.mean(levelidata)
        sdi = np.std(levelidata)
        numi = levelilength * ((meani - grandmean)**2)
        denomi = levelilength
        numtotal = numtotal + numi
        denomtotal = denomtotal + denomi
    # calculate the between-groups variance
    vb = numtotal / (numlevels - 1)
    return(vb)

print("Variance between sesota     - GRP 1 is: ", calcBetweenGroupsVariance(x.V1, y))   
print("Variance between versiculum - GRP 2 is: ", calcBetweenGroupsVariance(x.V2, y))
print("Variance between seticulum  - GRP 3 is: ", calcBetweenGroupsVariance(x.V3, y))
print("")
"""
#Between-groups Covariance and Within-groups Covariance for Two Variables
def calcWithinGroupsCovariance(variable1, variable2, groupvariable):
    levels = sorted(set(groupvariable))
    numlevels = len(levels)
    Covw = 0.0
    # get the covariance of variable 1 and variable 2 for each group:
    for leveli in levels:
        levelidata1 = variable1[groupvariable==leveli]
        levelidata2 = variable2[groupvariable==leveli]
        mean1 = np.mean(levelidata1)
        mean2 = np.mean(levelidata2)
        levelilength = len(levelidata1)
        # get the covariance for this group:
        term1 = 0.0
        for levelidata1j, levelidata2j in zip(levelidata1, levelidata2):
            term1 += (levelidata1j - mean1)*(levelidata2j - mean2)
        Cov_groupi = term1 # covariance for this group
        Covw += Cov_groupi
    totallength = len(variable1)
    Covw /= totallength - numlevels
    return Covw

def calcBetweenGroupsCovariance(variable1, variable2, groupvariable):
    # find out how many values the group variable can take
    levels = sorted(set(groupvariable))
    numlevels = len(levels)
    # calculate the grand means
    variable1mean = np.mean(variable1)
    variable2mean = np.mean(variable2)
    # calculate the between-groups covariance
    Covb = 0.0
    for leveli in levels:
        levelidata1 = variable1[groupvariable==leveli]
        levelidata2 = variable2[groupvariable==leveli]
        mean1 = np.mean(levelidata1)
        mean2 = np.mean(levelidata2)
        levelilength = len(levelidata1)
        term1 = (mean1 - variable1mean) * (mean2 - variable2mean) * levelilength
        Covb += term1
    Covb /= numlevels - 1
    return Covb

print("")
print("CoVariance Within Sepal: V1", calcWithinGroupsCovariance(x.V1, x.V3, y))   
print("CoVariance Within Sepal: V3", calcWithinGroupsCovariance(x.V2, x.V4, y))
print("")
print("CoVariance Within Petal: V2", calcWithinGroupsCovariance(x.V1, x.V3, y))   
print("CoVariance Within Petal: V4", calcWithinGroupsCovariance(x.V2, x.V4, y))
print("")

print("CoVariance between Sepal: V1", calcBetweenGroupsCovariance(x.V1, x.V3, y))   
print("CoVariance between Sepal: V3", calcBetweenGroupsCovariance(x.V2, x.V4, y))
print("")
print("CoVariance between Petal: V2", calcBetweenGroupsCovariance(x.V1, x.V3, y))   
print("CoVariance between Petal: V4", calcBetweenGroupsCovariance(x.V2, x.V4, y))

print("")

# Calculating Correlations for Multivariate Data
corr = stats.pearsonr(x.V1, x.V3)
print("SEPAL-p-value:\t", corr[1])
print("SEPAL-cor:\t\t", corr[0])
print("")
corr = stats.pearsonr(x.V2, x.V4)
print("PETAL-p-value:\t", corr[1])
print("PETAL-cor:\t\t", corr[0])
print("")
# Heatmap
corrmat = x.corr()
print(corrmat)
sns.heatmap(corrmat, vmax=1., square=False).xaxis.tick_top()
plt.suptitle("HeatMAP")
plt.grid()
plt.show()

"""