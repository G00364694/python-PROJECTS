# Francis Adepoju. March 31 - May 15 2018      
# End of Module Project
# Investigating the Iris_flower_data_set
# http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
"""
#
# A Python script that reads in the Iris data set stored in the data subdirectory under
# the current project and then prints the four numerical values on 
# each row in a nice format on the screen. The printed data are for:
# petal length, petal width, sepal length and sepal width. 
# These values are listed with decimal places aligned, and 
# with a space between the columns.
""" 

import numpy as np
import matplotlib.pyplot as plt

# Open the input iris data file using the with keyword
myList1 = []
myList2 = []
myList3 = []
myList4 = []
with open("data/iris.csv") as f: 
    # Loop through the file and split the data, summing up the data in the process  
    samplesTotal = 0     
    for myData in f:                    #
        # Data are forced to be seen as type float
        col1 = float(myData.split(',')[0])      
        col2 = float(myData.split(',')[1])
        col3 = float(myData.split(',')[2])
        col4 = float(myData.split(',')[3])
        col5 = myData.split(',')[4]  # Not used in this program...
        samplesTotal = samplesTotal + 1

        myList1.append(col1)
        myList2.append(col2)
        myList3.append(col3)
        myList4.append(col4)
        # Data are formatted and printed on the screen as required.
        # print('{0:.1f} {1:.1f} {2:.1f} {3:.1f}'.format(col1, col2, col3, col4))
        # Using the python f-Strings to print same
        #print(f'{col1} {col2} {col3} {col4}')
        #print(myList1)
        #print(myList2)
        #print(myList3)
        #print(myList4)
data = (myList1, myList2, myList3, myList4) 
colors = ("green", "blue", "red")
groups = ("setosa", "versicolor", "viginica")
# 1, 1, 1, 1, axisbg="1.0"
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

for data, color, group in zip(data, colors, groups):
    #x, y = myList1, myList2 #data
    x = myList1 
    y = myList2
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

plt.title('Relationship Sepal length and Sepal width')
plt.legend(loc=1)     
plt.xlabel('Sepal Length(cm)')
plt.ylabel('Sepal Width(cm)')

# plt.scatter(X, Y, s=60, c='red', marker='^')
# plt.scatter(myList1, myList2, myList3, myList4)
# plt.scatter(myList1, c='red', marker='*', myList2, c='blue', myList3, c='green', myList4, c='black')
#plt.scatter(myList1, myList2, marker='*')
#plt.scatter(myList1, myList2, myList3, myList4, marker='*')

plt.show()
        #print("Total Samples = " + str(samplesTotal))
        #  
#print("End of file processing")                 # End of processing.


