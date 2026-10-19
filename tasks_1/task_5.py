import math
def find_anomalies(data, k):
    n = len(data)
    if n == 0:
        return []
    total = 0
    for x in data:
        total += x
    mean = total / n
    sum_sq = 0
    for x in data:
        diff = x - mean
        sum_sq += diff * diff
    std = math.sqrt(sum_sq / n)
    if std == 0:
        return []
    anomalies = []
    for x in data:
        if abs(x - mean) > k * std:
            anomalies.append(x)
    return anomalies

data = [10, 12, 11, 13, 12, 11, 100, 12, 13, 11]
print("Аномалии при k=2:", find_anomalies(data, 2))
print("Аномалии при k=1:", find_anomalies(data, 1))

import numpy as np
def find_anomalies_numpy(data, k):
    arr = np.array(data)
    if arr.size == 0:
        return []
    mean = arr.mean()
    std = arr.std()
    if std == 0:
        return []

    mask = np.abs(arr - mean) > k * std
    return arr[mask].tolist()

data = [10, 12, 11, 13, 12, 11, 100, 12, 13, 11]
print("Аномалии numpy:", find_anomalies_numpy(data, 2))