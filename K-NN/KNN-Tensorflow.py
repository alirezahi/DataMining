import tensorflow as tf
from tensorflow import keras
import numpy as np
# import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(trImages, trLabels), (tImages, tLabels) = fashion_mnist.load_data()

paramk = 11

x = tf.placeholder(trImages.dtype, shape=trImages.shape) 
y = tf.placeholder(tImages.dtype, shape=tImages.shape[1:])

xThresholded = tf.clip_by_value(tf.cast(x, tf.int32), 0, 1) 
yThresholded = tf.clip_by_value(tf.cast(y, tf.int32), 0, 1) 
computeL0Dist = tf.count_nonzero(xThresholded - yThresholded, axis=[1,2]) 
findKClosestTrImages = tf.contrib.framework.argsort(computeL0Dist, direction='ASCENDING') 
findLabelsKClosestTrImages = tf.gather(trLabels, findKClosestTrImages[0:paramk]) 
findULabels, findIdex, findCounts = tf.unique_with_counts(findLabelsKClosestTrImages) 
findPredictedLabel = tf.gather(findULabels, tf.argmax(findCounts)) 

numErrs = 0
numTestImages = np.shape(tLabels)[0]
numTrainImages = np.shape(trLabels)[0] 

with tf.Session() as sess:
  for iTeI in range(0,numTestImages): # iterate each image in test set
    predictedLabel = sess.run([findPredictedLabel], feed_dict={x:trImages, y:tImages[iTeI]})   

    if predictedLabel == tLabels[iTeI]:
      numErrs += 1
      print(numErrs,"/",iTeI)
      print("\t\t", predictedLabel[0], "\t\t\t\t", tLabels[iTeI])

print("# Classification Errors= ", numErrs, "% accuracy= ", 100.*(numTestImages-numErrs)/numTestImages)
      