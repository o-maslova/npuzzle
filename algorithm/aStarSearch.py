import sys
import copy
from heuristic import sum_of_abs


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

    frontier = []
    frontier.append(start_arr)
    #print(''.join(str(e) for e in start_arr))
    came_from = {}
    cost_so_far ={}
    came_from[''.join(str(e) for e in start_arr)] = None
    cost_so_far[''.join(str(e) for e in start_arr)] = 0
    #print(len(frontier))
    while len(frontier) > 0:
        current = frontier.pop(0)
        #print(current)
        if sum_of_abs(current) == 0:
            print(current)
            break

        for next in find_neighbors(current):
            #print(next)

            new_cost = cost_so_far[''.join(str(e) for e in current)] + 1
            #print(new_cost)
            if ''.join(str(e) for e in next) not in cost_so_far or new_cost < cost_so_far[''.join(str(e) for e in next)]:
                cost_so_far[''.join(str(e) for e in next)] = new_cost
                priority = new_cost + sum_of_abs(next)
                frontier.insert(priority, next)
                came_from[''.join(str(e) for e in next)] = current

    for key in came_from:
        print(key)
    #print(cost_so_far)
    print(start_arr)
    return 0
