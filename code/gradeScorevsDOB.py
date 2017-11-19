# Import relevant packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import data
data = pd.read_excel("basicDataWithGrades-A.xlsx")

data = data.loc[:, ['DOB', 'Grade Score']]
data['DOB'].apply(str)

for i in range(0, data.shape[0]):
    if data.iloc[i]['DOB'].split()[1] == 'January':
        data.set_value(i, 'DOB', 1)
    elif data.iloc[i]['DOB'].split()[1] == 'February':
        data.set_value(i, 'DOB', 2)
    elif data.iloc[i]['DOB'].split()[1] == 'March':
        data.set_value(i, 'DOB', 3)
    elif data.iloc[i]['DOB'].split()[1] == 'April':
        data.set_value(i, 'DOB', 4)
    elif data.iloc[i]['DOB'].split()[1] == 'May':
        data.set_value(i, 'DOB', 5)
    elif data.iloc[i]['DOB'].split()[1] == 'June':
        data.set_value(i, 'DOB', 6)
    elif data.iloc[i]['DOB'].split()[1] == 'July':
        data.set_value(i, 'DOB', 7)
    elif data.iloc[i]['DOB'].split()[1] == 'August':
        data.set_value(i, 'DOB', 8)
    elif data.iloc[i]['DOB'].split()[1] == 'September':
        data.set_value(i, 'DOB', 9)
    elif data.iloc[i]['DOB'].split()[1] == 'October':
        data.set_value(i, 'DOB', 10)
    elif data.iloc[i]['DOB'].split()[1] == 'November':
        data.set_value(i, 'DOB', 11)
    elif data.iloc[i]['DOB'].split()[1] == 'December':
        data.set_value(i, 'DOB', 12)


xticks=['January','February','March','April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
x = data.loc[:, 'DOB']
y = data.loc[:, 'Grade Score']
plt.scatter(x,y)
# plt.xticks(x,xticks)
plt.show()



# exams = list(data.index)
# exams = exams[0:-1]
# y_pos = np.arange(len(exams))
# numResultsPerExam = data['Exam Total'].tolist()
# numResultsPerExam = numResultsPerExam[0:-1]
#
# plt.barh(y_pos, numResultsPerExam, align='center', alpha=0.5)
# plt.yticks(y_pos, exams)
# plt.xlabel('Number Of A-Level Results')
# plt.title('Number Of A-level Result For Each Exam')
