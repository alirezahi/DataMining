from itertools import combinations

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


# t = combination([[2, 3], [2, 4], [3, 4]])

def apriori(data_set):
    k = 1
    L = data_set
    # L = [ [i[1]] for i in data_set]
    while len(L) != 0:
        k += 1
        print(L)
        L = combination(L, k-2)

apriori([[3],[5],[9],[11]])