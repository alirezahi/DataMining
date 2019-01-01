
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


plt.figure()
plt.scatter(features.iloc[:,0],features.iloc[:,1], c=labels)
plt.show()

r = np.arctan(np.divide(features.iloc[:,1],features.iloc[:,0]))
teta = np.sqrt(np.power(features.iloc[:,0],2)+np.power(features.iloc[:,1],2))

plt.scatter(r,teta, c=labels)

plt.show()
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.4)

x_test, x_validation, y_test, y_validation = train_test_split(x_test, y_test, test_size=0.5)


C_candidates = [0.001,0.01, 0.1, 1, 10, 100]
C_accuracy = []

# for candidate in C_candidates:
classifier = SVC(C=C_candidates[0], kernel='linear')
classifier = classifier.fit(x_train, y_train)
    # predict_validation = classifier.predict(x_validation)
    # C_accuracy.append(accuracy_score(y_validation, predict_validation))

print(C_accuracy)

# get the separating hyperplane
w = classifier.coef_[0]
print(w)
a = -w[0] / w[1]
xx = np.linspace(-5, 5)
yy = a * xx - (classifier.intercept_[0]) / w[1]

plt.plot(xx, yy, 'k-')
plt.show()