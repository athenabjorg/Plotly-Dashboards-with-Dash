####################################
### Pandas Crash Course ###########
##################################
# We'll use pandas more than numpy in the Course
# so let's quickly go over a few main ideas with pandas!

import pandas as pd
import numpy as np


# Reading in CSV files. Use the read_csv command.
# More options: https://pandas.pydata.org/pandas-docs/stable/io.html
df = pd.read_csv('salaries.csv')

print(df)
#      Name  Salary  Age
# 0    John   50000   34
# 1   Sally  120000   45
# 2  Alyssa   80000   27


# You can select columns with a bracket call:
print(df['Name'])
# 0      John
# 1     Sally
# 2    Alyssa
# Name: Name, dtype: object

print(df['Salary'])
# 0     50000
# 1    120000
# 2     80000
# Name: Salary, dtype: int64


# Select multiple columns with a list of column names.
# Since you are passing in a list, you see two sets of []
print(df[['Name','Salary']])
#      Name  Salary
# 0    John   50000
# 1   Sally  120000
# 2  Alyssa   80000


# Similar to NumPy, you can create calls of min(), max(), mean(), etc...
# on a pandas dataframe.

print(df['Age'].mean())
# 35.333333333333336


# Just like Numpy, we can use conditional filtering to select rows that meet
# certain critera. Like choosing rows where the Age value is greater than 30

ser_of_bool = df['Age'] > 30
print(ser_of_bool)
# 0     True
# 1     True
# 2    False
# Name: Age, dtype: bool

# Use this filter of booleans to then select the rows

age_filter = df['Age'] > 30

# Pass it to the dataframe
print(df[age_filter])
#     Name  Salary  Age
# 0   John   50000   34
# 1  Sally  120000   45

# More commonly done all in one step:
df[df['Age'] > 30]


# There are lots of other commands you can do with pandas!
# But for now, we'll just talk about a few more, and then introduce the rest
# as we continue through the course :)

df['Age'].unique() # list of unique values for Age
df['Age'].nunique() # number of unqiue values
df.info() # General info about your dataframe
df.describe() # Statistics about your dataframe
df.columns # Grab a list of all columns
df.index # Create an index list
# You can convert a numpy matrix to a dataframe with:
mat = np.arange(0,10).reshape(5,2)
np_df = pd.DataFrame(data=mat, columns=['A','B'], index=['a','b','c','d','e'])
print(np_df)
#    A  B
# a  0  1
# b  2  3
# c  4  5
# d  6  7
# e  8  9
