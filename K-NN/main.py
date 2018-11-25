import csv
from knn import *
content_col = [[] for r in range(20)]
content_row = []
element_nums = 0
with open('US Presidential Data.csv') as csv_file:
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

euc_list = [euclidean_distance(content_row[4],content_row[i+5],min_max=min_max_arr) for i in range(element_nums-5)]
target = min(euc_list)
print(euc_list.index(target))