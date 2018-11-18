from numpy import *
import numpy as np
import random

# y = mx + b
# m is slope, b is y-intercept
def compute_error_for_line_given_points(b, m, c, points):
    totalError = 0
    for i in range(0, len(points['x1'])):
        x1 = points['x1'][i]
        x2 = points['x2'][i]
        y = points['y'][i]
        totalError += (y - (m * x1 + c * x2 + b)) ** 2
    return totalError / float(len(points['x1']))

def step_gradient(b_current, m_current, c_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    c_gradient = 0
    N = float(len(points['x1']))
    r = random.randint(0, N-1)
    x1 = points['x1'][r]
    x2 = points['x2'][r]
    y = points['y'][r]
    b_gradient += -(2/N) * (y - ((m_current * x1) + (c_current * x2) + b_current))
    m_gradient += -(2/N) * x1 * (y - ((m_current * x1) + (c_current * x2) + b_current))
    c_gradient += -(2/N) * x2 * (y - ((m_current * x1) + (c_current * x2) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_c = c_current - (learningRate * c_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m, new_c]

def stochastic_gradient_descent_runner(points, starting_b, starting_m, starting_c, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    c = starting_c
    for i in range(num_iterations):
        print(i)
        b, m, c = step_gradient(b, m, c, points, learning_rate)
    return [b, m, c]

def run():
    points = np.load("data.npz")
    learning_rate = 0.0001
    initial_b = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess
    initial_c = 0 # initial slope guess
    num_iterations = 200000
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, initial_c, compute_error_for_line_given_points(initial_b, initial_m, initial_c,points)))
    print("Running...")
    [b, m, c] = stochastic_gradient_descent_runner(points, initial_b, initial_m, initial_c, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, m = {2}, c = {3} error = {4}".format(num_iterations, b, m, c, compute_error_for_line_given_points(b, m, c, points)))

if __name__ == '__main__':
    run()