#### RUN ANONYMISEDATA FIRST
# Import relevant packages
import pandas as pd
import numpy as np

# Import data
data = pd.read_excel("basicDataWithGradesAndBehaviour-A.xlsx")


# Loop through exams and remove codes
for i in range(0,5):
    for j in range(data.shape[0]):

        # For each column, split on the dash and take the name of the exam only
        if i == 0:
            entry = data.iloc[j]['A2 Exam 1']
            if len(entry.split('-')) > 1:
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
                elif entry.split('-')[1]  == 'Classical Civilisation' or entry.split('-')[1]  == 'Classics (General)':
                    data.set_value(j,'A2 Exam 1', 'Classics')
                elif entry.split('-')[1]  == 'English Language & Literature' or entry.split('-')[1]  == 'English Literature':
                    data.set_value(j,'A2 Exam 1', 'English')
                elif entry.split('-')[1] == 'Fine Art' or entry.split('-')[1] == 'Art and Design':
                    data.set_value(j,'A2 Exam 1', 'Art')
                elif entry.split('-')[1]  == 'Product Design' or entry.split('-')[1]  == 'D & T: Product Design':
                    data.set_value(j,'A2 Exam 1', 'D&T Product Design')
                elif entry.split('-')[1] == 'Performing Arts':
                    data.set_value(j,'A2 Exam 1', 'Drama')
                else:
                    data.set_value(j,'A2 Exam 1', entry.split('-')[1])
            else:
                entry = entry.rsplit(None, -1)[0]
                if entry == 'Mathematics':
                    data.set_value(j,'A2 Exam 1', 'Maths (General)')
                elif entry == 'Mathematics Further' or entry == 'Further Mathematics' or entry == 'Further':
                    data.set_value(j,'A2 Exam 1', 'Maths (Further)')
                elif entry == 'Music Studies' or entry == 'Classical':
                    data.set_value(j,'A2 Exam 1', 'Music')
                elif entry == 'Sport/PE Studies' or entry == 'Sports Studies':
                    data.set_value(j,'A2 Exam 1', 'Sport')
                elif entry == 'Logic (Philosophy)' or entry == 'Philosophy (Theory)' or entry == 'Logic/Philosophy':
                    data.set_value(j,'A2 Exam 1', 'Philosophy')
                elif entry == 'Greek (Classic)':
                    data.set_value(j,'A2 Exam 1', 'Greek')
                elif entry == 'Art and Design  Photography' or entry == 'Art & Des (Photography)':
                    data.set_value(j,'A2 Exam 1', 'Photography')
                elif entry == 'Product Design' or entry == 'D & T: Product Design':
                    data.set_value(j,'A2 Exam 1', 'D&T Product Design')
                elif entry == 'English Language & Literature' or entry == 'English Literature' or entry == 'English Lang. & Lit.':
                    data.set_value(j,'A2 Exam 1', 'English')
                elif entry == 'Classical Civilisation' or entry == 'Classics (General)':
                    data.set_value(j,'A2 Exam 1', 'Classics')
                elif entry == 'Performing Arts' or entry == 'Drama & Theatre Stds':
                    data.set_value(j,'A2 Exam 1', 'Drama')
                elif entry == 'Fine Art' or entry == 'Art and Design' or entry == 'Fine':
                    data.set_value(j,'A2 Exam 1', 'Art')
                elif entry == 'Computer' or entry == 'Computer Studies/Computing' or entry == 'Comp Sci' or entry == 'Comp':
                    data.set_value(j,'A2 Exam 1', 'Computer Science')
                else:
                    data.set_value(j,'A2 Exam 1', entry)

        elif i == 1:
            entry = data.iloc[j]['A2 Exam 2']
            if type(entry) is str:
                if len(entry.split('-')) > 1:
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
                    elif entry.split('-')[1]  == 'Classical Civilisation' or entry.split('-')[1]  == 'Classics (General)':
                        data.set_value(j,'A2 Exam 2', 'Classics')
                    elif entry.split('-')[1]  == 'English Language & Literature' or entry.split('-')[1]  == 'English Literature':
                        data.set_value(j,'A2 Exam 2', 'English')
                    elif entry.split('-')[1] == 'Fine Art' or entry.split('-')[1] == 'Art and Design':
                        data.set_value(j,'A2 Exam 2', 'Art')
                    elif entry.split('-')[1]  == 'Product Design' or entry.split('-')[1]  == 'D & T: Product Design':
                        data.set_value(j,'A2 Exam 2', 'D&T Product Design')
                    elif entry.split('-')[1] == 'Performing Arts':
                        data.set_value(j,'A2 Exam 2', 'Drama')
                    else:
                        data.set_value(j,'A2 Exam 2', entry.split('-')[1])
                else:
                    entry = entry.rsplit(None, 0)[0]
                    if entry == 'Mathematics':
                        data.set_value(j,'A2 Exam 2', 'Maths (General)')
                    elif entry == 'Mathematics Further' or entry == 'Further Mathematics' or entry == 'Further':
                        data.set_value(j,'A2 Exam 2', 'Maths (Further)')
                    elif entry == 'Music Studies' or entry == 'Classical':
                        data.set_value(j,'A2 Exam 2', 'Music')
                    elif entry == 'Sport/PE Studies' or entry == 'Sports Studies':
                        data.set_value(j,'A2 Exam 2', 'Sport')
                    elif entry == 'Logic (Philosophy)' or entry == 'Philosophy (Theory)' or entry == 'Logic/Philosophy':
                        data.set_value(j,'A2 Exam 2', 'Philosophy')
                    elif entry == 'Greek (Classic)':
                        data.set_value(j,'A2 Exam 2', 'Greek')
                    elif entry == 'Art and Design  Photography' or entry == 'Art & Des (Photography)':
                        data.set_value(j,'A2 Exam 2', 'Photography')
                    elif entry == 'Product Design' or entry == 'D & T: Product Design':
                        data.set_value(j,'A2 Exam 2', 'D&T Product Design')
                    elif entry == 'English Language & Literature' or entry == 'English Literature' or entry == 'English Lang. & Lit.':
                        data.set_value(j,'A2 Exam 2', 'English')
                    elif entry == 'Classical Civilisation' or entry == 'Classics (General)':
                        data.set_value(j,'A2 Exam 2', 'Classics')
                    elif entry == 'Performing Arts' or entry == 'Drama & Theatre Stds':
                        data.set_value(j,'A2 Exam 2', 'Drama')
                    elif entry == 'Fine Art' or entry == 'Art and Design' or entry == 'Fine':
                        data.set_value(j,'A2 Exam 2', 'Art')
                    elif entry == 'Computer' or entry == 'Computer Studies/Computing' or entry == 'Comp Sci' or entry == 'Comp':
                        data.set_value(j,'A2 Exam 2', 'Computer Science')
                    else:
                        data.set_value(j,'A2 Exam 2', entry)

        elif i == 2:
            entry = data.iloc[j]['A2 Exam 3']
            if type(entry) is str:
                if len(entry.split('-')) > 1:
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
                    elif entry.split('-')[1]  == 'Classical Civilisation' or entry.split('-')[1]  == 'Classics (General)':
                        data.set_value(j,'A2 Exam 3', 'Classics')
                    elif entry.split('-')[1]  == 'English Language & Literature' or entry.split('-')[1]  == 'English Literature':
                        data.set_value(j,'A2 Exam 3', 'English')
                    elif entry.split('-')[1] == 'Fine Art' or entry.split('-')[1] == 'Art and Design':
                        data.set_value(j,'A2 Exam 3', 'Art')
                    elif entry.split('-')[1]  == 'Product Design' or entry.split('-')[1]  == 'D & T: Product Design':
                        data.set_value(j,'A2 Exam 3', 'D&T Product Design')
                    elif entry.split('-')[1] == 'Performing Arts':
                        data.set_value(j,'A2 Exam 3', 'Drama')
                    else:
                        data.set_value(j,'A2 Exam 3', entry.split('-')[1])
                else:
                    entry = entry.rsplit(None, 0)[0]
                    if entry == 'Mathematics':
                        data.set_value(j,'A2 Exam 3', 'Maths (General)')
                    elif entry == 'Mathematics Further' or entry == 'Further Mathematics' or entry == 'Further':
                        data.set_value(j,'A2 Exam 3', 'Maths (Further)')
                    elif entry == 'Music Studies' or entry == 'Classical':
                        data.set_value(j,'A2 Exam 3', 'Music')
                    elif entry == 'Sport/PE Studies' or entry == 'Sports Studies':
                        data.set_value(j,'A2 Exam 3', 'Sport')
                    elif entry == 'Logic (Philosophy)' or entry == 'Philosophy (Theory)' or entry == 'Logic/Philosophy':
                        data.set_value(j,'A2 Exam 3', 'Philosophy')
                    elif entry == 'Greek (Classic)':
                        data.set_value(j,'A2 Exam 3', 'Greek')
                    elif entry == 'Art and Design  Photography' or entry == 'Art & Des (Photography)':
                        data.set_value(j,'A2 Exam 3', 'Photography')
                    elif entry == 'Product Design' or entry == 'D & T: Product Design':
                        data.set_value(j,'A2 Exam 3', 'D&T Product Design')
                    elif entry == 'English Language & Literature' or entry == 'English Literature' or entry == 'English Lang. & Lit.':
                        data.set_value(j,'A2 Exam 3', 'English')
                    elif entry == 'Classical Civilisation' or entry == 'Classics (General)':
                        data.set_value(j,'A2 Exam 3', 'Classics')
                    elif entry == 'Performing Arts' or entry == 'Drama & Theatre Stds':
                        data.set_value(j,'A2 Exam 3', 'Drama')
                    elif entry == 'Fine Art' or entry == 'Art and Design' or entry == 'Fine':
                        data.set_value(j,'A2 Exam 3', 'Art')
                    elif entry == 'Computer' or entry == 'Computer Studies/Computing' or entry == 'Comp Sci' or entry == 'Comp':
                        data.set_value(j,'A2 Exam 3', 'Computer Science')
                    else:
                        data.set_value(j,'A2 Exam 3', entry)

        elif i == 3:
            entry = data.iloc[j]['A2 Exam 4']
            if type(entry) is str:
                if len(entry.split('-')) > 1:
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
                    elif entry.split('-')[1]  == 'Classical Civilisation' or entry.split('-')[1]  == 'Classics (General)':
                        data.set_value(j,'A2 Exam 4', 'Classics')
                    elif entry.split('-')[1]  == 'English Language & Literature' or entry.split('-')[1]  == 'English Literature':
                        data.set_value(j,'A2 Exam 4', 'English')
                    elif entry.split('-')[1] == 'Fine Art' or entry.split('-')[1] == 'Art and Design':
                        data.set_value(j,'A2 Exam 4', 'Art')
                    elif entry.split('-')[1]  == 'Product Design' or entry.split('-')[1]  == 'D & T: Product Design':
                        data.set_value(j,'A2 Exam 4', 'D&T Product Design')
                    elif entry.split('-')[1] == 'Performing Arts':
                        data.set_value(j,'A2 Exam 4', 'Drama')
                    else:
                        data.set_value(j,'A2 Exam 4', entry.split('-')[1])
                else:
                    entry = entry.rsplit(None, 0)[0]
                    if entry == 'Mathematics':
                        data.set_value(j,'A2 Exam 4', 'Maths (General)')
                    elif entry == 'Mathematics Further' or entry == 'Further Mathematics' or entry == 'Further':
                        data.set_value(j,'A2 Exam 4', 'Maths (Further)')
                    elif entry == 'Music Studies' or entry == 'Classical':
                        data.set_value(j,'A2 Exam 4', 'Music')
                    elif entry == 'Sport/PE Studies' or entry == 'Sports Studies':
                        data.set_value(j,'A2 Exam 4', 'Sport')
                    elif entry == 'Logic (Philosophy)' or entry == 'Philosophy (Theory)' or entry == 'Logic/Philosophy':
                        data.set_value(j,'A2 Exam 4', 'Philosophy')
                    elif entry == 'Greek (Classic)':
                        data.set_value(j,'A2 Exam 4', 'Greek')
                    elif entry == 'Art and Design  Photography' or entry == 'Art & Des (Photography)':
                        data.set_value(j,'A2 Exam 4', 'Photography')
                    elif entry == 'Product Design' or entry == 'D & T: Product Design':
                        data.set_value(j,'A2 Exam 4', 'D&T Product Design')
                    elif entry == 'English Language & Literature' or entry == 'English Literature' or entry == 'English Lang. & Lit.':
                        data.set_value(j,'A2 Exam 4', 'English')
                    elif entry == 'Classical Civilisation' or entry == 'Classics (General)':
                        data.set_value(j,'A2 Exam 4', 'Classics')
                    elif entry == 'Performing Arts' or entry == 'Drama & Theatre Stds':
                        data.set_value(j,'A2 Exam 4', 'Drama')
                    elif entry == 'Fine Art' or entry == 'Art and Design' or entry == 'Fine':
                        data.set_value(j,'A2 Exam 4', 'Art')
                    elif entry == 'Computer' or entry == 'Computer Studies/Computing' or entry == 'Comp Sci' or entry == 'Comp':
                        data.set_value(j,'A2 Exam 4', 'Computer Science')
                    else:
                        data.set_value(j,'A2 Exam 4', entry)

        elif i == 4:
            entry = data.iloc[j]['A2 Exam 5']
            if type(entry) is str:
                if len(entry.split('-')) > 1:
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
                    elif entry.split('-')[1]  == 'Classical Civilisation' or entry.split('-')[1]  == 'Classics (General)':
                        data.set_value(j,'A2 Exam 5', 'Classics')
                    elif entry.split('-')[1]  == 'English Language & Literature' or entry.split('-')[1]  == 'English Literature':
                        data.set_value(j,'A2 Exam 5', 'English')
                    elif entry.split('-')[1] == 'Fine Art' or entry.split('-')[1] == 'Art and Design':
                        data.set_value(j,'A2 Exam 5', 'Art')
                    elif entry.split('-')[1]  == 'Product Design' or entry.split('-')[1]  == 'D & T: Product Design':
                        data.set_value(j,'A2 Exam 5', 'D&T Product Design')
                    elif entry.split('-')[1] == 'Performing Arts':
                        data.set_value(j,'A2 Exam 5', 'Drama')
                    else:
                        data.set_value(j,'A2 Exam 5', entry.split('-')[1])
                else:
                    entry = entry.rsplit(None, 0)[0]
                    if entry == 'Mathematics':
                        data.set_value(j,'A2 Exam 5', 'Maths (General)')
                    elif entry == 'Mathematics Further' or entry == 'Further Mathematics' or entry == 'Further':
                        data.set_value(j,'A2 Exam 5', 'Maths (Further)')
                    elif entry == 'Music Studies' or entry == 'Classical':
                        data.set_value(j,'A2 Exam 5', 'Music')
                    elif entry == 'Sport/PE Studies' or entry == 'Sports Studies':
                        data.set_value(j,'A2 Exam 5', 'Sport')
                    elif entry == 'Logic (Philosophy)' or entry == 'Philosophy (Theory)' or entry == 'Logic/Philosophy':
                        data.set_value(j,'A2 Exam 5', 'Philosophy')
                    elif entry == 'Greek (Classic)':
                        data.set_value(j,'A2 Exam 5', 'Greek')
                    elif entry == 'Art and Design  Photography' or entry == 'Art & Des (Photography)':
                        data.set_value(j,'A2 Exam 5', 'Photography')
                    elif entry == 'Product Design' or entry == 'D & T: Product Design':
                        data.set_value(j,'A2 Exam 5', 'D&T Product Design')
                    elif entry == 'English Language & Literature' or entry == 'English Literature' or entry == 'English Lang. & Lit.':
                        data.set_value(j,'A2 Exam 5', 'English')
                    elif entry == 'Classical Civilisation' or entry == 'Classics (General)':
                        data.set_value(j,'A2 Exam 5', 'Classics')
                    elif entry == 'Performing Arts' or entry == 'Drama & Theatre Stds':
                        data.set_value(j,'A2 Exam 5', 'Drama')
                    elif entry == 'Fine Art' or entry == 'Art and Design' or entry == 'Fine':
                        data.set_value(j,'A2 Exam 5', 'Art')
                    elif entry == 'Computer' or entry == 'Computer Studies/Computing' or entry == 'Comp Sci' or entry == 'Comp':
                        data.set_value(j,'A2 Exam 5', 'Computer Science')
                    else:
                        data.set_value(j,'A2 Exam 5', entry)



# Create pandas excel writer and write to excel
writer = pd.ExcelWriter('basicDataWithGradesAndBehaviour-A.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name = 'Sheet1')
writer.save()
