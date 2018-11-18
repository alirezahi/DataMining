def euclidean_distance(x1, x2):
    return sum([sub_value(x1[i], x2[i])**2 for i in range(len(x1))])**(1/2)


def sub_value(v1, v2):
    if v1.isdigit() and v2.isdigit():
        return v1-v2
    return int(v1 is v2)


def normalize(value, min_value, max_value):
    return (value - min_value)/(max_value - min_value)