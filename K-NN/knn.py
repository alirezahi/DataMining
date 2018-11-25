import csv
import random
import operator
import itertools

def euclidean_distance(x1, x2,**kwargs):
    return sum([sub_value(x1[i+1], x2[i+1], **kwargs, counter=i)**2 for i in range(len(x1)-1)])**(1/2)


def sub_value(v1, v2, **kwargs):
    if str(v1).isdigit() and str(v2).isdigit():
        if 'min_max' in kwargs:
            return normalize(v1, kwargs['min_max'][kwargs['counter']]['min'], kwargs['min_max'][kwargs['counter']]['max']) - normalize(v2, kwargs['min_max'][kwargs['counter']]['min'], kwargs['min_max'][kwargs['counter']]['max'])
        return v1-v2
    return int(v1 is not v2)


def normalize(value, min_value, max_value):
    return (float(value) - float(min_value))/(float(max_value) - float(min_value))


def min_val(arr):
    if str(arr).isdigit():
        return min(arr)

def max_val(arr):
    if str(arr).isdigit():
        return max(arr)

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

def best_neighbours(items, k):
    items.sort(key=lambda x: x[1])
    res = [i[0][0] for i in items][:k]
    return most_common(res)


def knn(csv_file_name, k=1):
    if k < 1:
        print(':: INVALID VARIABLE K ::')
        return
    content_col = [[] for r in range(20)]
    content_row = []
    element_nums = 0
    with open(csv_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        ok = False
        for row in csv_reader:
            if not ok:
                ok = True
                continue
            content_row.append(row)
            element_nums += 1
            for r in range(len(row)):
                content_col[r].append(row[r])
    min_max_arr = []
    for element in content_col:
        if element:
            min_max_arr.append({'min': min(element), 'max': max(element)})

    data_length = len(content_row)
    train_length = int(data_length*4/5)
    test_length = data_length - train_length

    test_nums = [i for i in random.sample(range(data_length),test_length)]

    train_row = []
    test_row = []

    for index, item in enumerate(content_row):
        if index in test_nums:
            test_row.append(item)
        else:
            train_row.append(item)

    error_rate = 0
    for test_item in test_row: 
        euc_list = [[train_row[i],euclidean_distance(test_item,train_row[i],min_max=min_max_arr)] for i in range(len(train_row))]
        result = best_neighbours(euc_list,30)
        # print(test_item," => ", "WIN" if result == "1" else "Lose")
        # if(str(test_item[0]) != str(result)):
        #         print(result,test_item)
        error_rate += int(str(test_item[0]) != str(result))

    print(error_rate)
knn('US Presidential Data.csv')

# print(euclidean_distance([1,2,3],[2,3,4],min_max=[]))