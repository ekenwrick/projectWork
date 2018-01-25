# Import relevant packages
import pandas as pd
import numpy as np
import random
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression
import scipy, scipy.stats

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour-A.xlsx")

data = data.loc[:, ['Behaviour Score', 'Behaviour Count', 'Grade Score']]

# Remove zero scores for behaviour score
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

data['Eins'] = np.ones(( len(data), ))
Y = data.loc[:, ['Grade Score']]
X = data.loc[:, ['Behaviour Score', 'Eins']]
result = sm.OLS( Y, X ).fit()
print(result.summary())

data['Eins'] = np.ones(( len(data), ))
Y = data.loc[:, ['Grade Score']]
X = data.loc[:, ['Behaviour Count', 'Eins']]
result = sm.OLS( Y, X ).fit()
print(result.summary())

data['Eins'] = np.ones(( len(data), ))
Y = data.loc[:, ['Grade Score']]
X = data.loc[:, ['Behaviour Score', 'Behaviour Count', 'Eins']]
result = sm.OLS( Y, X ).fit()
print(result.summary())
