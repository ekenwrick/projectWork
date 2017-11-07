# Import relevant packages
import pandas as pd
import numpy as np

# Import data
data = pd.read_excel("basicDataWithGrades-A.xlsx")


examsTaken = data.loc[:, ['A2 Exam 1', 'A2 Exam 2', 'A2 Exam 3', 'A2 Exam 4', 'A2 Exam 5']]
results = data.loc[:, ['A2 Result 1', 'A2 Result 2', 'A2 Result 3', 'A2 Result 4', 'A2 Result 5']]

uniqueExams = examsTaken.stack().unique()
uniqueResults = results.stack().unique()

totalExams = examsTaken.stack().value_counts()
totalResults = results.stack().value_counts()

print(totalExams)
print(totalResults)

#for i in range(0,len(uniqueExams)):
#    print(uniqueExams[i])
