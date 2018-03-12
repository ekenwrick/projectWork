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
yearSevenData = pd.read_excel("yearSevenScores.xlsx")
yearEightData = pd.read_excel("yearEightScores.xlsx")
yearNineData = pd.read_excel("yearNineScores.xlsx")
yearTenData = pd.read_excel("yearTenScores.xlsx")
yearElevenData = pd.read_excel("yearElevenScores.xlsx")
yearThirteenData = pd.read_excel("yearThirteenScores.xlsx")
totalData = pd.read_excel("basicDataWithGradesAndBehaviour-A.xlsx")

# Reduce to desired data only
yearSevenData = yearSevenData.loc[:, ['Behaviour Score', 'Behaviour Count', 'Grade Score']]
yearEightData = yearEightData.loc[:, ['Behaviour Score', 'Behaviour Count', 'Grade Score']]
yearNineData = yearNineData.loc[:, ['Behaviour Score', 'Behaviour Count', 'Grade Score']]
yearTenData = yearTenData.loc[:, ['Behaviour Score', 'Behaviour Count', 'Grade Score']]
yearElevenData = yearElevenData.loc[:, ['Behaviour Score', 'Behaviour Count', 'Grade Score']]
yearThirteenData = yearThirteenData.loc[:, ['Behaviour Score', 'Behaviour Count', 'Grade Score']]
totalData = totalData.loc[:, ['Behaviour Score', 'Behaviour Count', 'Grade Score']]


## REPEAT FOLLOWING FOR EACH DATASET


# Remove zero scores for behaviour score - YEAR SEVEN
rowsToDelete = []

for i in range(yearSevenData.shape[0]):
    if yearSevenData.iloc[i]['Behaviour Score'] == 0:
        rowsToDelete.append(i)
    # if yearSevenData.iloc[i]['Grade Score'] >= 40 and random.random() > 0.10:
    #     rowsToDelete.append(i)

# Remove behavioural scores of 0
rowsToDelete.sort()
yearSevenData = yearSevenData.drop(yearSevenData.index[rowsToDelete])
# data = data.reset_index()






# Remove zero scores for behaviour score - YEAR EIGHT
rowsToDelete = []

for i in range(yearEightData.shape[0]):
    if yearEightData.iloc[i]['Behaviour Score'] == 0:
        rowsToDelete.append(i)
    # if yearEightData.iloc[i]['Grade Score'] >= 40 and random.random() > 0.10:
    #     rowsToDelete.append(i)

# Remove behavioural scores of 0
rowsToDelete.sort()
yearEightData = yearEightData.drop(yearEightData.index[rowsToDelete])
# data = data.reset_index()






# Remove zero scores for behaviour score - YEAR NINE
rowsToDelete = []

for i in range(yearNineData.shape[0]):
    if yearNineData.iloc[i]['Behaviour Score'] == 0:
        rowsToDelete.append(i)
    # if yearNineData.iloc[i]['Grade Score'] >= 40 and random.random() > 0.10:
    #     rowsToDelete.append(i)

# Remove behavioural scores of 0
rowsToDelete.sort()
yearNineData = yearNineData.drop(yearNineData.index[rowsToDelete])
# data = data.reset_index()





# Remove zero scores for behaviour score - YEAR TEN
rowsToDelete = []

for i in range(yearTenData.shape[0]):
    if yearTenData.iloc[i]['Behaviour Score'] == 0:
        rowsToDelete.append(i)
    # if yearTenData.iloc[i]['Grade Score'] >= 40 and random.random() > 0.10:
    #     rowsToDelete.append(i)

# Remove behavioural scores of 0
rowsToDelete.sort()
yearTenData = yearTenData.drop(yearTenData.index[rowsToDelete])
# data = data.reset_index()





# Remove zero scores for behaviour score - YEAR ELEVEN
rowsToDelete = []

for i in range(yearElevenData.shape[0]):
    if yearElevenData.iloc[i]['Behaviour Score'] == 0:
        rowsToDelete.append(i)
    # if yearElevenData.iloc[i]['Grade Score'] >= 40 and random.random() > 0.10:
    #     rowsToDelete.append(i)

# Remove behavioural scores of 0
rowsToDelete.sort()
yearElevenData = yearElevenData.drop(yearElevenData.index[rowsToDelete])
# data = data.reset_index()





# Remove zero scores for behaviour score - YEAR THIRTEEN
rowsToDelete = []

for i in range(yearThirteenData.shape[0]):
    if yearThirteenData.iloc[i]['Behaviour Score'] == 0:
        rowsToDelete.append(i)
    # if yearThirteenData.iloc[i]['Grade Score'] >= 40 and random.random() > 0.10:
    #     rowsToDelete.append(i)

# Remove behavioural scores of 0
rowsToDelete.sort()
yearThirteenData = yearThirteenData.drop(yearThirteenData.index[rowsToDelete])
# data = data.reset_index()






# Remove zero scores for behaviour score - TOTAL DATA
rowsToDelete = []

for i in range(totalData.shape[0]):
    if totalData.iloc[i]['Behaviour Score'] == 0:
        rowsToDelete.append(i)
    # if totalData.iloc[i]['Grade Score'] >= 40 and random.random() > 0.10:
    #     rowsToDelete.append(i)

