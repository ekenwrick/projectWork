# Import relevant packages
import pandas as pd
import numpy as np

# Import data for set up
basicData = pd.read_excel("data/studentData.xlsx")

# Remove unnecessary columns
del basicData["Boarder Status at DOL"]
del basicData["Leaving date"]



# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('basicDataSetUp.xlsx', engine='xlsxwriter')
basicData.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
