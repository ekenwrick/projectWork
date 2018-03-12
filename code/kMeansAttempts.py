# Import relevant packages
import pandas as pd
import numpy as np
import random
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
from sklearn import neighbors, datasets, preprocessing, svm
from sklearn.linear_model import LogisticRegression
from matplotlib.colors import ListedColormap

import scipy, scipy.stats



# Import data
# data = pd.read_excel("yearSevenScores.xlsx")
# data = pd.read_excel("yearEightScores.xlsx")
# data = pd.read_excel("yearNineScores.xlsx")
# data = pd.read_excel("yearTenScores.xlsx")
# data = pd.read_excel("yearElevenScores.xlsx")
# data = pd.read_excel("yearThirteenScores.xlsx")
data = pd.read_excel("basicDataWithGradesAndBehaviour-A.xlsx")

# Reduce to desired data only
data = data.loc[:, ['Behaviour Score', 'Behaviour Count', 'Grade Score']]

# Remove zero scores for behaviour score
rowsToDelete = []

for i in range(data.shape[0]):
    if data.iloc[i]['Behaviour Score'] == 0:
        rowsToDelete.append(i)
    if data.iloc[i]['Grade Score'] >= 40 and random.random() > 0.50:
        rowsToDelete.append(i)

# Remove behavioural scores of 0
rowsToDelete.sort()
data = data.drop(data.index[rowsToDelete])
data = data.reset_index()




for classifier in range(0,3):

    numSplits = 5
    numTries = 10
    n_neighbours = 1

    totalAccuracyDistance = 0
    totalAccuracyUniform = 0
    totalAccuracyDistanceB = 0
    totalAccuracyUniformB = 0

    for counter in range(numSplits):





        # Set up data frame to include grade data in groups
        refinedData = pd.DataFrame(np.nan, index=range(data.shape[0]), columns=['Grade Bracket', 'Behaviour Score', 'Behaviour Count'])
        refinedData = refinedData.fillna(0)


        top = 0
        middle = 0
        bottom = 0
        for i in range(data.shape[0]):
            # if data.iloc[i]['Grade Score'] >= 44:
            #     refinedData.set_value(i, 'Grade Bracket', 1)
            #     refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
            #     refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
            if data.iloc[i]['Grade Score'] >= 40:
                refinedData.set_value(i, 'Grade Bracket', 2)
                refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
                refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
                top += 1
            # elif data.iloc[i]['Grade Score'] >= 36:
            #     refinedData.set_value(i, 'Grade Bracket', 3)
            #     refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
            #     refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
            elif data.iloc[i]['Grade Score'] >= 32:
                refinedData.set_value(i, 'Grade Bracket', 4)
                refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
                refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
                middle += 1
            # elif data.iloc[i]['Grade Score'] >= 28:
            #     refinedData.set_value(i, 'Grade Bracket', 5)
            #     refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
            #     refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
            else:
                refinedData.set_value(i, 'Grade Bracket', 6)
                refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
                refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
                bottom += 1

        # OVERSAMPLING!!!!

        overSampleRange = refinedData.shape[0]

        for i in range(overSampleRange):
            r = refinedData.ix[[i], :]
            if refinedData.iloc[i]['Grade Bracket'] == 2:
                pass
            elif refinedData.iloc[i]['Grade Bracket'] == 4:
                for j in range(round(top/middle)):
                    refinedData = refinedData.append(r)
            else:
                for j in range(round(top/bottom)):
                    refinedData = refinedData.append(r)

        refinedData = refinedData.reset_index(drop=True)
        #
        #



        for count in range(numTries):

            trainSet = sorted(random.sample(range(0,refinedData.shape[0]), round(refinedData.shape[0] * 0.7)))
            testSet = list(range(0,refinedData.shape[0]))

            for i in trainSet:
                testSet.remove(i)

            refinedDataTrain = refinedData.loc[trainSet, :]
            refinedDataTest = refinedData.loc[testSet, :]




            h = 0.02

            X = refinedDataTrain.loc[:, ['Behaviour Score', 'Behaviour Count']]
            Y = refinedDataTrain.loc[:, 'Grade Bracket']

            # Create color maps
            cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
            cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

            for weights in ['uniform', 'distance']:

                # we create an instance of Neighbours Classifier and fit the data.
                if classifier == 0:
                    clf = neighbors.KNeighborsClassifier(n_neighbours, weights=weights)
                elif classifier == 1:
                    if weights == 'uniform':
                        clf = svm.SVC(kernel='linear')
                    else:
                        clf = svm.SVC(kernel='rbf')
                elif classifier == 2:
                    clf = LogisticRegression()

                clf.fit(X, Y)

                predictions = clf.predict(refinedDataTest.loc[:, ['Behaviour Score', 'Behaviour Count']])
                baseline = []
                for x in predictions:
                    baseline.append(2)

                correct = 0
                incorrect = 0

                baselineCorrect = 0
                baselineIncorrect = 0

                for i in range(refinedDataTest.shape[0]):
                    if predictions[i] == refinedDataTest.iloc[i]['Grade Bracket']:
                        correct += 1
                    else:
                        incorrect += 1

                    if baseline[i] == refinedDataTest.iloc[i]['Grade Bracket']:
                        baselineCorrect += 1
                    else:
                        baselineIncorrect += 1



                if weights == 'uniform':
                    totalAccuracyUniform += ((correct/(correct + incorrect)) * 100)
                    totalAccuracyUniformB += ((baselineCorrect/(baselineCorrect+ baselineIncorrect)) * 100)
                elif weights == 'distance':
                    totalAccuracyDistance += ((correct/(correct + incorrect)) * 100)
                    totalAccuracyDistanceB += ((baselineCorrect/(baselineCorrect + baselineIncorrect)) * 100)

                if count == numTries:
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
                    plt.xlabel('Behaviour Score')
                    plt.ylabel('Behaviour Count')

                    plt.show()




        # averageAccuracyUniform = totalAccuracyUniform / numTries
        # averageAccuracyDistance = totalAccuracyDistance / numTries
        #
        # averageAccuracyUniformB = totalAccuracyUniformB / numTries
        # averageAccuracyDistanceB = totalAccuracyDistanceB / numTries

    averageAccuracyUniform = totalAccuracyUniform / (numSplits*numTries)
    averageAccuracyDistance = totalAccuracyDistance / (numSplits*numTries)

    averageAccuracyUniformB = totalAccuracyUniformB / (numSplits*numTries)
    averageAccuracyDistanceB = totalAccuracyDistanceB / (numSplits*numTries)

    print('Uniformly weighted nearest neighbours (baseline of always 2) provides an accuracy of ' + str(averageAccuracyUniformB) + '%.')
    print('Distance weighted nearest neighbours (baseline of always 2) provides an accuracy of ' + str(averageAccuracyDistanceB) + '%.')
    print(' ')
    print('Uniformly weighted nearest neighbours provides an accuracy of ' + str(averageAccuracyUniform) + '%.')
    print('Distance weighted nearest neighbours provides an accuracy of ' + str(averageAccuracyDistance) + '%.')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
