print(__doc__)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split


data = pd.read_csv('svmdata.csv')
labels = data.iloc[:,2]
features = data.iloc[:,0:2]

plt.figure()
plt.scatter(features.iloc[:,0],features.iloc[:,1], c=labels)

plt.show()

x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.4)

x_test, x_validation, y_test, y_validation = train_test_split(x_test, y_test, test_size=0.5)



