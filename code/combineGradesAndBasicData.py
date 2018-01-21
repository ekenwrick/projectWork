# Import relevant packages
import pandas as pd
import numpy as np

# Import data
basicData = pd.read_excel("basicDataSetUp.xlsx")
gradeData = pd.read_excel("gradeDataFinalGrades.xlsx")

# Use DOB and names to check for the same student
firstNameCheck = gradeData.iloc[0]['Forename']
lastNameCheck = gradeData.iloc[0]['Surname']
DOBCheck = gradeData.iloc[0]['DOB']

# Store subjects and student locations
subjectList = []
gradeList = []
newStudentStart = 0

for i in range(0,gradeData.shape[0]):
    print(i)
    if (DOBCheck == gradeData.iloc[i]['DOB'] and firstNameCheck == gradeData.iloc[i]['Forename']):

        # Append new subject an grade to the list
        subjectList.append(gradeData.iloc[i]['Subject'])
        gradeList.append(gradeData.iloc[i]['Grade'])

    else:

        for j in range(0,basicData.shape[0]):
            if (basicData.iloc[j]['Forename'] == firstNameCheck and basicData.iloc[j]['DOB'] == DOBCheck and basicData.iloc[j]['Surname'] == lastNameCheck):
                for k in range(0,len(subjectList)):
                    if k == 0:
                        basicData.set_value(j,'A2 Exam 1', subjectList[k])
                        basicData.set_value(j, 'A2 Result 1', gradeList[k])
                    elif k == 1:
                        basicData.set_value(j,'A2 Exam 2', subjectList[k])
                        basicData.set_value(j,'A2 Result 2', gradeList[k])
                    elif k == 2:
                        basicData.set_value(j,'A2 Exam 3', subjectList[k])
                        basicData.set_value(j,'A2 Result 3', gradeList[k])
                    elif k == 3:
                        basicData.set_value(j,'A2 Exam 4', subjectList[k])
                        basicData.set_value(j,'A2 Result 4', gradeList[k])
                    elif k == 4:
                        basicData.set_value(j,'A2 Exam 5', subjectList[k])
                        basicData.set_value(j,'A2 Result 5', gradeList[k])





        subjectList = []
        gradeList = []
        DOBCheck = gradeData.iloc[i]['DOB']
        firstNameCheck = gradeData.iloc[i]['Forename']
        lastNameCheck = gradeData.iloc[i]['Surname']
        newStudentStart = i

        # Append new subject and grade to the list
        subjectList.append(gradeData.iloc[i]['Subject'])
        gradeList.append(gradeData.iloc[i]['Grade'])


# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('basicDataWithGrades.xlsx', engine='xlsxwriter')
basicData.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
