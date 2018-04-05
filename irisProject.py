"""
https://en.wikipedia.org/wiki/Iris_flower_data_set
A script for plotting multivariate tabular data as gridded scatter plots.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
inFile = r'data/iris.csv'
# Check if data file exists:
#if not os.path.exists(inFile): sys.exit("File %s does not exist" % inFile)
#rootFolder = os.path.dirname(os.path.abspath(inFile))
# Read in the data file
df = pd.read_csv(inFile, delimiter=',')        #data = pd.read_csv("data/iris.csv", header = 0)
headers = list(df.columns.values)
df.head(5) # Prints first n lines to check if we loaded the data file as expected.
# We also have n=3 distinct species in the Species column and I will
# list the species names so we can distinguish them later for plotting:
species = list(df.Species.unique()) # normal python list, thank you very much!
print(type(species))
# Here we specify how many columns prepend and append the columns that we want to use.
# For Dakota this would include the objective function(s) column(s) appended to the end.
num_precols = 0
num_obj_fn = 1
# Work out the number of dimensions in each design vector:
num_dims = df.shape[1] - num_obj_fn # We know that there are 3 additional columns (and hope that it stays consistent in future)!
print("Our design vector has %s dimensions: %s" % (num_dims, headers[num_precols:-1]))
gridshape = (num_dims, num_dims)
num_plots = num_dims**2
print("Our multivariate grid will therefore be of shape", gridshape, "with a total of", num_plots, "plots")
# Plot the data in a grid of subplots.
fig = plt.figure(figsize=(12, 12))
# Iterate over the correct number of plots.
n = 1
# Create an empty 2D list to store created axes. This alows us to edit them somehow.
axes = [[False for i in range(num_dims)] for j in range(num_dims)]
for j in range(num_dims):
    for i in range(num_dims):
        # e.g. plt.subplot(nx, ny, plotnumber)
        ax = fig.add_subplot(num_dims, num_dims, n) # Plot numbering in this case starts from 1 not zero (MATLAB style indexing)!
        # Choose your list of colours
        colors = ['red', 'green', 'blue']
        for index, s in enumerate(species):    
            # x axis: For each in the species list look at all rows with that value in the Species column.
            # Use the ith column of that subset as the x series.
            # y axis: Likewisem, but use the jth column.
            if i != j:
                ax.scatter(df.where(df['Species'] == s).ix[:,i], df.where(df['Species'] == s).ix[:,j], color=colors[index], label=s)
            else:
                # Put the variable name on the i=j subplots:
                ax.text(0.25, 0.5, headers[i])
                pass
            # Set axis labels:
            ax.set_xlabel(headers[i])
            ax.set_ylabel(headers[j])
            # Hide axes for all but the plots on the edge:
            if j < num_dims - 1: 
                ax.xaxis.set_visible(False) 
                if i > 0:
                    ax.yaxis.set_visible(False)
                    if i == 1 and j == 0:
                        ax.legend(bbox_to_anchor=(3.5, 1), loc=2, borderaxespad=0., title="Species name:")
                        # Add this axis to the list.
                        axes[j][i] = ax
    n += 1
plt.subplots_adjust(left=0.1, right=0.85, top=0.85, bottom=0.1)
# plt.savefig("%s/iris.png" % rootFolder, dpi=300)
plt.show()