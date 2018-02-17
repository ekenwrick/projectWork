# Import relevant packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour-A.xlsx")

# gradeScore = data.loc[:, ['Grade Score']]
ethnicity = data.loc[:, ['Ethnicity']]


# Find all different entries
uniqueEthnicity = ethnicity.stack().unique()

# Set up and create a dataframe with the grades and exams
index = uniqueEthnicity

ethnicityDF = pd.DataFrame(index=index, columns=['Total Grade Score', 'Count'])
ethnicityDF = ethnicityDF.fillna(0)

for i in range(data.shape[0]):
    if(pd.isnull(data.iloc[i]['Ethnicity'])):
        pass
    else:
        ethnicityDF.set_value(data.iloc[i]['Ethnicity'], 'Total Grade Score', ethnicityDF.loc[data.iloc[i]['Ethnicity']]['Total Grade Score'] + data.iloc[i]['Grade Score'])
        ethnicityDF.set_value(data.iloc[i]['Ethnicity'], 'Count', ethnicityDF.loc[data.iloc[i]['Ethnicity']]['Count'] + 1)

indexValues = ethnicityDF.index.values

for i in indexValues:
    ethnicityDF.set_value(i, 'Average Grade Score', ethnicityDF.loc[i]['Total Grade Score'] / ethnicityDF.loc[i]['Count'])


xticks = indexValues
x_pos = np.arange(len(xticks)) + 1
y = ethnicityDF['Average Grade Score'].tolist()

# plt.scatter(y, x_pos)
plt.barh(x_pos, y, align='center', alpha=0.5)
plt.ylabel('Ethnicity')
plt.xlabel('Average Grade Score')
plt.title('Average Students UCAS Point Score Organised By Ethnicity')
plt.yticks(x_pos,xticks)
#plt.xticks(rotation=40)
plt.show()
