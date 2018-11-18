def euclidean_distance(x1, x2,**kwargs):
    return sum([sub_value(x1[i], x2[i], **kwargs, counter=i)**2 for i in range(len(x1))])**(1/2)


def sub_value(v1, v2, **kwargs):
    if str(v1).isdigit() and str(v2).isdigit():
        if 'min_max' in kwargs:
            return normalize(v1, kwargs['min_max'][kwargs['counter']]['min'], kwargs['min_max'][kwargs['counter']]['max']) - normalize(v2, kwargs['min_max'][kwargs['counter']]['min'], kwargs['min_max'][kwargs['counter']]['max'])
        return v1-v2
    return int(v1 is v2)


def normalize(value, min_value, max_value):
    return (value - min_value)/(max_value - min_value)

print(euclidean_distance([1,2,3],[2,3,4],min_max=[{'min':1, 'max':2},{'min':2, 'max':3},{'min':3, 'max':4}]))