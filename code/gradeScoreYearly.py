# Import relevant packages
import pandas as pd
import numpy as np

# Import data
data = pd.read_excel("yearSevenScores.xlsx")

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
writer = pd.ExcelWriter('yearSevenScores.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()



# Import data
data = pd.read_excel("yearEightScores.xlsx")

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
writer = pd.ExcelWriter('yearEightScores.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()



# Import data
data = pd.read_excel("yearNineScores.xlsx")

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
writer = pd.ExcelWriter('yearNineScores.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()



# Import data
data = pd.read_excel("yearTenScores.xlsx")

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
writer = pd.ExcelWriter('yearTenScores.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()



# Import data
data = pd.read_excel("yearElevenScores.xlsx")

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
writer = pd.ExcelWriter('yearElevenScores.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()



# Import data
data = pd.read_excel("yearThirteenScores.xlsx")

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
writer = pd.ExcelWriter('yearThirteenScores.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
