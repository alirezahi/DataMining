# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
import numpy as np
import csv


x = [
    [],
    [],
    [],
    [],
]

r = []
with open('iris.data','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if len(row):
            for i in range(4):
                x[i].append(float(row[i]))
            if(row[-1] == 'Iris-setosa'):
                x[i].append(1)
            if(row[-1] == 'Iris-versicolor'):
                x[i].append(2)
            if(row[-1] == 'Iris-virginica'):
                x[i].append(3)
            # Iris-virginica
            # Iris-versicolor


a = np.array(x[i])
corr = np.corrcoef(x[0],x[1])
print("corr 0,1 ==> " + str(corr))
corr = np.corrcoef(x[0],x[2])
print("corr 0,2 ==> " + str(corr))
corr = np.corrcoef(x[0],x[3])
print("corr 0,3 ==> " + str(corr))
corr = np.corrcoef(x[1],x[2])
print("corr 1,2 ==> " + str(corr))
corr = np.corrcoef(x[1],x[3])
print("corr 1,3 ==> " + str(corr))
corr = np.corrcoef(x[2],x[3])
print("corr 2,3 ==> " + str(corr))