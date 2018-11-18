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


for i in range(4):
    a = np.array(x[i])
    mean = np.mean(a)
    print("propert " +str(i) + " mean ==> " + str(mean))
