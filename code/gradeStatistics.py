# Import relevant packages
import pandas as pd
import numpy as np

# Import data
data = pd.read_excel("basicDataWithGrades-A.xlsx")

# Collect exam and results columns
examsTaken = data.loc[:, ['A2 Exam 1', 'A2 Exam 2', 'A2 Exam 3', 'A2 Exam 4', 'A2 Exam 5']]
results = data.loc[:, ['A2 Result 1', 'A2 Result 2', 'A2 Result 3', 'A2 Result 4', 'A2 Result 5']]

# Find all different entries
uniqueExams = examsTaken.stack().unique()
uniqueResults = results.stack().unique()

# Count up all different entries
totalExams = examsTaken.stack().value_counts()
totalResults = results.stack().value_counts()



print(uniqueExams[1])
print(uniqueResults)

columns = uniqueResults
index = uniqueExams

examsDataFrame = pd.DataFrame(index=index, columns=columns)
examsDataFrame = examsDataFrame.fillna(0)

for i in range(0,uniqueExams.shape[0]):
    for j in range(0,examsTaken.shape[0]):
        for k in range(0,5):
            if k == 0:
                examCheck = examsTaken.iloc[j]['A2 Exam 1']
                if examCheck == uniqueExams[i]:
                    examResult = results.iloc[j]['A2 Result 1']
                    currentCount = int(examsDataFrame.loc[examCheck][examResult])
                    examsDataFrame.set_value(examCheck, examResult, (currentCount + 1))
            elif k == 1:
                examCheck = examsTaken.iloc[j]['A2 Exam 2']
                if examCheck == uniqueExams[i]:
                    examResult = results.iloc[j]['A2 Result 2']
                    currentCount = int(examsDataFrame.loc[examCheck][examResult])
                    examsDataFrame.set_value(examCheck, examResult, (currentCount + 1))
            elif k == 2:
                examCheck = examsTaken.iloc[j]['A2 Exam 3']
                if examCheck == uniqueExams[i]:
                    examResult = results.iloc[j]['A2 Result 3']
                    currentCount = int(examsDataFrame.loc[examCheck][examResult])
                    examsDataFrame.set_value(examCheck, examResult, (currentCount + 1))
            elif k == 3:
                examCheck = examsTaken.iloc[j]['A2 Exam 4']
                if examCheck == uniqueExams[i]:
                    examResult = results.iloc[j]['A2 Result 4']
                    currentCount = int(examsDataFrame.loc[examCheck][examResult])
                    examsDataFrame.set_value(examCheck, examResult, (currentCount + 1))
            elif k == 4:
                examCheck = examsTaken.iloc[j]['A2 Exam 5']
                if examCheck == uniqueExams[i]:
                    examResult = results.iloc[j]['A2 Result 5']
                    currentCount = int(examsDataFrame.loc[examCheck][examResult])
                    examsDataFrame.set_value(examCheck, examResult, (currentCount + 1))

print(examsDataFrame)
