import math
import operator
import itertools

def entropy(probability_list):
    sum_result = 0
    for probability_item in probability_list:
        if probability_item == 0:
            sum_result += 0
        else:
            sum_result += (-1)*probability_item*math.log2(probability_item)
    return sum_result


def information_gain(parent_probability, children_properties):
    children_weighted_entopry = 0
    for child in children_properties:
        children_weighted_entopry += child['weight']*entropy(child['probability'])
    return entropy(parent_probability) - children_weighted_entopry


def most_common(L):
    # get an iterable of (item, iterable) pairs
    SL = sorted((x, i) for i, x in enumerate(L))
    # print 'SL:', SL
    groups = itertools.groupby(SL, key=operator.itemgetter(0))
    # auxiliary function to get "quality" for an item
    def _auxfun(g):
            item, iterable = g
            count = 0
            min_index = len(L)
            for _, where in iterable:
                    count += 1
                    min_index = min(min_index, where)
            # print 'item %r, count %r, minind %r' % (item, count, min_index)
            return count, -min_index
    # pick the highest-count/earliest item
    return max(groups, key=_auxfun)[0]