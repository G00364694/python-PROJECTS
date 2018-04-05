import csv
import numpy  as np 
import pandas as pd




# import some data to play with. w
# 
with open("data/iris.csv") as datasets:
# iris = datasets.load_iris()
 X = datasets.data[:, :2] # we only take the first two features. 
 Y = datasets.target
# print(X)
# print(Y)
# print(np.bincount(Y, minlength=np.size(Y)))

 h = .02 # step size in the mesh

 knn = neighbors.KNeighborsClassifier()

# we create an instance of Neighbours Classifier and fit the data.
 knn.fit(X, Y)

# Plot the decision boundary. For that, we will asign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
 x_min, x_max = X[:,0].min() - .5, X[:,0].max() + .5
 y_min, y_max = X[:,1].min() - .5, X[:,1].max() + .5
 xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
 Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

 # Put the result into a color plot
 Z = Z.reshape(xx.shape)
 plt.figure(1, figsize=(4, 3))
 plt.set_cmap(plt.cm.Paired)
 plt.pcolormesh(xx, yy, Z)

# Plot also the training points
 plt.scatter(X[:,0], X[:,1],c=Y )
 plt.xlabel('Sepal length')
 plt.ylabel('Sepal width')

 plt.xlim(xx.min(), xx.max())
 plt.ylim(yy.min(), yy.max())
 plt.xticks(())
 plt.yticks(())

 plt.show()
