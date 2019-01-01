print(__doc__)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm, datasets


data = pd.read_csv('svmdata.csv')
labels = data.iloc[:,2]
features = data.iloc[:,0:2]

plt.figure()
plt.scatter(features.iloc[:,0],features.iloc[:,1], c=labels)

plt.show()