# Remove behavioural scores of 0
rowsToDelete.sort()
totalData = totalData.drop(totalData.index[rowsToDelete])
# data = data.reset_index()




# Collect index for each dataframe to find common entries across dataframes
yearSevenEntries = yearSevenData.index
yearEightEntries = yearEightData.index
yearNineEntries = yearNineData.index
yearTenEntries = yearTenData.index
yearElevenEntries = yearElevenData.index
yearThirteenEntries = yearThirteenData.index
totalEntries = totalData.index

# Find biggest intersections
# count = 1
# for data1 in [yearSevenEntries, yearEightEntries, yearNineEntries, yearTenEntries, yearElevenEntries, yearThirteenEntries, totalEntries]:
#     for data2 in [yearTenEntries]:
#         print(count)
#         count += 1
        # print(list(set(data1).intersection(data2)))

# Collect list of common entries across a multiple years
intersectionList = sorted(list(set(totalEntries).intersection(totalEntries)))

# Reduce datasets to only the relevant data
data1 = totalData
data1 = data1.loc[intersectionList]
data2 = totalData
data2 = data2.loc[intersectionList]
data2 = data2.rename(columns = {'Behaviour Score':'Behaviour Score 2'})
data2 = data2.rename(columns = {'Behaviour Count':'Behaviour Count 2'})
data2 = data2.rename(columns = {'Grade Score':'Grade Score 2'})


# Concatenate the two dataframes into one
dataToNormalise = pd.concat([data1.loc[:, ['Behaviour Score', 'Behaviour Count']], data2.loc[:, ['Behaviour Score 2', 'Behaviour Count 2']]], axis=1)
dataSet2 = pd.concat([data1.loc[:, ['Grade Score']], data2.loc[:, ['Grade Score 2']]], axis=1)

# Normalising data
# dataToNormalise = (dataToNormalise-dataToNormalise.mean())/dataToNormalise.std()
data = pd.concat([dataToNormalise, dataSet2], axis = 1)



# # UNDERSAMPLING!!!!
# rowsToDelete = []
# for i in range(data.shape[0]):
#     if data.iloc[i]['Grade Score'] >= 40 and random.random() > 0.10:
#         rowsToDelete.append(i)
#
# rowsToDelete.sort()
# data = data.drop(data.index[rowsToDelete])







for classifier in range(0,3):

    numSplits = 5
    numTries = 10
    n_neighbours = 3

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
                refinedData.set_value(i, 'Behaviour Score 2', data.iloc[i]['Behaviour Score 2'])
                refinedData.set_value(i, 'Behaviour Count 2', data.iloc[i]['Behaviour Count 2'])
                top += 1
            # elif data.iloc[i]['Grade Score'] >= 36:
            #     refinedData.set_value(i, 'Grade Bracket', 3)
            #     refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
            #     refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
            elif data.iloc[i]['Grade Score'] >= 32:
                refinedData.set_value(i, 'Grade Bracket', 4)
                refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
                refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
                refinedData.set_value(i, 'Behaviour Score 2', data.iloc[i]['Behaviour Score 2'])
                refinedData.set_value(i, 'Behaviour Count 2', data.iloc[i]['Behaviour Count 2'])
                middle += 1
            # elif data.iloc[i]['Grade Score'] >= 28:
            #     refinedData.set_value(i, 'Grade Bracket', 5)
            #     refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
            #     refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
            else:
                refinedData.set_value(i, 'Grade Bracket', 6)
                refinedData.set_value(i, 'Behaviour Score', data.iloc[i]['Behaviour Score'])
                refinedData.set_value(i, 'Behaviour Count', data.iloc[i]['Behaviour Count'])
                refinedData.set_value(i, 'Behaviour Score 2', data.iloc[i]['Behaviour Score 2'])
                refinedData.set_value(i, 'Behaviour Count 2', data.iloc[i]['Behaviour Count 2'])
                bottom += 1

        # TO KNOW THE CLASS IMBALANCE
        # print(top)
        # print(middle)
        # print(bottom)



        # # OVERSAMPLING!!!!
        #
        # overSampleRange = refinedData.shape[0]
        #
        # for i in range(overSampleRange):
        #     r = refinedData.ix[[i], :]
        #     if refinedData.iloc[i]['Grade Bracket'] == 2:
        #         pass
        #     elif refinedData.iloc[i]['Grade Bracket'] == 4:
        #         for j in range(round(top/middle)):
        #             refinedData = refinedData.append(r)
        #     else:
        #         for j in range(round(top/bottom)):
        #             refinedData = refinedData.append(r)
        #
        # refinedData = refinedData.reset_index(drop=True)
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

            X = refinedDataTrain.loc[:, ['Behaviour Score', 'Behaviour Count', 'Behaviour Score 2', 'Behaviour Count 2']]
            Y = refinedDataTrain.loc[:, 'Grade Bracket']


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

                predictions = clf.predict(refinedDataTest.loc[:, ['Behaviour Score', 'Behaviour Count', 'Behaviour Score 2', 'Behaviour Count 2']])
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
