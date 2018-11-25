import math

def entropy(probability_list):
    sum_result = 0
    for probability_item in probability_list:
        sum_result += (-1)*probability_item*math.log2(probability_item)
    return sum_result


def information_gain(parent_probability, children_properties):
    children_weighted_entopry = 0
    for child in children_properties:
        children_weighted_entopry += child['weight']*entropy(child['probability'])
    return entropy(parent_probability) - children_weighted_entopry