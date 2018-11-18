def euclidean_distance(x1, x2):
    return sum([(x1[i] - x2[i])**2 for i in range(len(x1))])**(1/2)


print(euclidean_distance([1,2,3],[2,3,4]))