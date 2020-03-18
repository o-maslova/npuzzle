import sys


def create_final_state(len):
    print(len)
    state = tuple(i % (len * len) for i in range(1, len * len + 1))

    final_state = list(0 for i in range(1, len * len + 1))


    k = 0
    j = 0
    i = 0
    while i < len * len:
        while j < len and final_state[k * len + j] == 0:
            final_state[k * len + j] = state[i]
            i += 1
            j += 1
        k += 1
        j -= 1
        while k < len and final_state[k * len + j] == 0:
            final_state[k * len + j] = state[i]
            i += 1
            k += 1
        k -= 1
        j -= 1
        while j >= 0 and final_state[k * len + j] == 0:
            final_state[k * len + j] = state[i]
            i += 1
            j -= 1
        j += 1
        k -= 1
        while k >= 0 and final_state[k * len + j] == 0:
            final_state[k * len + j] = state[i]
            i += 1
            k -= 1
        k += 1
        j += 1

    final_state_dic = {}
    for i in range(len):
        for j in range(len):
            final_state_dic[final_state[i * len + j]] = (i, j)

    # print(final_state_dic)
    # print('i: ' + str(final_state_dic[10][0]))
    # print('j: ' + str(final_state_dic[10][1]))
    return final_state_dic, tuple(final_state)
