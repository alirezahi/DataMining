def euclidean_distance(x1, x2):
    return sum([(x1[i] - x2[i])**2 for i in range(len(x1))])**(1/2)


def normalize(value, min_value, max_value):
    return (value - min_value)/(max_value - min_value)