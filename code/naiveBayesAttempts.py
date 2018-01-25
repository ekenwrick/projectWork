# Import relevant packages
import pandas as pd
import numpy as np
import random
import statsmodels.formula.api as sm
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB

import scipy, scipy.stats

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour-A.xlsx")

data = data.loc[:, ['Behaviour Score', 'Behaviour Count', 'Grade Score']]

rowsToDelete = []

for i in range(data.shape[0]):
    if data.iloc[i]['Behaviour Score'] == 0:
        rowsToDelete.append(i)
    # if data.iloc[i]['Grade Score'] == 48 and random.random() > 0.25:
    #     rowsToDelete.append(i)

# Remove behavioural scores of 0
rowsToDelete.sort()
data = data.drop(data.index[rowsToDelete])
data = data.reset_index()







# Store grade scores in 1d array
gradeScore = []

for i in range(data.shape[0]):
    gradeScore.append(data.iloc[i]['Grade Score'])



iris  = datasets.load_iris()

print(np.ravel(data.loc[:, ['Behaviour Score', 'Behaviour Count']]))




gnb = GaussianNB()

y_pred = gnb.fit(data.loc[:, ['Behaviour Score', 'Behaviour Count']], gradeScore ).predict(data.loc[:, ['Behaviour Score', 'Behaviour Count']])

print("Number of mislabeled points out of a total %d points : %d" % (data.shape[0],(gradeScore != y_pred).sum()))
