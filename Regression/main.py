import numpy as np

a = np.load('data.npz')
for i in range(10):
    print(a['y'][i],end=',')
    print(a['x1'][i])
    print(a['x2'][i])
print(len(a['x1_test']))
print(len(a['x1']))
print(len(a['x2']))
print(len(a['x1_test']))