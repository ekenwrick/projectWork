# Import relevant packages
import pandas as pd
import numpy as np
import random
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import neighbors, datasets
from matplotlib.colors import ListedColormap

import scipy, scipy.stats

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour-A.xlsx")

# Reduce to desired data only
data = data.loc[:, ['Behaviour Score', 'Behaviour Count', 'Grade Score']]

# Remove zero scores for behaviour score
rowsToDelete = []

for i in range(data.shape[0]):
    if data.iloc[i]['Behaviour Score'] == 0:
        rowsToDelete.append(i)
    if data.iloc[i]['Grade Score'] >= 44 and random.random() > 0.25:
        rowsToDelete.append(i)

# Remove behavioural scores of 0
rowsToDelete.sort()
data = data.drop(data.index[rowsToDelete])
data = data.reset_index()


# Set up data frame to include grade data in groups
refinedData = pd.DataFrame(np.nan, index=range(data.shape[0]), columns=['Grade Bracket', 'Behaviour Score', 'Behaviour Count'])
refinedData = refinedData.fillna(0)


for i in range(data.shape[0]):
    # if data.iloc[i]['Grade Score'] >= 44:
    #     refinedData.set_value(i, 'Grade Bracket', 1)
    #     refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
    #     refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
    if data.iloc[i]['Grade Score'] >= 40:
        refinedData.set_value(i, 'Grade Bracket', 2)
        refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
        refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
    # elif data.iloc[i]['Grade Score'] >= 36:
    #     refinedData.set_value(i, 'Grade Bracket', 3)
    #     refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
    #     refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
    elif data.iloc[i]['Grade Score'] >= 32:
        refinedData.set_value(i, 'Grade Bracket', 4)
        refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
        refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
    # elif data.iloc[i]['Grade Score'] >= 28:
    #     refinedData.set_value(i, 'Grade Bracket', 5)
    #     refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
    #     refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
    else:
        refinedData.set_value(i, 'Grade Bracket', 6)
        refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
        refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])

print(refinedData.shape[0])

n_neighbours = 3
h = 0.02

X = refinedData.loc[:, ['Behaviour Score', 'Behaviour Count']]
Y = refinedData.loc[:, 'Grade Bracket']

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbours, weights=weights)
    clf.fit(X, Y)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X.loc[:, 'Behaviour Score'].min() - 1, X.loc[:, 'Behaviour Score'].max() + 1
    y_min, y_max = X.loc[:, 'Behaviour Count'].min() - 1, X.loc[:, 'Behaviour Count'].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    plt.scatter(X.loc[:, 'Behaviour Score'], X.loc[:, 'Behaviour Count'], c=Y, cmap=cmap_bold,
                edgecolor='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbours, weights))

plt.show()
