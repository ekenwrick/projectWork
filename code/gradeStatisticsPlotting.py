# Import relevant packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import data
data = pd.read_excel("examsAndNumberOfGrades.xlsx")

# Plot different exams and number of students taking each

exams = list(data.index)
exams = exams[0:-1]
y_pos = np.arange(len(exams))
numResultsPerExam = data['Exam Total'].tolist()
numResultsPerExam = numResultsPerExam[0:-1]

plt.barh(y_pos, numResultsPerExam, align='center', alpha=0.5)
plt.yticks(y_pos, exams)
plt.xlabel('Number Of A-Level Results')
plt.title('Number Of A-level Result For Each Exam')

plt.show()


# PLot grades and number of exams achieving each grade

grades = ['A', 'B', 'C', 'D', 'E', 'U']
y_pos = np.arange(len(grades))
numEachGrade= data.loc['Grade Total', :]
numEachGrade = numEachGrade[0:-1]

plt.barh(y_pos, numEachGrade, align='center', alpha=0.5)
plt.yticks(y_pos, grades)
plt.xlabel('Number of Results')
plt.title('Number Of Results At Each Grade')


plt.show()
