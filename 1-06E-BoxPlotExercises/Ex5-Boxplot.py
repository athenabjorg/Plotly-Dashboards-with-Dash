#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# create a DataFrame from the .csv file:
df = pd.read_csv('data/abalone.csv')

# take two random samples of different sizes:
sample1 = np.random.choice(df['rings'], 10, replace=False)
sample2 = np.random.choice(df['rings'], 10, replace=False)

# create a data variable with two Box plots:
data = [go.Box(y=sample1, name='Sample 1'),
        go.Box(y=sample2, name='Sample 2')]

# add a layout
layout = go.Layout(title='Rings samples')

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='results/1-06_boxplot.html')
