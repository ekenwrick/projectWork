# Import relevant packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import data
data = pd.read_excel("basicDataWithGrades-A.xlsx")

data = data.loc[:, ['DOB', 'Grade Score']]
data['DOB'].apply(str)

janScore = 0
janNum = 0
febScore = 0
febNum = 0
marScore = 0
marNum = 0
aprScore = 0
aprNum = 0
mayScore = 0
mayNum = 0
junScore = 0
junNum = 0
julScore = 0
julNum = 0
augScore = 0
augNum = 0
sepScore = 0
sepNum = 0
octScore = 0
octNum = 0
novScore = 0
novNum = 0
decScore = 0
decNum = 0


for i in range(0, data.shape[0]):

    if data.iloc[i]['DOB'].split()[1] == 'September':
        data.set_value(i, 'DOB', 1)
        sepScore += data.iloc[i]['Grade Score']
        sepNum += 1
    elif data.iloc[i]['DOB'].split()[1] == 'October':
        data.set_value(i, 'DOB', 2)
        octScore += data.iloc[i]['Grade Score']
        octNum += 1
    elif data.iloc[i]['DOB'].split()[1] == 'November':
        data.set_value(i, 'DOB', 3)
        novScore += data.iloc[i]['Grade Score']
        novNum += 1
    elif data.iloc[i]['DOB'].split()[1] == 'December':
        data.set_value(i, 'DOB', 4)
        decScore += data.iloc[i]['Grade Score']
        decNum += 1
    elif data.iloc[i]['DOB'].split()[1] == 'January':
        data.set_value(i, 'DOB', 5)
        janScore += data.iloc[i]['Grade Score']
        janNum += 1
    elif data.iloc[i]['DOB'].split()[1] == 'February':
        data.set_value(i, 'DOB', 6)
        febScore += data.iloc[i]['Grade Score']
        febNum += 1
    elif data.iloc[i]['DOB'].split()[1] == 'March':
        data.set_value(i, 'DOB', 7)
        marScore += data.iloc[i]['Grade Score']
        marNum += 1
    elif data.iloc[i]['DOB'].split()[1] == 'April':
        data.set_value(i, 'DOB', 8)
        aprScore += data.iloc[i]['Grade Score']
        aprNum += 1
    elif data.iloc[i]['DOB'].split()[1] == 'May':
        data.set_value(i, 'DOB', 9)
        mayScore += data.iloc[i]['Grade Score']
        mayNum += 1
    elif data.iloc[i]['DOB'].split()[1] == 'June':
        data.set_value(i, 'DOB', 10)
        junScore += data.iloc[i]['Grade Score']
        junNum += 1
    elif data.iloc[i]['DOB'].split()[1] == 'July':
        data.set_value(i, 'DOB', 11)
        julScore += data.iloc[i]['Grade Score']
        julNum += 1
    elif data.iloc[i]['DOB'].split()[1] == 'August':
        data.set_value(i, 'DOB', 12)
        augScore += data.iloc[i]['Grade Score']
        augNum += 1


janScore = janScore / janNum
febScore = febScore / febNum
marScore = marScore / marNum
aprScore = aprScore / aprNum
mayScore = mayScore / mayNum
junScore = junScore / junNum
julScore = julScore / julNum
augScore = augScore / augNum
sepScore = sepScore / sepNum
octScore = octScore / octNum
novScore = novScore / novNum
decScore = decScore / decNum


xticks=['September', 'October', 'November', 'December', 'January','February','March','April', 'May', 'June', 'July', 'August']
x_pos = np.arange(len(xticks)) + 1
y = [sepScore, octScore, novScore, decScore, janScore, febScore, marScore, aprScore, mayScore, junScore, julScore, augScore]

plt.scatter(x_pos,y)
plt.ylabel('Average UCAS Point Score')
plt.title('Average Students UCAS Point Score Organised By Month Of Birth')
plt.xticks(x_pos,xticks)
plt.xticks(rotation=40)
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
# plt.title('Number Of A-level Result For Each Exam' )
