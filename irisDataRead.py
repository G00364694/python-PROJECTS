
import csv

import numpy as np
import pandas as pd

import matplotlib
from matplotlib import pyplot as plt
#matplotlib.style.use('ggplot')
import pylab
import seaborn as sns

from IPython.core.display import display, HTML

data = pd.read_csv("data/iris.csv", header = 0)
#reset index
data = data.reset_index()
data.head()

species_list = list(data["Species"].unique())
print("Types of species: %s\n" % species_list)

print("Dataset length: %i\n" % len(data))

print("Sepal length range: [%s, %s]" % (min(data["SepalLengthCm"]), max(data["SepalLengthCm"])))
print("Sepal width range:  [%s, %s]" % (min(data["SepalWidthCm"]), max(data["SepalLengthCm"])))
print("Petal length range: [%s, %s]" % (min(data["PetalLengthCm"]), max(data["PetalLengthCm"])))
print("Petal width range:  [%s, %s]\n" % (min(data["PetalWidthCm"]), max(data["PetalWidthCm"])))

print("Sepal length variance:\t %f" % np.var(data["SepalLengthCm"]))
print("Sepal width variance: \t %f" % np.var(data["SepalWidthCm"]))
print("Petal length variance:\t %f" % np.var(data["PetalLengthCm"]))
print("Petal width variance: \t %f\n" % np.var(data["PetalWidthCm"]))

print("Sepal length stddev:\t %f" % np.std(data["SepalLengthCm"]))
print("Sepal width stddev: \t %f" % np.std(data["SepalWidthCm"]))
print("Petal length stddev:\t %f" % np.std(data["PetalLengthCm"]))
print("Petal width stddev: \t %f\n" % np.std(data["PetalWidthCm"]))

print("Data describe\n---")
print(data[data.columns[2:]].describe())