# Import relevant packages
import pandas as pd
import numpy as np

# Import data
basicData = pd.read_excel("basicDataWithGrades.xlsx")
gradeData = pd.read_excel("data/2014_A2_results_pupil.xlsx")

del gradeData[0:4]
