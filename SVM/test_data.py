import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


data = pd.read_csv('svmdata.csv')
labels = data.iloc[:,2]
features = data.iloc[:,0:2]




x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.4)

x_test, x_validation, y_test, y_validation = train_test_split(x_test, y_test, test_size=0.5)


C_candidates = [0.0001,0.001,0.01, 0.1, 1, 10, 100, 1000]
C_accuracy = []
C_svm = []

for candidate in C_candidates:
    classifier = SVC(C=C_candidates[0], kernel='linear')
    classifier = classifier.fit(x_train, y_train)
    predict_validation = classifier.predict(x_validation)
    C_accuracy.append(accuracy_score(y_validation, predict_validation))
    C_svm.append(classifier)

print("C accurace rate: ", C_accuracy)
min_c = min(C_accuracy)
print("Min of C => ", min_c)
c_min_id = C_accuracy.index(min_c)

# get the separating hyperplane
w = C_svm[c_min_id].coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-5, 5)
yy = a * xx - (C_svm[c_min_id].intercept_[0]) / w[1]

predict_validation = classifier.predict(x_test)
test_accuracy = accuracy_score(y_test, predict_validation)
print('test accuracy => ', test_accuracy)

plt.scatter(x_test.iloc[:,0],x_test.iloc[:,1], c=y_test)
plt.plot(xx, yy, 'k-')
plt.show()