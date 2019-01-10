import numpy as np

def soft_max(arr):
    f = np.array(arr)
    f -= np.max(f)
    p = np.exp(f) / np.sum(np.exp(f))
    return p