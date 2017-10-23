# Import relevant packages
import pandas as pd
import numpy as np

# Import data for set up
basicData = pd.read_excel("data/studentData.xlsx")

# Remove unnecessary columns
del basicData["Boarder Status at DOL"]
del basicData["Leaving date"]

# Add columns for future data addition
basicData["A2 Result 1"] = np.nan
basicData["A2 Result 2"] = np.nan
basicData["A2 Result 3"] = np.nan
basicData["A2 Result 4"] = np.nan

# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('basicDataSetUp.xlsx', engine='xlsxwriter')
basicData.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
