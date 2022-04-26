import pandas as pd
import plotly.express as px
import numpy as np
import csv

def plotGraph():
    with open("Student Marks vs Days Present.csv") as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x = 'Marks In Percentage',y = 'Days Present')
        fig.show()

def getData():
    MarksPercentage = []
    DaysPresent = []
    with open("Student Marks vs Days Present.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            MarksPercentage.append(float(row["Roll No"]))
            DaysPresent.append(float(row["Marks In Percentage"]))
    return{"x": MarksPercentage,"y": DaysPresent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage vs Days present :-  \n--->",correlation[0,1])

datasource = getData()
findCorrelation(datasource)
plotGraph()