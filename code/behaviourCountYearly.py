# Import relevant packages
import pandas as pd
import numpy as np
import math

# Import data
data = pd.read_excel("yearSevenScores.xlsx")

for i in range(0,data.shape[0]):
    print(i)
    behaviourScore = 0
    num = 0

    for j in range(15, data.shape[1]):  #HARDCODED!!!! CHANGE AS AND WHEN NEEDED

        if isinstance(data.iloc[i][j], float):
            if math.isnan(data.iloc[i][j]):
                pass
            else:
                behaviourScore += data.iloc[i][j]
                num += 1


    if behaviourScore != 0:
        behaviourScore = behaviourScore / num

    data.set_value(i,'Behaviour Score', behaviourScore)

# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('yearSevenScores.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

# Import data
data = pd.read_excel("yearEightScores.xlsx")

for i in range(0,data.shape[0]):
    print(i)
    behaviourScore = 0
    num = 0

    for j in range(15, data.shape[1]):  #HARDCODED!!!! CHANGE AS AND WHEN NEEDED

        if isinstance(data.iloc[i][j], float):
            if math.isnan(data.iloc[i][j]):
                pass
            else:
                behaviourScore += data.iloc[i][j]
                num += 1


    if behaviourScore != 0:
        behaviourScore = behaviourScore / num

    data.set_value(i,'Behaviour Score', behaviourScore)

# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('yearEightScores.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

# Import data
data = pd.read_excel("yearNineScores.xlsx")

for i in range(0,data.shape[0]):
    print(i)
    behaviourScore = 0
    num = 0

    for j in range(15, data.shape[1]):  #HARDCODED!!!! CHANGE AS AND WHEN NEEDED

        if isinstance(data.iloc[i][j], float):
            if math.isnan(data.iloc[i][j]):
                pass
            else:
                behaviourScore += data.iloc[i][j]
                num += 1


    if behaviourScore != 0:
        behaviourScore = behaviourScore / num

    data.set_value(i,'Behaviour Score', behaviourScore)

# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('yearNineScores.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

# Import data
data = pd.read_excel("yearTenScores.xlsx")

for i in range(0,data.shape[0]):
    print(i)
    behaviourScore = 0
    num = 0

    for j in range(15, data.shape[1]):  #HARDCODED!!!! CHANGE AS AND WHEN NEEDED

        if isinstance(data.iloc[i][j], float):
            if math.isnan(data.iloc[i][j]):
                pass
            else:
                behaviourScore += data.iloc[i][j]
                num += 1


    if behaviourScore != 0:
        behaviourScore = behaviourScore / num

    data.set_value(i,'Behaviour Score', behaviourScore)

# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('yearTenScores.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

# Import data
data = pd.read_excel("yearElevenScores.xlsx")

for i in range(0,data.shape[0]):
    print(i)
    behaviourScore = 0
    num = 0

    for j in range(15, data.shape[1]):  #HARDCODED!!!! CHANGE AS AND WHEN NEEDED

        if isinstance(data.iloc[i][j], float):
            if math.isnan(data.iloc[i][j]):
                pass
            else:
                behaviourScore += data.iloc[i][j]
                num += 1


    if behaviourScore != 0:
        behaviourScore = behaviourScore / num

    data.set_value(i,'Behaviour Score', behaviourScore)

# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('yearElevenScores.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

# Import data
data = pd.read_excel("yearThirteenScores.xlsx")

for i in range(0,data.shape[0]):
    print(i)
    behaviourScore = 0
    num = 0

    for j in range(15, data.shape[1]):  #HARDCODED!!!! CHANGE AS AND WHEN NEEDED

        if isinstance(data.iloc[i][j], float):
            if math.isnan(data.iloc[i][j]):
                pass
            else:
                behaviourScore += data.iloc[i][j]
                num += 1


    if behaviourScore != 0:
        behaviourScore = behaviourScore / num

    data.set_value(i,'Behaviour Score', behaviourScore)

# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('yearThirteenScores.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
