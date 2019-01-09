from itertools import combinations

SUPPORT_THRESHOLD = 4

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

def replace_n(string):
    string = string.replace('\r','')
    string = string.replace('\n','')
    string = string.replace('\r\n','')
    return string

def subs(l):
    if l == []:
        return [[]]
    x = subs(l[1:])
    return x + [[l[0]] + y for y in x]

def subs_non_zero(l):
    res = []
    for r in filter(lambda x: x != [] and x != l, subs(l)):
        res.append(r)
    return res

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
    NEW_L = L.copy()
    L = []
    for comb in NEW_L:
        count = count_repeat(data_set, comb)
        if count >= SUPPORT_THRESHOLD:
            L.append(comb)
    print(L)
    result = None
    while len(L) != 0:
        k += 1
        new_list = combination(L, k-2)
        tmp_l = []
        for comb in new_list:
            count = count_repeat(data_set, comb)
            if count >= SUPPORT_THRESHOLD:
                tmp_l.append(comb)
        print('', tmp_l)
        if len(tmp_l) == 0:
            result = L.copy()
        L = tmp_l
    return result

input_data = []
with open('chess.dat') as f:
    input_data = [[el for el in replace_n(line).split(' ')] for line in f]

r = apriori(input_data)
r = r[0]
r = ['B','E']
# print(r)
# print(subs_non_zero(r))
r_rept = count_repeat(input_data, r)
# for comb in subs_non_zero(r):
    # complementary_comb = list(set(r)-set(comb))
comb = ['B']
c1 = count_repeat(input_data, comb)
    # c1 = count_repeat(input_data, ['B'])
print(comb, ' => ', list(set(r)-set(comb)))
print(r_rept/c1)
# print('we')
