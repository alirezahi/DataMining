import tensorflow as tf
from tensorflow import keras
import pandas as pd

import numpy as np

print(tf.__version__)


data=pd.read_csv('Drinks.csv')
train_features = []
train_labels = []
for index, row in data.iterrows():
    train_features.append(row[:-3].tolist())
    classes = row[-3:].tolist()
    train_labels.append(classes.index(1))

train_features = np.asarray(train_features)
train_labels = np.asarray(train_labels)

class_names = ['Class 1', 'Class 2', 'Class 3']


print(train_features)

model = keras.Sequential([
    keras.layers.Dense(8, activation=tf.nn.tanh),
    keras.layers.Dense(5, activation=tf.nn.tanh),
    keras.layers.Dense(3, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_features, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(train_features, train_labels)

print('Test accuracy:', test_acc)

predictions = model.predict(train_features)