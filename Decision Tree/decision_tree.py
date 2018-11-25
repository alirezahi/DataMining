from functions import *
import pandas as pd
import json


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
    for value in values:
        wow[ideal_col][value] = tree_growth(data[data[ideal_col] == value], tmp_columns, **kwargs)
    return wow

def make_decision_tree(data_name, class_column):
    df = pd.read_csv(data_name)
    columns = df.columns.tolist()
    columns.remove(class_column)
    tree = tree_growth(df,columns, class_column=class_column)
    print(json.dumps(tree))

make_decision_tree('baseball.csv', 'Play ball?')