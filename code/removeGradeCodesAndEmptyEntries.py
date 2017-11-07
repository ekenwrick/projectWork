#### RUN ANONYMISEDATA FIRST
# Import relevant packages
import pandas as pd
import numpy as np

# Import data
data = pd.read_excel("basicDataWithGrades-A.xlsx")

dataLength = data.shape[0]

emptyEntries = []

# Remove rows with no exam in the first slot
for i in range(0,dataLength):

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



# Loop through exams and remove codes
for i in range(0,5):
    for j in range(data.shape[0]):

        # For each column, split on the dash and take the name of the exam only
        if i == 0:
            entry = data.iloc[j]['A2 Exam 1']
            if entry.split('-')[1] == 'Mathematics':
                data.set_value(j,'A2 Exam 1', 'Maths (General)')
            elif entry.split('-')[1] == 'Mathematics Further':
                data.set_value(j,'A2 Exam 1', 'Maths (Further)')
            elif entry.split('-')[1] == 'Music Studies':
                data.set_value(j,'A2 Exam 1', 'Music')
            elif entry.split('-')[1] == 'Sport/PE Studies' or entry.split('-')[1] == 'Sports Studies':
                data.set_value(j,'A2 Exam 1', 'Sport')
            elif entry.split('-')[1] == 'Logic (Philosophy)' or entry.split('-')[1] == 'Philosophy (Theory)' or entry.split('-')[1] == 'Logic/Philosophy':
                data.set_value(j,'A2 Exam 1', 'Philosophy')
            elif entry.split('-')[1] == 'Greek (Classic)':
                data.set_value(j,'A2 Exam 1', 'Greek')
            elif entry.split('-')[1] == 'Art and Design  Photography':
                data.set_value(j,'A2 Exam 1', 'Photography')
            else:
                data.set_value(j,'A2 Exam 1', entry.split('-')[1])
        elif i == 1:
            entry = data.iloc[j]['A2 Exam 2']
            if type(entry) is str:
                if entry.split('-')[1] == 'Mathematics':
                    data.set_value(j,'A2 Exam 2', 'Maths (General)')
                elif entry.split('-')[1] == 'Mathematics Further':
                    data.set_value(j,'A2 Exam 2', 'Maths (Further)')
                elif entry.split('-')[1] == 'Music Studies':
                    data.set_value(j,'A2 Exam 2', 'Music')
                elif entry.split('-')[1] == 'Sport/PE Studies' or entry.split('-')[1] == 'Sports Studies':
                    data.set_value(j,'A2 Exam 2', 'Sport')
                elif entry.split('-')[1] == 'Logic (Philosophy)' or entry.split('-')[1] == 'Philosophy (Theory)' or entry.split('-')[1] == 'Logic/Philosophy':
                    data.set_value(j,'A2 Exam 2', 'Philosophy')
                elif entry.split('-')[1] == 'Greek (Classic)':
                    data.set_value(j,'A2 Exam 2', 'Greek')
                elif entry.split('-')[1] == 'Art and Design  Photography':
                    data.set_value(j,'A2 Exam 2', 'Photography')
                else:
                    data.set_value(j,'A2 Exam 2', entry.split('-')[1])
        elif i == 2:
            entry = data.iloc[j]['A2 Exam 3']
            if type(entry) is str:
                if entry.split('-')[1] == 'Mathematics':
                    data.set_value(j,'A2 Exam 3', 'Maths (General)')
                elif entry.split('-')[1] == 'Mathematics Further':
                    data.set_value(j,'A2 Exam 3', 'Maths (Further)')
                elif entry.split('-')[1] == 'Music Studies':
                    data.set_value(j,'A2 Exam 3', 'Music')
                elif entry.split('-')[1] == 'Sport/PE Studies' or entry.split('-')[1] == 'Sports Studies':
                    data.set_value(j,'A2 Exam 3', 'Sport')
                elif entry.split('-')[1] == 'Logic (Philosophy)' or entry.split('-')[1] == 'Philosophy (Theory)' or entry.split('-')[1] == 'Logic/Philosophy':
                    data.set_value(j,'A2 Exam 3', 'Philosophy')
                elif entry.split('-')[1] == 'Greek (Classic)':
                    data.set_value(j,'A2 Exam 3', 'Greek')
                elif entry.split('-')[1] == 'Art and Design  Photography':
                    data.set_value(j,'A2 Exam 3', 'Photography')
                else:
                    data.set_value(j,'A2 Exam 3', entry.split('-')[1])
        elif i == 3:
            entry = data.iloc[j]['A2 Exam 4']
            if type(entry) is str:
                if entry.split('-')[1] == 'Mathematics':
                    data.set_value(j,'A2 Exam 4', 'Maths (General)')
                elif entry.split('-')[1] == 'Mathematics Further':
                    data.set_value(j,'A2 Exam 4', 'Maths (Further)')
                elif entry.split('-')[1] == 'Music Studies':
                    data.set_value(j,'A2 Exam 4', 'Music')
                elif entry.split('-')[1] == 'Sport/PE Studies' or entry.split('-')[1] == 'Sports Studies':
                    data.set_value(j,'A2 Exam 4', 'Sport')
                elif entry.split('-')[1] == 'Logic (Philosophy)' or entry.split('-')[1] == 'Philosophy (Theory)' or entry.split('-')[1] == 'Logic/Philosophy':
                    data.set_value(j,'A2 Exam 4', 'Philosophy')
                elif entry.split('-')[1] == 'Greek (Classic)':
                    data.set_value(j,'A2 Exam 4', 'Greek')
                elif entry.split('-')[1] == 'Art and Design  Photography':
                    data.set_value(j,'A2 Exam 4', 'Photography')
                else:
                    data.set_value(j,'A2 Exam 4', entry.split('-')[1])
        elif i == 4:
            entry = data.iloc[j]['A2 Exam 5']
            if type(entry) is str:
                if entry.split('-')[1] == 'Mathematics':
                    data.set_value(j,'A2 Exam 5', 'Maths (General)')
                elif entry.split('-')[1] == 'Mathematics Further':
                    data.set_value(j,'A2 Exam 5', 'Maths (Further)')
                elif entry.split('-')[1] == 'Music Studies':
                    data.set_value(j,'A2 Exam 5', 'Music')
                elif entry.split('-')[1] == 'Sport/PE Studies' or entry.split('-')[1] == 'Sports Studies':
                    data.set_value(j,'A2 Exam 5', 'Sport')
                elif entry.split('-')[1] == 'Logic (Philosophy)' or entry.split('-')[1] == 'Philosophy (Theory)' or entry.split('-')[1] == 'Logic/Philosophy':
                    data.set_value(j,'A2 Exam 5', 'Philosophy')
                elif entry.split('-')[1] == 'Greek (Classic)':
                    data.set_value(j,'A2 Exam 5', 'Greek')
                elif entry.split('-')[1] == 'Art and Design  Photography':
                    data.set_value(j,'A2 Exam 5', 'Photography')
                else:
                    data.set_value(j,'A2 Exam 5', entry.split('-')[1])
        print(i)


# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('basicDataWithGrades-A.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
