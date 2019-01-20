import pandas as pd
import numpy as np
import random
import pprint
import math

learning_rate = 0.5

layers_detail = [
    {
        'activation_function': 'tanh',
        'neurons_number': 8,
        'previous_number': 14,
    },
    {
        'activation_function': 'tanh',
        'neurons_number': 5,
        'previous_number': 9,
    },
    {
        'activation_function': 'soft_max',
        'neurons_number': 3,
        'previous_number': 6,
    },
]

    
def soft_max(arr):
    f = np.array(arr)
    f -= np.max(f)
    p = np.exp(f) / np.sum(np.exp(f))
    return p

def activation_function(weights, level, **kwargs):
    if layers_detail[level]['activation_function'] == 'tanh':
        return [ np.tanh(w) for w in weights]
    elif layers_detail[level]['activation_function'] == 'soft_max':
        return soft_max(weights)
    

def get_error_rate(error_type, inner_neurons, **kwargs):
    error_rates = []
    if error_type == 'output':
        for index in range(len(inner_neurons)):
            error_rates.append(kwargs['target'][index]-inner_neurons[index])
        return error_rates
    if error_type == 'hidden_layer':
        for index in range(len(inner_neurons)):
            error_rates.append(
                (1-inner_neurons[index]**2)*sum([kwargs['weights'][t_node_index][index] * kwargs['delta'][t_node_index] for t_node_index in range(len(kwargs['weights']))])
            )
        return error_rates

def change_weight(w,neuron,delta):
    result_weight = []
    for index in range(len(w)):
        tmp_weight = []
        for s_index in range(len(w[0])):
            tmp_weight.append(
                w[index][s_index]-learning_rate*delta[index]*neuron[s_index]
            ) 
        result_weight.append(tmp_weight)
    return result_weight


def calculate_weight(x,w,iterate,level):
    weight = 0 
    for i in range(len(w[level][0])):
        weight += x[i] * w[level][iterate][i]
    return weight

w = [
    np.random.normal(0,0.1,size=[layer['neurons_number'],layer['previous_number']]) for layer in layers_detail
]

neurons = [
    [ 0 for i in range(layer['neurons_number'])] for layer in layers_detail
]

data_list = pd.read_csv('Drinks.csv')
data_list = data_list.sample(frac=1)

epoch = 50

for epoch_iterator in range(epoch):
    for data_index in range(len(data_list)):
        # feed-forward nn
        neurons = [
            [ 0 for i in range(layer['neurons_number'])] for layer in layers_detail
        ]
        d = data_list.iloc[data_index].tolist()
        x = [1]+d[:-3]

        delta = []


        for i in range(8):
            neurons[0][i] = calculate_weight(x,w,i,0)


        neurons[0] = activation_function(neurons[0],0)

        neurons[0] = [1] + neurons[0]

        for i in range(5):
            neurons[1][i] = calculate_weight([1]+neurons[0],w,i,1)


        neurons[1] = activation_function(neurons[1],1)

        neurons[1] = [1] + neurons[1]

        for i in range(3):
            neurons[2][i] = calculate_weight([1]+neurons[1],w,i,2)
        neurons[2] = activation_function(neurons[2],2)

        # backpropagation nn
        new_delta = get_error_rate(error_type='output',inner_neurons=neurons[2],target=d[-3:])
        w[-1] = change_weight(w[-1],neurons[1],new_delta)
        new_delta = get_error_rate(error_type='hidden_layer',inner_neurons=neurons[1],delta=new_delta, weights=w[-1])
        w[-2] = change_weight(w[-2],neurons[0],new_delta)
        new_delta = get_error_rate(error_type='hidden_layer',inner_neurons=neurons[0],delta=new_delta, weights=w[-2])
        w[-3] = change_weight(w[-3],x,new_delta)

# testing test point

true_count = 0
list_count = 0
for i in range(len(data_list)):
    neurons = [
        [ 0 for i in range(layer['neurons_number'])] for layer in layers_detail
    ]
    d = data_list.iloc[i].tolist()
    x = [1]+d[:-3]

    delta = []


    for i in range(8):
        neurons[0][i] = calculate_weight(x,w,i,0)


    neurons[0] = activation_function(neurons[0],0)

    neurons[0] = [1] + neurons[0]

    for i in range(5):
        neurons[1][i] = calculate_weight([1]+neurons[0],w,i,1)


    neurons[1] = activation_function(neurons[1],1)

    neurons[1] = [1] + neurons[1]

    for i in range(3):
        neurons[2][i] = calculate_weight([1]+neurons[1],w,i,2)
    neurons[2] = activation_function(neurons[2],2)
    if list(neurons[-1]).index(1) == d.index(1)-13:
        true_count += 1
    list_count += 1

print('ACCURACY:', true_count/list_count)
