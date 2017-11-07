# Import relevant packages
import pandas as pd
import numpy as np

# Import data
data = pd.read_excel("basicDataWithGrades.xlsx")

# Remove name information
del data['Forename']
del data['Surname']

# Randomise row order and reset index
data = data.iloc[np.random.permutation(len(data))]
data = data.reset_index(drop=True)

# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('basicDataWithGrades-A.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
