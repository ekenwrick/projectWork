# Import relevant packages
import pandas as pd
import numpy as np
import math

# Import data
data = pd.read_excel("data/beh.xlsx")

# Set up code
nameCount = 1;
nameLoc = 0;

# Collect number of times each name appears
for i in range(data.shape[0]):

    if i == 0:
        nameLoc = i
    else:
        if pd.isnull(data.iloc[i]['Forename']):
            nameCount += 1
        else:
            if pd.isnull(data.iloc[i - 1]['Type']):
                data.set_value(nameLoc, 'Count', 0)
                nameLoc = i
                nameCount = 1
            else:
                data.set_value(nameLoc, 'Count', nameCount)
                nameLoc = i
                nameCount = 1

    # HARDCODED - fine for this data
    if i == data.shape[0]:
        data.set_value(i, 'Count', 0)

print(data)


# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('behaviourNotesCounted.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
