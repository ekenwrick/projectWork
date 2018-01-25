# Import relevant packages
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour-A.xlsx")

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

# Calculate correlation matrix for the three variables
correlationCoefficient = np.corrcoef(data.loc[:, ['Behaviour Score', 'Behaviour Count', 'Grade Score']], rowvar = False)
print(correlationCoefficient)


fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(data['Behaviour Score'].values.tolist(), data['Grade Score'].values.tolist(), data['Behaviour Count'].values.tolist(), zdir='z', label='zs=0, zdir=z')

ax.set_xlabel('Behaviour Score')
ax.set_ylabel('Average Grade Score')
ax.set_zlabel('Behaviour Count')

plt.show()
