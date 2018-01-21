# Import relevant packages
import pandas as pd
import numpy as np
import math

# Import data
behaviourData = pd.read_excel("behaviourNotesCounted.xlsx")
data = pd.read_excel("basicDataWithGradesAndBehaviour.xlsx")

for i in range(behaviourData.shape[0]):
    if pd.isnull(behaviourData.iloc[i]['Forename']):
        pass
    else:

        forename = behaviourData.iloc[i]['Forename']
        surname = behaviourData.iloc[i]['Surname']
        behaviourCount = behaviourData.iloc[i]['Count']

        # Get index of all matching forenmaes
        forenameIdx = data.index[data['Forename'] == forename].tolist()

        # Find matching surnames and store corresponding behaviour counts
        for j in range(len(forenameIdx)):
            if surname == data.iloc[forenameIdx[j]]['Surname']:
                data.set_value(forenameIdx[j], 'Behaviour Count', behaviourCount)



# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('basicDataWithGradesAndBehaviour.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
