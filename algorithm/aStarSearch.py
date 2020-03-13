import sys
import copy
from .heuristic import sum_of_abs, sum_of_pow
from .Queue import MyPriorityQueue, MyItem
from .finalState import create_final_state

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
                break

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

# def is_solvable(arr):
#     arr_len = len(arr)
#     sum_solv = 0
#
#     for i in range(arr_len):
#         for j in range(arr_len):
#             if arr[i][j] == 0:
#                 sum_solv += i + 1
#                 print("sum1: " + str(sum_solv))
#                 continue
#             k = j + 1
#             while k < arr_len:
#                 if arr[i][j] > arr[i][k] and arr[i][k] != 0:
#                     sum_solv += 1
#                     print("sum2: " + str(sum_solv))
#
#                 k += 1
#
#
#     return sum_solv

def a_star(start_arr):
    final_state = create_final_state(len(start_arr))

    heuristic_function = sum_of_abs
    start_item = MyItem(0, start_arr, None)
    complexity_time = 0
    complexity_size = 1
    actual_size = 1
    opened_heap = MyPriorityQueue()
    opened_heap.push(start_item)
    opened_set = []
    closed_set = []
    opened_set.append(start_arr)
    print(''.join(str(e) for e in start_item.arr))
    solution = None
    while not solution and not opened_heap.is_empty():

        current = opened_heap.pop()
        closed_set.append(current)


        if current.arr not in closed_set:
            closed_set.append(current.arr)
            opened_set.remove(current.arr)
            # print(''.join(str(e) for e in current.arr))
            # input()
            neighbors = find_neighbors(current.arr)
            for next_arr in neighbors:
                if next_arr in closed_set:
                    continue

                h_f = heuristic_function(next_arr, final_state)
                new_cost = current.cost + 1
                priority = new_cost + h_f
                next = MyItem(priority, next_arr, current)
                if h_f == 0:
                    print('FINISHED')
                    solution = next
                    break
                opened_heap.push(next)
                opened_set.append(next_arr)

    if not solution:
        print("No path found")
        return

    path = []
    while solution:
        path.append(solution.arr)
        solution = solution.previous
    path.reverse()
    for step in path:
        print(step)

    print("LEN: " + str(len(path)))
    print("CLOSED: " + str(len(closed_set)))
    print("OPENED: " + str(len(opened_set)))




                # new_cost = cost_so_far[current_arr_str] + 1
                # new_arr_str = ''.join(str(e) for e in next)
                # if new_arr_str not in cost_so_far or new_cost < cost_so_far[new_arr_str]:
                #     cost_so_far[new_arr_str] = new_cost
                #
                #     if new_arr_str not in close_set:
                #         priority = new_cost + heuristic_function(next, final_state)
                #         new_item = MyItem(priority, next)
                #         if max_priority < priority:
                #             max_priority = priority
                #             open_set.append(new_item, True)
                #         else:
                #             open_set.append(new_item)
                #
                #     came_from[new_arr_str] = current.arr


    # step = current.arr
    # path = []
    # while step != start_arr:
    #     path.append(step)
    #     step = came_from[''.join(str(e) for e in step)]
    #
    # path.append(step)
    #
    # for element in reversed(path):
    #     print(element)
    #
    # print('LEN: ' + str(len(path)))
    # print('Num of Close_set:' + str(len(close_set)))
    # print('Num of Open_set:' + str(len(open_set.list_items)))

    return 0


