
## Topic: How to Deal with Missing Data in Python

# During the process of data exploration, it is not unommon to realize that the data we have is incomplete.#
# Missing data could arise as a result of changes in data collection methods, human error, bias, or simply the lack of reliable input. 

#############################################################

#++++++ How to detect missing values?

import pandas as pd

students = pd.read_excel("students.xlsx")

print(students.head())

# We can see the missing values by column using following code:
# True means that is the missing value

mask = students['State'].isnull()
print(mask)

# We can use this series as a mask to filter the students data frame
print(students[mask])

##################################################################################

# +++++++ +++ How to remove missing values?

print(students.dropna())

# Removing missing values in certain rows
students.dropna(subset=['State', 'Zip'], how='all')
print(students)

# Removing missing values in certain columns
students.dropna(axis = 1)
print(students)

# Removing certain clomuns missing certain numbers percentage
students.dropna(axis = 1, thresh=10)
print(students)

#################################################################
# How to resolve missing values

# we can replace in the missing column and rows manually
students = students.fillna({'Gender':'Female'})
print(students)

# replace missing values median or mean

students = students.fillna({'Age':students['Age'].median()})
print(students)

# Enter missing value manually

mask = (students['City'] == 'Granger') & (students['State'] == 'IN')

# we use row filteras .loc operator
print(students.loc[mask, :])

# enter a particluar cell
students.loc[mask, 'Zip'] = 46530
print(students.loc[mask, :])

# Lets update a clomn and row
mask = (students['City'] == 'Niles') & (students['State'] == 'MI')
students.loc[mask, 'Zip'] = 49120
print(students.loc[mask, :])

print(students)