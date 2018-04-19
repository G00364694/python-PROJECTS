

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

Distributions are generated here... Standard Deviation, Variance within Group,
Covariance within Groups, Coefficient of Correlation withing Group, etc. for all Samples...
"""
# Francis Adepoju. March 31 - April 28 2018      
# End of Module Project
# Investigating the Iris_flower_data_set
# http://python-for-multivariate-analysis.readthedocs.io/   ....python book"    
# http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
# https://en.wikipedia.org/wiki/Iris_flower_data_set
# A script for plotting multivariate tabular data as gridded scatter plots.

#import pandas.plotting.scatter_matrix as pd2 and all necessary libraries for this analytics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#from sklearn.preprocessing import scale
#from sklearn.decomposition import PCA
#from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from scipy import stats
from IPython.display import display, HTML

np.set_printoptions(suppress=True)

# Sample number of rows to print for a dataframe [0 <= n <= 150]
DISPLAY_MAX_ROWS = 40
pd.set_option('display.max_rows', DISPLAY_MAX_ROWS)

# Read in the data file from csv kept in /data directory
#data = pd.read_csv("data/iris.csv", header = 0)... no listed header in the file
data = pd.read_csv('data/iris.csv', delimiter=',', header=None)   

# Rename the columns to be similar to R naming convention for easy internal access...
data.columns = [ "H"+str(i) for i in range(1, len(data.columns)+1) ]
data.H5 = data.H5.astype(str)

# Means and Variances Per Group 
# from group data assigned to variable x as shown below...
x = data.loc[:, "H1":"H4"]
y = data.loc[:, "H5"]

print(data)
print("")
print("*****************************************************")
print("*                                                   *")
print("* Displaying Summary Statistics.... for input data  *")
print("*                                                   *")
print("*****************************************************")
print("")
# from group data assigned to variable x as shown below...
x = data.loc[:, "H1":"H4"]
y = data.loc[:, "H5"]

# Define a Function to Compute the Maximum, Minimum and Arithmetic Mean of the data set
# The arguments to the function are the variables that we need to calculate 
# the mean values for and the group of each sample
def printMeanByGroup(variables, groupVariable):
    data_groupby = variables.groupby(groupVariable)
    print("## Total Sample Size:", len(data))
    print(pd.DataFrame(data_groupby.apply(len)))
    print("")
    print("")
    print("## Maximum values of data sets by columns:")
    print("------------------------------------------")
    print(np.max(x))
    print("")
    print("")
    print("## Minimum values of data sets by columns:")
    print("------------------------------------------")
    print(np.min(x))
    print("")
    print("")
    print("## Mean values of data sets by groups:")
    print("--------------------------------------")
    print(data_groupby.apply(np.mean))
    print("")

# Define a Function to Calculate the standard deviations.
# The arguments to the function are the variables that we need to calculate 
# standard deviation for and the group of each sample
def printSDByGroup(variables, groupVariable):
    data_groupby = variables.groupby(groupVariable)
    #print("## Means:") and display(data_groupby.apply(np.mean))
    print("\n## Standard Deviations:")
    print("-------------------------")
    display(data_groupby.apply(np.std))


# Define the Function calcWithinColumnsVariance to compute the Within-Columns Variance 
# for a Variable, for example H1 (Sepal Length, Consisting of all 3 groups)
def calcWithinColumnsVariance(variable, groupvariable):
    # find out how many values the group variable can take
    levels = sorted(set(groupvariable))
    numlevels = len(levels)
    # get the mean and standard deviation for each group:
    numtotal = 0
    denomtotal = 0
    for leveli in levels:
        levelidata = variable[groupvariable==leveli]
        levelilength = len(levelidata)
        #print('Level= ', leveli)       # For Debugging...
        #print('Level Length= ', levelilength) 
        # get the standard deviation for group i:
        sdi = np.std(levelidata)
        numi = (levelilength)*sdi**2
        denomi = levelilength
        numtotal = numtotal + numi
        denomtotal = denomtotal + denomi
    # calculate the within-groups variance
    vw = numtotal / (denomtotal - numlevels)
    return vw

# Define the function valcBetweenGroupsInColumnsVariance for a particular variable e.g. H1, 
# for example H1 (Sepal Length.. Having Groups 1, 2, 3 - setosa, versicolor & virginica)
def calcBetweenGroupsInColVariance(variable, groupvariable):
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
        #print('Level= ', leveli)                       # For Debugging 
        #print('Level Length= ', levelilength)
        # get the mean and standard deviation for group i:
        meani = np.mean(levelidata)
        sdi = np.std(levelidata)
        #print('Mean= ', meani)                         # For Debugging
        #print('SDI= ', sdi)
        numi = levelilength * ((meani - grandmean)**2)
        denomi = levelilength
        numtotal = numtotal + numi
        denomtotal = denomtotal + denomi
    # calculate the between-groups variance
    vb = numtotal / (numlevels - 1)
    return(vb)

# Define the function calcWithinColumnsCovariance for Two Variables
# For example between columns Sepal Width & Petal Width for Groups(setosa, versicolor & virginica)
# and also for columns Sepal Height & Petal Height for Groups(setosa, versicolor & virginica)
def calcWithinColumnCovariance(variable1, variable2, groupvariable):
    levels = sorted(set(groupvariable))
    numlevels = len(levels)
    covw = 0.0
    # get the covariance of variable 1 and variable 2 for each group:
    for leveli in levels:
        levelidata1 = variable1[groupvariable==leveli]
        levelidata2 = variable2[groupvariable==leveli]
        mean1 = np.mean(levelidata1)
        mean2 = np.mean(levelidata2)
        #levelilength = len(levelidata1)
        # get the covariance for this group:
        term1 = 0.0
        for levelidata1j, levelidata2j in zip(levelidata1, levelidata2):
            term1 += (levelidata1j - mean1)*(levelidata2j - mean2)
        # covariance for this group    
        cov_groupi = term1 
        covw += cov_groupi
    totallength = len(variable1)
    covw /= totallength - numlevels
    return covw

# Define the function calcBetweenGroupsInColumns Covariance for Two Variables
# For example between columns Sepal Width & Petal Width for Groups(setosa, versicolor & virginica)
# and also for columns Sepal Height & Petal Height for Groups(setosa, versicolor & virginica)
def calcBetweenGroupsInColumnsCovariance(variable1, variable2, groupvariable):
    # find out how many values the group variable can take
    levels = sorted(set(groupvariable))
    numlevels = len(levels)
    # calculate the grand means
    variable1mean = np.mean(variable1)
    variable2mean = np.mean(variable2)
    # calculate the between-groupsInColumn covariance
    covb = 0.0
    for leveli in levels:
        levelidata1 = variable1[groupvariable==leveli]
        levelidata2 = variable2[groupvariable==leveli]
        mean1 = np.mean(levelidata1)
        mean2 = np.mean(levelidata2)
        levelilength = len(levelidata1)
        term1 = (mean1 - variable1mean) * (mean2 - variable2mean) * levelilength
        covb += term1
    covb /= numlevels - 1
    return covb

# Call the functions...

# Calculating Summary Statistics
printMeanByGroup(x, y)
print("")

# Calculating Standard Deviation data
printSDByGroup(x, y)
print("")

# Calculating Variances
print("")
print("## Variance Within Columns:")
print("---------------------------------------")
print("Variance within Column H1          is:\t\t", calcWithinColumnsVariance(x.H1, y))   
print("Variance within Column H2          is:\t\t", calcWithinColumnsVariance(x.H2, y))
print("Variance within Column H3          is:\t\t", calcWithinColumnsVariance(x.H3, y))
print("Variance within Column H4          is:\t\t", calcWithinColumnsVariance(x.H4, y))

print("")
print("## Variance Between Goups in Columns:")
print("-------------------------------------")
print("Variance between GroupsInColumn H1 is:\t\t", calcBetweenGroupsInColVariance(x.H1, y))   
print("Variance between GroupsInColumn H2 is:\t\t", calcBetweenGroupsInColVariance(x.H2, y))
print("Variance between GroupsInColumn H3 is:\t\t", calcBetweenGroupsInColVariance(x.H3, y))
print("Variance between GroupsInColumn H4 is:\t\t", calcBetweenGroupsInColVariance(x.H4, y))

# Calculating Covariances
print("")
print("## CoVariance within Similar Columns -") 
print("e.g. Sepal Length/Petal Length")
print("-------------------------------------")
print("CoVariance WithinColumns H1 & H3\t\t", calcWithinColumnCovariance(x.H1, x.H3, y))   
print("CoVariance WithinColumns H2 & H4\t\t", calcWithinColumnCovariance(x.H2, x.H4, y))

print("")
print("## CoVariance Between Groups in Similar") 
print("Columns - e.g. Sepal Length/Petal Length")
print("-------------------------------------")
print("CoVariance BetweenGroupsInColumns H1 & H3\t", calcBetweenGroupsInColumnsCovariance(x.H1, x.H3, y))   
print("CoVariance BetweenGroupsInColumns H2 & H4\t", calcBetweenGroupsInColumnsCovariance(x.H2, x.H4, y))
print("")

# Calculating Correlations for Multivariate Data. It is often of interest to investigate
# whether any of the variables in a multivariate dataset are significantly correlated.
# The correlation coefficient tells us whether the two variable that are compared have a 
# weak or a strong correlation as indicated by its magnitude.
# The p-value  for the testtells whether the correlation is significantly different
# from zero or not.
print("")
print("## Correlations for sample data set")
print("-----------------------------------")
corr = stats.pearsonr(x.H1, x.H3)
print("SEPAL-p-value:\t\t\t\t\t", corr[1])
print("SEPAL-correlation value:\t\t\t", corr[0])
print("")
corr = stats.pearsonr(x.H2, x.H4)
print("PETAL-p-value:\t\t\t\t\t", corr[1])
print("PETAL-correlation value:\t\t\t", corr[0])
print("")
print("")
print("## Correlations for all Multivariate data set")
print("---------------------------------------------")
# In order to visualize the whole data set, we can use the pandas Dataframe method corr()
# to calculate a matrix that shows the correlation coefficient for each pair of variables.
corrmat = x.corr()
#print(corrmat)

# Doing a Heatmap
# A better graphical representation of the correlation matrix is via a correlation matrix plot 
# in the form of a heatmap, using seaborn tools... 
# The color of the boxes determines the sign of the correlation, in this case,
# purple of positive and black for negative correlation; while the size of the boxes determines
# their magnitude. The bigger the box, the higher the magnitude of the coefficient of correlation.
#  
corrmat = x.corr()
print(corrmat)
sns.heatmap(corrmat, vmax=1., square=False).xaxis.tick_top()
plt.suptitle("HeatMAP of Coefficient of Correlation - Iris Dataset")
plt.grid()
plt.show()


