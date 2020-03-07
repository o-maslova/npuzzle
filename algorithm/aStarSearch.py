import sys
import copy
from .heuristic import sum_of_abs
from .Queue import MyQueue, MyItem


def left_neighbor(arr, i, j):
    if j == 0:
        return 0

    new_arr = copy.deepcopy(arr)
    new_arr[i][j] = new_arr[i][j - 1]
    new_arr[i][j - 1] = 0
    return new_arr


def right_neighbor(arr, i, j):
    if j == len(arr) - 1:
        return 0

    new_arr = copy.deepcopy(arr)
    new_arr[i][j] = new_arr[i][j + 1]
    new_arr[i][j + 1] = 0
    return new_arr


def top_neighbor(arr, i, j):
    if i == 0:
        return 0

    new_arr = copy.deepcopy(arr)
    new_arr[i][j] = new_arr[i - 1][j]
    new_arr[i - 1][j] = 0
    return new_arr


def bottom_neighbor(arr, i, j):
    if i == len(arr) - 1:
        return 0

    new_arr = copy.deepcopy(arr)
    new_arr[i][j] = new_arr[i + 1][j]
    new_arr[i + 1][j] = 0
    return new_arr


def find_neighbors(arr):
    all_neighbors = []
    arr_len = len(arr)

    for i in range(arr_len):
        for j in range(arr_len):
            if arr[i][j] == 0:
                l_n = left_neighbor(arr, i, j)
                r_n = right_neighbor(arr, i, j)
                t_n = top_neighbor(arr, i, j)
                b_n = bottom_neighbor(arr, i, j)
                all_neighbors.append(l_n) if l_n != 0 else 0
                all_neighbors.append(r_n) if r_n != 0 else 0
                all_neighbors.append(t_n) if t_n != 0 else 0
                all_neighbors.append(b_n) if b_n != 0 else 0

    return all_neighbors


def a_star(start_arr):
    weight = sum_of_abs(start_arr)
    nb = find_neighbors(start_arr)

    frontier = MyQueue()
    start_item = MyItem(0, start_arr)
    frontier.append(start_item)

    came_from = {}
    cost_so_far ={}
    came_from[''.join(str(e) for e in start_arr)] = None
    cost_so_far[''.join(str(e) for e in start_arr)] = 0

    current = start_item

    min_soa = sum_of_abs(current.arr)

    while len(frontier.list_items) > 0:
        current = frontier.list_items.pop(0)
        #print(current)
        soa = sum_of_abs(current.arr)
        if soa == 0:
            # print(current.arr)
            break
        if soa < min_soa:
            # print(current.arr)
            min_soa = soa
            
        for next in find_neighbors(current.arr):

            new_cost = cost_so_far[''.join(str(e) for e in current.arr)]

            if ''.join(str(e) for e in next) not in cost_so_far:
                cost_so_far[''.join(str(e) for e in next)] = new_cost
                priority = sum_of_abs(next)
                new_item = MyItem(priority, next)
                frontier.append(new_item)
                came_from[''.join(str(e) for e in next)] = current.arr
            elif new_cost < cost_so_far[''.join(str(e) for e in next)]:
                cost_so_far[''.join(str(e) for e in next)] = new_cost
                came_from[''.join(str(e) for e in next)] = current.arr


    step = current.arr
    path = []
    while step != start_arr:
        path.append(step)
        step = came_from[''.join(str(e) for e in step)]

    path.append(step)

    for element in reversed(path):
        print(element)

    return 0
