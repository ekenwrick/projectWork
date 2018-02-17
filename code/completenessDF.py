# Import relevant packages
import pandas as pd
import numpy as np
import math

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour-A.xlsx")

completeness = data.count()

print(type(completeness))

completeness = completeness.to_frame()

completeness = completeness.sort_values(0, ascending=[False])
completeness = completeness.drop(completeness.index[0:17])

rowsToDelete = []

for i in range(completeness.shape[0]):
    if completeness.iloc[i][0] <= 10:
        rowsToDelete.append(i)

completeness = completeness.drop(completeness.index[rowsToDelete])

indexValues = completeness.index

print(completeness)
