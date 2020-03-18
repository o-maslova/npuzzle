import sys
import copy
from math import sqrt
from .heuristic import sum_of_abs, sum_of_pow
from .Queue import MyQueue, MyItem
from .finalState import create_final_state


def find_neighbors(arr):
    all_neighbors = []
    arr_len = int(sqrt(len(arr)))

    moves = []
    pos_zero = arr.index(0)
    j, i = pos_zero % arr_len, pos_zero // arr_len
    if i > 0: moves.append(-arr_len)
    if i < arr_len - 1: moves.append(+arr_len)
    if j > 0: moves.append(-1)
    if j < arr_len - 1: moves.append(+1)
    l = list(arr)
    for m in moves:
        l[pos_zero] = l[pos_zero + m]
        l[pos_zero + m] = 0
        all_neighbors.append(tuple(l))
        l[pos_zero + m] = l[pos_zero]
        l[pos_zero] = 0
    return all_neighbors

def is_solvable(arr):
    arr_len = len(arr)
    sum_solv = 0

    for i in range(arr_len):
        for j in range(arr_len):
            if arr[i][j] == 0:
                sum_solv += i + 1
                continue
            k = j - 1
            m = i
            while m >= 0:
                while k >= 0:
                    # print('arr1: ' + str(arr[i][j]) + 'arr2: ' + str(arr[m][k]))
                    if arr[m][k] > arr[i][j]:
                        # print('arr1: ' + str(arr[i][j]) + '; arr2: ' + str(arr[m][k]))
                        sum_solv += 1
                        # print('i: ' + str(i) + '; j: ' + str(j) + '; sum: ' + str(sum_solv))
                    k -= 1
                m -= 1
                k = arr_len - 1


    return sum_solv



def a_star(start_arr):

    final_state_dic, final_state = create_final_state(int(sqrt(len(start_arr))))

    heuristic_function = sum_of_abs
    open_queue = MyQueue()
    start_item = MyItem(1, 0, start_arr)
    open_queue.append(start_item)
    open_set = {start_arr: 1}
    close_set = {}
    path_set = {start_arr: None}
    print(start_arr)
    result_state = None
    len_open_set = 50000
    while len(open_queue.list_items) > 0:
        i = 0
        current_arr = open_queue.list_items.get(i)
        while not current_arr:
            i += 1
            current_arr = open_queue.list_items.get(i)

        current = current_arr.pop()
        if len(current_arr) == 0:
            del open_queue.list_items[i]
        if current.arr == final_state:
            print('FINISHED')
            print(current.arr)
            result_state = current.arr
            break
        try_close_set = close_set.get(current.arr)
        if not try_close_set:
            close_set[current.arr] = 1
            neighbors = find_neighbors(current.arr)
            for next in neighbors:

                new_cost = current.cost + 1
                try_open_set = open_set.get(next)

                if not try_open_set :
                    open_set[next] = 1
                    priority = new_cost + heuristic_function(next, final_state_dic)
                    new_item = MyItem(priority, new_cost, next)
                    open_queue.append(new_item)
                    path_set[next] = current.arr

    print("step")

    path = [result_state]
    step = path_set[result_state]
    while step:

        path.append(step)
        step = path_set[step]

    for element in reversed(path):
        print(element)

    print('LEN: ' + str(len(path)))
    print('Num of Close_set:' + str(len(close_set)))
    print('Num of Open_set:' + str(len(open_set)))
    return 0
