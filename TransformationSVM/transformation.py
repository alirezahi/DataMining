
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


data = pd.read_csv('svmdata2.csv')
labels = data.iloc[:,2]
features = data.iloc[:,0:2]


r = np.arctan(np.divide(features.iloc[:,1],features.iloc[:,0]))
teta = np.sqrt(np.power(features.iloc[:,0],2)+np.power(features.iloc[:,1],2))

plt.scatter(r,teta, c=labels)

plt.show()