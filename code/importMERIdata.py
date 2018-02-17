# Import relevant packages
import pandas as pd
import numpy as np
import math
import glob

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour.xlsx")

# Collect all files
prelimFileList = glob.glob("/Users/ethankenwrick/Documents/Uni/fourthYear/technicalProject/projectWork/code/MERIdata/*.xlsx")

# Set up empty list for names of files
fileList = []

duplicates = []

# Collect file names only
for j in range(len(prelimFileList)):
    individualFile = prelimFileList[j].split('/')[-1]
    fileList.append(individualFile)

for i in range(len(fileList)):
    print(i)

    behaviouralScores = pd.read_excel("MERIdata/" + individualFile)
    scoreHeadings = list(behaviouralScores)

    for j in range(behaviouralScores.shape[0]):
        name = behaviouralScores.iloc[j]['Surname Forename']
        forename = name.split()[1]
        surname = name.split()[0]

        # Get index of all matching forenmaes
        forenameIdx = data.index[data['Forename'] == forename].tolist()

        check = 0


        for z in range(len(forenameIdx)):
            if surname == data.iloc[forenameIdx[z]]['Surname'].upper():
                if check == 0:
                    check = 1

                    if individualFile.split()[1] == '12':
                        start = 2
                        for k in range(start, len(scoreHeadings)):
                            data.set_value(forenameIdx[z],scoreHeadings[k], str(behaviouralScores.iloc[j][scoreHeadings[k]]))

                    elif individualFile.split()[1] == '13':
                        start = 2
                        for k in range(start, len(scoreHeadings)):
                            data.set_value(forenameIdx[z],scoreHeadings[k], str(behaviouralScores.iloc[j][scoreHeadings[k]]))


# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('basicDataWithGradesAndBehaviour.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
