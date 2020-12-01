import numpy as np
import pandas as pd
import plotly as pl
import plotly.offline as po
import cufflinks as cf

po.init_notebook_mode(connected=True)
cf.go_offline()

def createdata(data):
    if(data == 1):
        x = np.random.rand(100,5)
        df1 = pd.DataFrame(x,columns=['A','B','C','D','E'])
    elif(data == 2):
        file = input('Enter the file name')
        x = pd.read_csv(file)
        df1 = pd.DataFrame(x)
    else:
        print('DataFrame creation failed please enter in between 1 to 3 and try again')
    return df1

def main(cat):
    if cat == 1:
        print('Select The type of plot you need to plot by writing 1 to 6')
        print('1.line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')
        print('6.surface plot')
        plot = int(input())
        output = plotter(plot)
    elif(cat == 2):
        print('Select the type of plot you need to plot by writing 1 to 7')
        print('1.Line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')
        print('6.Surface plot')
        print('7.Bubble plot')
        plot = int(input())
        output = plotter2(plot)
    else:
        print('Please enter 1 or 2 and try again')

def plotter(plot):
    if(plot == 1):
        finalplot = df1.iplot(kind='scatter')
    elif(plot == 2):
        finalplot = df1.iplot(kind='scatter',mode='markers' ,symbol='x',colorscale='paired')
    elif(plot == 3):
        finalplot = df1.iplot(kind='bar')
    elif(plot == 4):
        finalplot = df1.iplot(kind='hist')
    elif(plot == 5):
        finalplot = df1.iplot(kind='box')
    elif(plot == 6):
        finalplot = df1.iplot(kind='surface')
    else:
        finalplot = print('Select only between 1 to 7')
    return finalplot

def plotter2(plot):
    col = input('Enter the number of columns you want to plot by selecting only 1 , 2 or 3')
    col = int(col)
    if(col==1):
        colm = input('Enter the column you want to plot by selecting any column from dataframe head')
        if(plot==1):
            finalplot = df1[colm].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[colm].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[colm].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[colm].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[colm].iplot(kind='box')
        elif(plot==6 or plot==7):
            finalplot = print('surface plot require more than one column arguments')
        else:
            finalplot = print('Select only between 1 to 6')
    elif(col==2):
        print('Enter the columns you want to plot by selecting from dataframe head')
        x = input('First column').upper()
        y = input('Second column').upper()
        if(plot==1):
            finalplot = df1[[x,y]].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[[x,y]].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[[x,y]].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[[x,y]].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[[x,y]].iplot(kind='box')
        elif(plot==6):
            finalplot = df1[[x,y]].iplot(kind='surface')

            finalplot = print('Select only between 1 to 6')
    elif(col==3):
        print('Enter the columns you want to plot')
        x=input('First column').upper()
        y=input('Second column').upper()
        z=input('Third column').upper()
        if(plot==1):
            finalplot = df1[[x,y,z]].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[[x,y,z]].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[[x,y,z]].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[[x,y,z]].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[[x,y,z]].iplot(kind='box')
        elif(plot==6):
            finalplot = df1[[x,y,z]].iplot(kind='surface')

        else:
            finalplot = print('Select only between 1 to 6')
    else:
        finalplot = print('Please enter only 1 , 2 or 3')
    return finalplot

print('select the type of data you need to plot(By writing 1, 2).')
print('1.Randam data with 100 rows and 5 columns.')
print('2.Upload csv/json/text file.')
data=int(input())
df1=createdata(data)
print('Your DataFrame head is given below check the columns to plot using cufflinks')
df1.head()
print('What kind of plot you need, The complet data plot or columns plot')
cat=input('Press 1 for plotting all columns or Press 2 for specifying columns to plot')
cat=int(cat)
main(cat)
