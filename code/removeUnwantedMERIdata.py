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
    individualFile = fileList[i]

    behaviouralScores = pd.read_excel("MERIdata/" + individualFile)
    scoreHeadings = list(behaviouralScores)

    if individualFile.split()[1] == '13':
        for j in range(len(scoreHeadings)):
            if scoreHeadings[j].split()[0] == 'Motivation' or scoreHeadings[j].split()[0] == 'Engagement' or scoreHeadings[j].split()[0] == 'Reflection' or scoreHeadings[j].split()[0] == 'Independent' or scoreHeadings[j].split()[0] == 'Surname':
                pass
            else:
                del behaviouralScores[scoreHeadings[j]]

        print(behaviouralScores)

        # Create pandas excel writer and write to excel
        writer = pd.ExcelWriter('MERIdata/' + individualFile, engine='xlsxwriter')
        behaviouralScores.to_excel(writer, sheet_name = 'Sheet1')
        writer.save()
