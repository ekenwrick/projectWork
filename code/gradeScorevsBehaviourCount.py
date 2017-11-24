# Import relevant packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour-A.xlsx")

data = data.loc[:, ['Behaviour Count', 'Grade Score']]


for i in range(data.shape[0]):
    #
    # if i == 1:
    #     pass
    # else:
    #     for j in range(i):
    #         if data.iloc[j]['Behaviour Count'] == data.iloc[i]['Behaviour Count'] and data.iloc[j]['Grade Score'] == data.iloc[i]['Grade Score']:
    #             print(i)
    #             data.set_value(j, 'Repeat', data.iloc[j]['Repeat'] + 1)
    #             repeatEntries.append(j)

    gradeIdx = data.index[data['Grade Score'] == data.iloc[i]['Grade Score'] ].tolist()

    num = 1;
    for j in range(len(gradeIdx)):
        if data.iloc[gradeIdx[j]]['Behaviour Count'] == data.iloc[i]['Behaviour Count']:
            num += 1

    data.set_value(i, 'Repeat', num)

    print(i)

print(data)

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(data['Behaviour Count'].values.tolist(), data['Grade Score'].values.tolist(), data['Repeat'].values.tolist(), zdir='z', label='zs=0, zdir=z')

ax.set_xlabel('Behaviour Count')
ax.set_ylabel('Average Grade Score')
ax.set_zlabel('Repetition of Entry')

plt.show()



# x = data['Behaviour Count'].values.tolist()
# y = data['Grade Score'].values.tolist()
#
#
# plt.scatter(x,y)
# plt.ylabel('Average UCAS Point Score')
# plt.title('Average Students UCAS Point Score Organised By Month Of Birth')
# plt.show()
