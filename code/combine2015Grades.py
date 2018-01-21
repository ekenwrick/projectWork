# Import relevant packages
import pandas as pd
import numpy as np

# Import data
basicData = pd.read_excel("basicDataWithGradesAndBehaviour.xlsx")
gradeData = pd.read_excel("data/2015_A_Student_results.xlsx")

dataFrameHeaders = list(gradeData)

for i in range(gradeData.shape[0]):

    # Store subjects and student locations
    subjectList = []
    gradeList = []

    # Set up checks
    firstNameCheck = str(gradeData.iloc[i][0]).split(' ')[1]
    lastNameCheck = str(gradeData.iloc[i][0]).split(' ')[0]

    for j in range(1, gradeData.shape[1]):

        entry = gradeData.iloc[i][j]

        if type(entry) is str:
            gradeList.append(entry)
            subjectList.append(dataFrameHeaders[j])

    check = 0

    # Get index of all matching forenmaes
    forenameIdx = basicData.index[basicData['Forename'] == firstNameCheck].tolist()

    for z in range(len(forenameIdx)):
        if lastNameCheck == basicData.iloc[forenameIdx[z]]['Surname']:

            for k in range(0,len(subjectList)):
                if k == 0:
                    basicData.set_value(forenameIdx[z],'A2 Exam 1', subjectList[k])
                    basicData.set_value(forenameIdx[z], 'A2 Result 1', gradeList[k])
                elif k == 1:
                    basicData.set_value(forenameIdx[z],'A2 Exam 2', subjectList[k])
                    basicData.set_value(forenameIdx[z],'A2 Result 2', gradeList[k])
                elif k == 2:
                    basicData.set_value(forenameIdx[z],'A2 Exam 3', subjectList[k])
                    basicData.set_value(forenameIdx[z],'A2 Result 3', gradeList[k])
                elif k == 3:
                    basicData.set_value(forenameIdx[z],'A2 Exam 4', subjectList[k])
                    basicData.set_value(forenameIdx[z],'A2 Result 4', gradeList[k])
                elif k == 4:
                    basicData.set_value(forenameIdx[z],'A2 Exam 5', subjectList[k])
                    basicData.set_value(forenameIdx[z],'A2 Result 5', gradeList[k])


# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('basicDataWithGradesAndBehaviour.xlsx', engine='xlsxwriter')
basicData.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
