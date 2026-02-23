import numpy as np

def gen(n, p, threshold):
    data_list = []

    arr0 = np.random.uniform(-threshold, threshold, p)
    arr0.sort()
    data_list.append(arr0)

    arr1 = np.random.uniform(-threshold, threshold, p)
    arr1 = np.sort(arr1)[::-1]
    data_list.append(arr1)

    for _ in range(3):
        arr = np.random.uniform(-threshold, threshold, p)
        data_list.append(arr)

    for _ in range(5):
        arr = np.random.randint(-int(threshold), int(threshold), p)
        data_list.append(arr)
        
    return data_list
    
    