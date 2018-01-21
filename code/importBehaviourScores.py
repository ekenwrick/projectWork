# Import relevant packages
import pandas as pd
import numpy as np
import math
import glob

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour.xlsx")

# Collect all files
prelimFileList = glob.glob("/Users/ethankenwrick/Documents/Uni/fourthYear/technicalProject/projectWork/code/data/behaviouralData/*.xlsx")

# Set up empty list for names of files
fileList = []

duplicates = []

# Collect file names only
for j in range(len(prelimFileList)):
    individualFile = prelimFileList[j].split('/')[-1]
    fileList.append(individualFile)

# Put data from all files into overall data set
for i in range(len(fileList)):
    individualFile = fileList[i]
    if individualFile == 'MATRIX OF DATA FOR CPR.xlsx':
        pass

    else:

        year = individualFile.split()[1]
        behaviouralScores = pd.read_excel("data/behaviouralData/" + individualFile)
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

                        if individualFile == 'YEAR 7 2012-13 PHOB.xlsx' or individualFile == 'YEAR 7 2013-14 PHOB.xlsx' or individualFile == 'YEAR 7 2014-15 PHOB.xlsx':
                            start = 5
                            for k in range(start, len(scoreHeadings)):
                                data.set_value(forenameIdx[z],scoreHeadings[k], str(behaviouralScores.iloc[j][scoreHeadings[k]]))

                        elif individualFile == 'YEAR 8 2012-13 PHOB.xlsx' or individualFile == 'YEAR 8 2013-14 PHOB.xlsx' or individualFile == 'YEAR 8 2014-15 PHOB.xlsx' or individualFile == 'YEAR 9 2012-13 PHOB.xlsx' or individualFile == 'YEAR 9 2013-14 PHOB.xlsx' or individualFile == 'YEAR 9 2014-15 PHOB.xlsx' or individualFile == 'YEAR 10 2012-13 PHOB.xlsx' or individualFile == 'YEAR 10 2013-14 PHOB.xlsx' or individualFile == 'YEAR 10 2014-155 PHOB.xlsx':
                            start = 3
                            for k in range(start, len(scoreHeadings)):
                                data.set_value(forenameIdx[z],scoreHeadings[k], str(behaviouralScores.iloc[j][scoreHeadings[k]]))

                        elif individualFile == 'YEAR 11 2012-13 PHOB.xlsx':
                            start = 4
                            for k in range(start, len(scoreHeadings)):
                                data.set_value(forenameIdx[z],scoreHeadings[k], str(behaviouralScores.iloc[j][scoreHeadings[k]]))





                    else:
                        # Collect names of duplicates so they can be entered manually
                        duplicates.append(forename + ' ' + surname + ' File: ' + individualFile)




# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('basicDataWithGradesAndBehaviour.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
