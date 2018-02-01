# Import relevant packages
import pandas as pd
import numpy as np
import math
import glob

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour.xlsx")


prelimFileList = glob.glob("/Users/ethankenwrick/Documents/Uni/fourthYear/technicalProject/projectWork/code/data/ethnicity/*.xlsx")

fileList = []

# Collect file names only
for j in range(len(prelimFileList)):
    individualFile = prelimFileList[j].split('/')[-1]
    fileList.append(individualFile)

for z in range(len(fileList)):
    print(z)
    individualFile = fileList[z]

    ethnicity = pd.read_excel("data/ethnicity/" + individualFile)


    for i in range(ethnicity.shape[0]):

        surnameCheck = ethnicity.iloc[i]['Legal Surname']
        forenameCheck = ethnicity.iloc[i]['Legal Forename']

        # Get index of all matching forenmaes
        forenameIdx = data.index[data['Forename'] == forenameCheck].tolist()



        for j in range(len(forenameIdx)):
            if surnameCheck == data.iloc[forenameIdx[j]]['Surname']:
                data.set_value(forenameIdx[j], 'Ethnicity', str(ethnicity.iloc[i]['Ethnicity']))


# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('basicDataWithGradesAndBehaviour.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
