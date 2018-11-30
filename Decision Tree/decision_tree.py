from functions import *
import pandas as pd
import random
import json
import copy


def stop_condition(data, columns, **kwargs):
    return len(set(data[kwargs['class_column']])) == 1 or len(columns) == 0


def probability(data, column, value):
    data[data[column] == value]

def calculate_ig(data, column, **kwargs):
    count = len(data)
    col_values = data[column].tolist()
    column_values = list(set(data[column].tolist()))
    children_properties = []
    for val in column_values:
        valued_data = data[data[column] == val]
        children_properties.append({
            'weight': len(valued_data)/count,
            'probability': [
                len(valued_data[valued_data[kwargs['class_column']] == 0])/len(valued_data),
                len(valued_data[valued_data[kwargs['class_column']] == 1])/len(valued_data),
            ]
        })
    
    return column ,information_gain([0.5, 0.5],children_properties)


def find_best_split(data, columns, **kwargs):
    best_option_name = ''
    best_option_ig = 0
    for col in columns:
        col_name, col_ig = calculate_ig(data, col, **kwargs)
        best_option_ig = best_option_ig if best_option_ig > col_ig else col_ig
        best_option_name = best_option_name if best_option_ig > col_ig else col_name
    return best_option_name


def tree_growth(data, columns, **kwargs):
    wow = {}
    if stop_condition(data, columns, **kwargs):
        return data[kwargs['class_column']].tolist()[0]
    ideal_col = find_best_split(data, columns, **kwargs)
    wow[ideal_col] = {}
    values = list(set(data[ideal_col].tolist()))
    tmp_columns = [col for col in columns]
    tmp_columns.remove(ideal_col)
    most_seen = 0
    wow[ideal_col]['values'] = {}
    for value in values:
        wow[ideal_col]['values'][value] = tree_growth(data[data[ideal_col] == value], tmp_columns, **kwargs)
        seen_count = data[ideal_col].tolist().count(value)
        if seen_count > most_seen:
            most_seen = seen_count
            wow[ideal_col]['default'] = value
    return wow

def make_decision_tree(data_name, class_column, pruning = True):
    df = pd.read_csv(data_name)
    columns = df.columns.tolist()
    columns.remove(class_column)
    tree = tree_growth(df,columns, class_column=class_column)
    print(json.dumps(tree))
    if pruning:
        data = pd.read_csv('noisy_valid.csv')
        error_counter = 0
        counter = 0
        
        pruned_tree = post_order_traverse(tree, data, main_data=df, class_column=class_column, main_tree=tree, route=[]))

        for element in data.iterrows():
            e = element[1].to_dict()
            if not test_item(t, e,  main_data=df, class_column=class_column, main_tree=pruned_tree, route=[]):
                error_counter += 1
            counter += 1
        print('error_counter', error_counter)
        print('counter', error_counter)

def test_item(tree, item, **kwargs):
    new_tree = tree.copy()
    while True:
        current_col = next(iter(new_tree.keys()))
        seen_value = item[current_col]
        new_level = next(iter(new_tree.values()))['values']
        if not(seen_value in new_level):
            seen_value = new_tree[current_col]['default']
        new_tree = new_level[seen_value]
        if type(new_tree) != dict:
            return new_tree == item[kwargs['class_column']]
        


def post_order_traverse(tmp_tree, data, **kwargs):

    if type(tmp_tree) != dict:
        return tmp_tree
    value = next(iter(tmp_tree.values()))
    key = next(iter(tmp_tree.keys()))
    tmp_node = {}
    route = kwargs['route']
    for item in value['values'].items():
        tmp_route = route.copy()
        tmp_route.append([key,item[0]])
        kwargs.update({'route':tmp_route})
        tmp_node[item[0]] = post_order_traverse(item[1], data, **kwargs)
    error_counter = 0
    counter = 0
    
    for element in data.iterrows():
        e = element[1].to_dict()
        if not test_item(kwargs['main_tree'], e, **kwargs):
            error_counter += 1
        counter += 1
        
    error_counter_sec = 0
    counter_sec = 0
    tmp_data = kwargs['main_data']
    for r in route:
        tmp_data = tmp_data[tmp_data[r[0]] == r[1]]
    default_class = most_common(tmp_data[kwargs['class_column']].tolist())
    new_tree = construct_new_tree(kwargs['main_tree'], route, default_class)
    for element in data.iterrows():
        e = element[1].to_dict()
        if not test_item(new_tree, e, **kwargs):
            error_counter_sec += 1
        counter_sec += 1
    print('error_counter',error_counter)
    print('error_counter_sec',error_counter_sec)
    if error_counter_sec < error_counter:
        return default_class
    return {key:{'default':value['default'] ,'values':tmp_node}}

def construct_new_tree(tree, routes, new_value, depth=0):
    if len(routes) == 0:
        if depth == 0:
            return tree
        return new_value
    val = next(iter(tree.keys()))
    tmp_tree = {val:{'default': tree[val]['default'], 'values':{}}}
    for node in tree[val]['values'].items():
        if len(routes) > 0 and val == routes[0][0] and node[0] == routes[0][1]:
            routes.remove(routes[0])
            tmp_tree[val]['values'][node[0]] = construct_new_tree(node[1], routes, new_value, depth=1)
        else:
            tmp_tree[val]['values'][node[0]] = tree[val]['values'][node[0]]
    return tmp_tree

r = {
    't':{
        'r':'1',
        'b':'2'
    },
    'y': '3'
}

make_decision_tree('noisy_train.csv', 'poisonous')