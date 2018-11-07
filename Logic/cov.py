from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
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


a = np.array(x[i])
cov = np.cov(x[0],x[1])
print("cov ==> \n" + str(cov)+"\n\n")
