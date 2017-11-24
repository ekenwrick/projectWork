# Import relevant packages
import pandas as pd
import numpy as np

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour.xlsx")

emptyEntries = []

# Remove rows with no exam in the first slot
for i in range(0,data.shape[0]):

    # Exam 1 entry
    entry = data.iloc[i]['A2 Exam 1']

    # Check whether string exists, if not store index
    if type(entry) is str:
        pass
    elif (np.isnan(entry)):
        emptyEntries.append(i)

# Drop empty indexs and reset index
data = data.drop(data.index[emptyEntries])
data = data.reset_index(drop=True)

# Remove name information
del data['Forename']
del data['Surname']

# Randomise row order and reset index
data = data.iloc[np.random.permutation(len(data))]
data = data.reset_index(drop=True)

# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('basicDataWithGradesAndBehaviour-A.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
