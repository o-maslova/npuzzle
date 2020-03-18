import sys
from math import sqrt

# arr = [[0, 5, 7], [3, 2, 4], [1, 8, 6]]
def sum_of_abs(arr, final_state):
    arr_len = int(sqrt(len(arr)))
    arr_weight = 0

    for i in range(arr_len):
        for j in range(arr_len):
            if arr[i * arr_len + j] == 0:
                continue
            arr_weight += abs(i - final_state[arr[i * arr_len + j]][0]) + abs(j - final_state[arr[i * arr_len + j]][1])

    return arr_weight

def sum_of_pow(arr, final_state):
    arr_len = len(arr)
    arr_weight = 0

    for i in range(arr_len):
        for j in range(arr_len):
            if arr[i * arr_len + j] == 0:
                continue
            arr_weight += sqrt(pow(i - final_state[arr[i * arr_len + j]][0], 2) + pow(j - final_state[arr[i * arr_len + j]][1], 2))

    return arr_weight
