# Import relevant packages
import pandas as pd
import numpy as np
import math

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour-A.xlsx")

for i in range(0,data.shape[0]):
    print(i)
    behaviourScore = 0
    num = 0
    for j in range(15, 1236):  #HARDCODED!!!! CHAGE AS AND WHEN NEEDED

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
writer = pd.ExcelWriter('basicDataWithGradesAndBehaviour-A.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
