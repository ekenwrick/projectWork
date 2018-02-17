# Import relevant packages
import pandas as pd
import numpy as np
import math

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour-A.xlsx")


columnHeaders = list(data)

yearSeven = []
yearEight = []
yearNine = []
yearTen = []
yearEleven = []
yearThirteen = []


for i in columnHeaders:
    if 'Y7' in i or 'Year 7' in i:
        yearSeven.append(i)
    elif 'Y8' in i or 'Year 8' in i:
        yearEight.append(i)
    elif 'Y9' in i or 'Year 9' in i:
        yearNine.append(i)
    elif 'Y10' in i or 'Year 10' in i:
        yearTen.append(i)
    elif 'Y11' in i or 'Year 11' in i:
        yearEleven.append(i)
    elif 'Y13' in i or 'Year 13' in i:
        yearThirteen.append(i)

yearSevenDF = data.iloc[:, 0:15]
yearSevenDF[yearSeven] = data[yearSeven]

yearEightDF = data.iloc[:, 0:15]
yearEightDF[yearEight] = data[yearEight]

yearNineDF = data.iloc[:, 0:15]
yearNineDF[yearNine] = data[yearNine]

yearTenDF = data.iloc[:, 0:15]
yearTenDF[yearTen] = data[yearTen]

yearElevenDF = data.iloc[:, 0:15]
yearElevenDF[yearEleven] = data[yearEleven]

yearThirteenDF = data.iloc[:, 0:15]
yearThirteenDF[yearThirteen] = data[yearThirteen]


# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('yearSevenScores.xlsx', engine='xlsxwriter')
yearSevenDF.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

writer = pd.ExcelWriter('yearEightScores.xlsx', engine='xlsxwriter')
yearEightDF.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

writer = pd.ExcelWriter('yearNineScores.xlsx', engine='xlsxwriter')
yearNineDF.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

writer = pd.ExcelWriter('yearTenScores.xlsx', engine='xlsxwriter')
yearTenDF.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

writer = pd.ExcelWriter('yearElevenScores.xlsx', engine='xlsxwriter')
yearElevenDF.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

writer = pd.ExcelWriter('yearThirteenScores.xlsx', engine='xlsxwriter')
yearThirteenDF.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
