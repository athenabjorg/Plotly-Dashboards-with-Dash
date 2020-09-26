#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('data/iris.csv')

# Define the traces
flowers = pd.unique(df['class'])

# Define a data variable
data = [df[df['class']==flower]['petal_length'] for flower in flowers]

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(data, flowers, bin_size=0.2)
pyo.plot(fig, filename='results/1-08_distplot.html')
