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
# Open the input iris data file using the with keyword
with open("data/iris.csv") as inputFile: 
    # Loop through the file and split the data, summing up the data in the process  
    samplesTotal = 0     
    for myData in inputFile:                    #
        # Data are forced to be seen as type float
        col1 = float(myData.split(',')[0])      
        col2 = float(myData.split(',')[1])
        col3 = float(myData.split(',')[2])
        col4 = float(myData.split(',')[3])
        col5 = myData.split(',')[4]  # Not used in this program...
        samplesTotal = samplesTotal + 1
        # Data are formatted and printed on the screen as required.
        # print('{0:.1f} {1:.1f} {2:.1f} {3:.1f}'.format(col1, col2, col3, col4))
        # Using the python f-Strings to print same
        print(f'{col1} {col2} {col3} {col4}')
    print("Total Samples = " + str(samplesTotal))
        #  
print("End of file processing")                 # End of processing.


