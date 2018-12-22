from itertools import combinations

SUPPORT_THRESHOLD = 2

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

def combination(arr_list, common_number):
    iter_arr = [i for i in range(len(arr_list))]
    result = []
    for el in combinations(iter_arr, 2):
        item = list(set(arr_list[el[0]]+ arr_list[el[1]]))
        item.sort()
        if len(common_elements(arr_list[el[0]],arr_list[el[1]])) >= common_number and item not in result:
            result.append(item)
    return result

def get_items(data_set):
    items = []
    for obj in data_set:
        for el in obj:
            if [el] not in items:
                items.append([el])
    return items


def count_repeat(data_set, target):
    counter = 0
    for obj in data_set:
        if set(target) <= set(obj):
            counter += 1
    return counter

def apriori(data_set):
    k = 1
    L = get_items(data_set)
    # L = [ [i[1]] for i in data_set]
    while len(L) != 0:
        k += 1
        L = combination(L, k-2)
        tmp_l = []
        for comb in L:
            count = count_repeat(data_set, comb)
            if count >= SUPPORT_THRESHOLD:
                tmp_l.append(comb)
        L = tmp_l
        

apriori([
    [1,2,5],
    [2,4],
    [2,3],
    [1,2,4],
    [1,3],
    [2,3],
    [1,3],
    [1,2,3,5],
    [1,2,3]
])
