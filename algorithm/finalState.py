import sys


def create_final_state(len):
    state = []
    for i in range(len * len):
        state.append(i + 1)
    state[len * len - 1] = 0

    final_state = []
    for i in range(len):
        final_state.append([])
        for j in range(len):
            final_state[i].append(0)

    k = 0
    j = 0
    i = 0
    while i < len * len:

        while j < len and final_state[k][j] == 0:
            final_state[k][j] = state[i]
            i += 1
            j += 1
        k += 1
        j -= 1
        while k < len and final_state[k][j] == 0:
            final_state[k][j] = state[i]
            i += 1
            k += 1
        k -= 1
        j -= 1
        while j >= 0 and final_state[k][j] == 0:
            final_state[k][j] = state[i]
            i += 1
            j -= 1
        j += 1
        k -= 1
        while k >= 0 and final_state[k][j] == 0:
            final_state[k][j] = state[i]
            i += 1
            k -= 1
        k += 1
        j += 1

    final_state_dic = {}
    for i in range(len):
        for j in range(len):
            final_state_dic[final_state[i][j]] = [i, j]

    # print(final_state_dic)
    # print('i: ' + str(final_state_dic[10][0]))
    # print('j: ' + str(final_state_dic[10][1]))
    return final_state_dic
