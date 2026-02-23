import numpy as np

def gen(n, p, threshold):
    data_list = []
    limit = int(threshold)

    data_list.append(np.sort(np.random.uniform(-threshold, threshold, p)))
    data_list.append(np.sort(np.random.uniform(-threshold, threshold, p))[::-1])

    for _ in range(3):
        data_list.append(np.random.uniform(-threshold, threshold, p))

    for _ in range(5):
        data_list.append(np.random.randint(-limit, limit, p))

    return data_list