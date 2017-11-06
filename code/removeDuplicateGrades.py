# Import relevant packages
import pandas as pd
import numpy as np

# Import data for set up
gradeData = pd.read_excel("gradeDataGradeInformation.xlsx")

## Set up script to remove duplicate A-level scores

# Use DOB and names to check for the same student
firstNameCheck = gradeData.iloc[0]['Forename']
DOBCheck = gradeData.iloc[0]['DOB']

# Store subjects and student locations
subjectList = []
newStudentStart = 0

# Store list of rows to be deleted
rowsToDelete = []

for i in range(0,gradeData.shape[0]):
    if (DOBCheck == gradeData.iloc[i]['DOB'] and firstNameCheck == gradeData.iloc[i]['Forename']):

        #Check for repeats in subjectList
        for j in range(0, len(subjectList)):
            if subjectList[j] == gradeData.iloc[i]['Subject']:
                rowNumberToDelete = newStudentStart + j
                rowsToDelete.append(rowNumberToDelete)

        # Append new subject to the list
        subjectList.append(gradeData.iloc[i]['Subject'])

    else:
        subjectList = []
        DOBCheck = gradeData.iloc[i]['DOB']
        firstNameCheck = gradeData.iloc[i]['Forename']
        newStudentStart = i

        # Append new subject to the list
        subjectList.append(gradeData.iloc[i]['Subject'])

# Remove duplicate grades, replacing with retaken exams
rowsToDelete.sort()
gradeData = gradeData.drop(gradeData.index[rowsToDelete])

# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('gradeDataFinalGrades.xlsx', engine='xlsxwriter')
gradeData.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
