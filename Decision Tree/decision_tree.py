from functions import *
import pandas as pd




def make_decision_tree(data_name):
    df = pd.read_csv('noisy_train.csv')
    columns = df.columns.tolist()
    tree_growth(data,columns)


def stop_condition(data, columns):
    return False


def find_best_split(data, columns):
    return ''


def tree_growth(data, columns):
    if stop_condition(data,columns):
        return
    find_best_column(data)
    return