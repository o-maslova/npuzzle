import sys


# arr = [[0, 5, 7], [3, 2, 4], [1, 8, 6]]
def sum_of_abs(arr):
    arr_len = len(arr)
    arr_weight = 0

    for i in range(arr_len):
        for j in range(arr_len):
            if arr[i][j] == 0:
                continue
            arr_weight += abs(i - (arr[i][j] - 1) // arr_len) + abs(j - (arr[i][j] - 1) % arr_len)

    return arr_weight
