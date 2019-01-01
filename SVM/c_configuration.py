
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

plt.figure()

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
min_c = max(C_accuracy)
print("Max of C rate => ", min_c)