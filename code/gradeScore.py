# Import relevant packages
import pandas as pd
import numpy as np

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour-A.xlsx")

for i in range(0,data.shape[0]):
    gradeScore = 0
    num = 0
    for j in range(5):
        if data.iloc[i]['A2 Result ' + str(j+1)] == 'A' or data.iloc[i]['A2 Result ' + str(j+1)] == 'A*':
            gradeScore += 48
            num += 1
        elif data.iloc[i]['A2 Result ' + str(j+1)] == 'B':
            gradeScore += 40
            num += 1
        elif data.iloc[i]['A2 Result ' + str(j+1)] == 'C':
            gradeScore += 32
            num += 1
        elif data.iloc[i]['A2 Result ' + str(j+1)] == 'D':
            gradeScore += 24
            num += 1
        elif data.iloc[i]['A2 Result ' + str(j+1)] == 'E':
            gradeScore += 16
            num += 1

    gradeScore = gradeScore / num

    data.set_value(i,'Grade Score', gradeScore)

# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('basicDataWithGradesAndBehaviour-A.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