# import sys
# import copy
# from .heuristic import sum_of_abs, sum_of_pow
# from .Queue import MyQueue, MyItem
# from .finalState import create_final_state
# from queue import PriorityQueue
#
#
# def left_neighbor(arr, i, j):
#     if j == 0:
#         return 0
#
#     new_arr = copy.deepcopy(arr)
#     new_arr[i][j] = new_arr[i][j - 1]
#     new_arr[i][j - 1] = 0
#     return new_arr
#
#
# def right_neighbor(arr, i, j):
#     if j == len(arr) - 1:
#         return 0
#
#     new_arr = copy.deepcopy(arr)
#     new_arr[i][j] = new_arr[i][j + 1]
#     new_arr[i][j + 1] = 0
#     return new_arr
#
#
# def top_neighbor(arr, i, j):
#     if i == 0:
#         return 0
#
#     new_arr = copy.deepcopy(arr)
#     new_arr[i][j] = new_arr[i - 1][j]
#     new_arr[i - 1][j] = 0
#     return new_arr
#
#
# def bottom_neighbor(arr, i, j):
#     if i == len(arr) - 1:
#         return 0
#
#     new_arr = copy.deepcopy(arr)
#     new_arr[i][j] = new_arr[i + 1][j]
#     new_arr[i + 1][j] = 0
#     return new_arr
#
#
# def find_neighbors(arr):
#     all_neighbors = []
#     arr_len = len(arr)
#
#     for i in range(arr_len):
#         for j in range(arr_len):
#             if arr[i][j] == 0:
#                 l_n = left_neighbor(arr, i, j)
#                 r_n = right_neighbor(arr, i, j)
#                 t_n = top_neighbor(arr, i, j)
#                 b_n = bottom_neighbor(arr, i, j)
#                 all_neighbors.append(l_n) if l_n != 0 else 0
#                 all_neighbors.append(r_n) if r_n != 0 else 0
#                 all_neighbors.append(t_n) if t_n != 0 else 0
#                 all_neighbors.append(b_n) if b_n != 0 else 0
#                 break
#
#     return all_neighbors
#
# def is_solvable(arr):
#     arr_len = len(arr)
#     sum_solv = 0
#
#     for i in range(arr_len):
#         for j in range(arr_len):
#             if arr[i][j] == 0:
#                 sum_solv += i + 1
#                 continue
#             k = j - 1
#             m = i
#             while m >= 0:
#                 while k >= 0:
#                     # print('arr1: ' + str(arr[i][j]) + 'arr2: ' + str(arr[m][k]))
#                     if arr[m][k] > arr[i][j]:
#                         # print('arr1: ' + str(arr[i][j]) + '; arr2: ' + str(arr[m][k]))
#                         sum_solv += 1
#                         # print('i: ' + str(i) + '; j: ' + str(j) + '; sum: ' + str(sum_solv))
#                     k -= 1
#                 m -= 1
#                 k = arr_len - 1
#
#
#     return sum_solv
#
# # def is_solvable(arr):
# #     arr_len = len(arr)
# #     sum_solv = 0
# #
# #     for i in range(arr_len):
# #         for j in range(arr_len):
# #             if arr[i][j] == 0:
# #                 sum_solv += i + 1
# #                 print("sum1: " + str(sum_solv))
# #                 continue
# #             k = j + 1
# #             while k < arr_len:
# #                 if arr[i][j] > arr[i][k] and arr[i][k] != 0:
# #                     sum_solv += 1
# #                     print("sum2: " + str(sum_solv))
# #
# #                 k += 1
# #
# #
# #     return sum_solv
#
# def a_star(start_arr):
#     final_state = create_final_state(len(start_arr))
#     # print(is_solvable(start_arr))
#     # if is_solvable(start_arr) % 2 == 1:
#     #     print("NOT SOLVABLE")
#     #     return
#
#     heuristic_function = sum_of_abs
#     # open_set = MyQueue()
#     # start_item = MyItem(0, start_arr)
#     # open_set.append(start_item)
#     open_set = PriorityQueue()
#     open_set.put(start_arr, 0)
#     came_from = {}
#     cost_so_far = {}
#     came_from[''.join(str(e) for e in start_arr)] = None
#     cost_so_far[''.join(str(e) for e in start_arr)] = 0
#     close_set = {}
#     current = start_arr
#
#     # min_h_f = heuristic_function(current.arr, final_state)
#     print(''.join(str(e) for e in current))
#     while not open_set.empty():
#         current = open_set.get()
#         h_f = heuristic_function(current, final_state)
#         current_arr_str = ''.join(str(e) for e in current)
#         if h_f == 0:
#             print('FINISHED')
#             print(current)
#             break
#         # if h_f < min_h_f:
#         #     print(current.arr)
#         #     min_h_f = h_f
#         if current_arr_str not in close_set:
#             close_set[current_arr_str] = current
#             # print(''.join(str(e) for e in current.arr))
#             # input()
#             neighbors = find_neighbors(current)
#             for next in neighbors:
#                 new_cost = cost_so_far[current_arr_str] + 1
#                 new_arr_str = ''.join(str(e) for e in next)
#                 if new_arr_str not in cost_so_far or new_cost < cost_so_far[new_arr_str]:
#                     cost_so_far[new_arr_str] = new_cost
#                     priority = new_cost + heuristic_function(next, final_state)
#                     open_set.put(next, priority)
#                     came_from[new_arr_str] = current
#
#
#     step = current
#     path = []
#     while step != start_arr:
#         path.append(step)
#         step = came_from[''.join(str(e) for e in step)]
#
#     path.append(step)
#
#     for element in reversed(path):
#         print(element)
#
#     print('LEN: ' + str(len(path)))
#     print('Num of Close_set:' + str(len(close_set)))
#     print('Num of Open_set:' + str(open_set.qsize()))
#
#     return 0
