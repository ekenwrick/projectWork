# Import relevant packages
import pandas as pd
import numpy as np

# Import data for set up
gradeData = pd.read_excel("data/gradeData.xlsx")

# Spread names for each entry
for i in range(1, gradeData.shape[0]):

    if(i == 1):
        firstName = gradeData.iloc[0]['Forename']
        lastName = gradeData.iloc[0]['Surname']
        DOB = gradeData.iloc[0]['DOB']

    if(pd.isnull(gradeData.iloc[i]['Forename'])):
        gradeData.set_value(i, 'Forename', firstName)
        gradeData.set_value(i, 'Surname', lastName)
        gradeData.set_value(i, 'DOB', DOB)
    else:
        firstName = gradeData.iloc[i]['Forename']
        lastName = gradeData.iloc[i]['Surname']
        DOB = gradeData.iloc[i]['DOB']


# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('gradeDataCleaned.xlsx', engine='xlsxwriter')
gradeData.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
