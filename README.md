

# 52167 -- Programming and Scripting (End of Semester Project)

# Topic: Investigating the Fisher's Iris data set

## Project Plan
  1.	Investigation of the problem and available solutions… References
  2.	Writing the Python code to implement the solution
  3.	Documentation and explanations, including comments and README

## python-PROJECTS
This repository contains the project files for 52167 -- PROGRAMMING AND SCRIPTING.
Currently, The Irish Flower analysis program consists of 6 sets of code and 9 output files/plots namely:
1. Data1-Record.py
2. Data2-ScatterPlot.py
3. Data3-Relationship.py
4. Data4-Regression.py
5. Data5-Profile.py
6. Data6-Summary.py

7.  scatter.png
8.  relationship1.png
9.  relationship2.png
10. regression1.png
11. regression2.png
12. profile.png
13. heatwave.png
14. summaryOutput.txt

## Running the programs
1. Ensure that the iris-flower dataset is stored in the data directory in the project folder as a .csv file
2. Instantiate python (ipython) and run the python scripts shown above one afer the other.
3. Note that the codes may be run in any order. Each python script is self contained and are performing specific function.

## Statistical classification
In machine learning and statistics, classification is the problem of identifying to which of a set of categories (sub-populations) a new observation belongs, on the basis of a training set of data containing observations (or instances) whose category membership is known. Classification is an example of pattern recognition.
In the terminology of machine learning,[1] classification is considered an instance of supervised learning, i.e. learning where a training set of correctly identified observations is available. The corresponding unsupervised procedure is known as clustering, and involves grouping data into categories based on some measure of inherent similarity or distance.
Often, the individual observations are analyzed into a set of quantifiable properties, known variously as explanatory variables or features. These properties may variously be ordinal (e.g. "large", "medium" or "small"), integer-valued (e.g. the number of occurrences of a particular word in an email) or real-valued (e.g. a measurement of blood pressure). 

## The Iris flower data set or Fisher's Iris data set
The Iris flower data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis [2] 
LDA is a generalization of Fisher's linear discriminant, a method used in statistics, pattern recognition and machine learning to find a linear combination of features that characterizes or separates two or more classes of objects or events. The resulting combination may be used as a linear classifier, or, more commonly, for dimensionality reduction before later classification.[3] 

## Data samples and traits
The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. R. A Fisher observed that one flower species is linearly separable from the other two samples, but the other two are not linearly separable from each other. This observation will be validated in this project, together with other statistical insights, using Python3.
The columns in the Fisher’s Iris dataset are:
•	Sepal Length (cm)
•	Sepal Width (cm)
•	Petal Length (cm)
•	Petal Width (cm
•	Species Class: 
  -- Iris Virginica 
  -- Iris Versicolour 
  -- Iris Setosa

Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.
Based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning such as support vector machines [4] 
Sepal is a part of the flowering plants. Usually green, sepals typically function as protection for the flower in bud, and often as support for the petals when in bloom.
Petals are modified leaves that surround the reproductive parts of flowers. They are often brightly colored or unusually shaped to attract pollinators. Together, all of the petals of a flower are called a corolla. As mentioned above, Petals are usually accompanied by another set of special leaves called sepals. Collectively, Sepals and Petals are called calyx. [5] 

### (flowerPIC.png)
The Iris dataset employed in this project is the same used in R.A. Fisher's classic 1936 paper, “The Use of Multiple Measurements in Taxonomic Problems”, and can also be found on the UCI Machine Learning Repository. [6] 

## Data analysis 
### Clusterization
Cluster analysis or clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense) to each other than to those in other groups (clusters). It is a main task of exploratory data mining, and a common technique for statistical data analysis, used in many fields, including machine learning, pattern recognition, image analysis, information retrieval, bioinformatics, data compression, and computer graphics.
Cluster analysis itself is not one specific algorithm, but the general task to be solved. It can be achieved by various algorithms that differ significantly in their notion of what constitutes a cluster and how to efficiently find them. Popular notions of clusters include groups with small distances between cluster members, dense areas of the data space, intervals or particular statistical distributions. Clustering can therefore be formulated as a multi-objective optimization problem.
### (scatter.png)

### Distributions
### Mean (Arithmetic)
A measure of central tendency is a single value that attempts to describe a set of data by identifying the central position within that set of data. As such, measures of central tendency are sometimes called measures of central location. They are also classed as summary statistics. The mean (often called the average) is the measure of central tendency that is common among researchers, but there are others, such as the median and the mode.
The mean, median and mode are all valid measures of central tendency, but under different conditions, some measures of central tendency become more appropriate to use than others.[7]
The mean (or average) is the most popular and well known measure of central tendency. It can be used with both discrete and continuous data, although its use is most often with continuous data (see our Types of Variable guide for data types). The mean is equal to the sum of all the values in the data set divided by the number of values in the data set. So, if we have n values in a data set and they have values x1, x2, ..., xn, the sample mean, usually denoted by   (pronounced x bar), is:

 

