# Import relevant packages
import pandas as pd
import numpy as np

# Import data for set up
gradeDataCleaned = pd.read_excel("gradeDataCloneID.xlsx")

# Remove unnecessary columns
del gradeDataCleaned["Exam name"]
del gradeDataCleaned["Exam number"]
del gradeDataCleaned["Qualification"]
del gradeDataCleaned["Result set"]

# Remove all rows where grade is noted as 'Y'
wantedRowsForGrade = gradeDataCleaned.loc[gradeDataCleaned['Grade'] != 'Y']
wantedRowsForGrade = wantedRowsForGrade.loc[wantedRowsForGrade['Grade'] != 'N']
wantedRowsForGrade = wantedRowsForGrade[pd.notnull(wantedRowsForGrade['Level'])]
wantedRowsForGrade = wantedRowsForGrade.loc[wantedRowsForGrade['Level'] == 'GCE/ASB']
wantedRowsForGrade = wantedRowsForGrade.loc[~wantedRowsForGrade['Grade'].astype(str).str.isdigit()]

# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('gradeDataGradeInformation.xlsx', engine='xlsxwriter')
wantedRowsForGrade.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
