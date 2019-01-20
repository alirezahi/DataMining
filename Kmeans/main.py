
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow.contrib.factorization import KMeans
import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

#import mnist data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
data = mnist.train.images

# number of steps to run
steps_n = 100
# number of clusters
k = 30
# 10 digits
classes_n = 10
# convert images of 28*28 to 784 feature
features_n = 784


X = tf.placeholder(tf.float32, shape=[None, features_n])
Y = tf.placeholder(tf.float32, shape=[None, classes_n])

kmeans = KMeans(inputs=X, num_clusters=k, distance_metric='cosine',
                use_mini_batch=True)

training_graph = kmeans.training_graph()

if len(training_graph) > 6:
    (all_scores, cluster_idx, scores, cluster_centers_initialized,
     cluster_centers_var, init_op, train_op) = training_graph
else:
    (all_scores, cluster_idx, scores, cluster_centers_initialized,
     init_op, train_op) = training_graph

cluster_idx = cluster_idx[0]
dist_avg = tf.reduce_mean(scores)

initial_value = tf.global_variables_initializer()

sess = tf.Session()

sess.run(initial_value, feed_dict={X: data})
sess.run(init_op, feed_dict={X: data})

for i in range(1, steps_n + 1):
    _, d, idx = sess.run([train_op, dist_avg, cluster_idx],
                         feed_dict={X: data})

numbers = np.zeros(shape=(k, classes_n))
for i in range(len(idx)):
    numbers[idx[i]] += mnist.train.labels[i]

l_map = [np.argmax(c) for c in numbers]
l_map = tf.convert_to_tensor(l_map)

c_l = tf.nn.embedding_lookup(l_map, cluster_idx)
correct_prediction = tf.equal(c_l, tf.cast(tf.argmax(Y, 1), tf.int32))
accuracy_op = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

test_x, test_y = mnist.test.images, mnist.test.labels
print("Accuracy: ", sess.run(accuracy_op, feed_dict={X: test_x, Y: test_y}))