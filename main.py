import sys
from algorithm.aStarSearch import a_star
# from parser import parsing


if __name__ == "__main__":
    if len(sys.argv) == 2:
        # arr = [[4, 3, 11, 9], [0, 5, 15, 10], [13, 2, 6, 7], [12, 1, 14, 8]] # not solvable
        # arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 15, 14, 0]] # not solvable
        # arr = [[8, 12, 7, 4], [5, 6, 0, 14], [3, 13, 15, 9], [1, 11, 10, 2]] # solvable
        # arr = [[3, 2, 6], [1, 4, 0], [8, 7, 5]] # not solvable
        # arr = [[2, 7, 0], [3, 4, 1], [5, 6, 8]] # not solvable
        # arr = [[0, 5, 7], [3, 2, 4], [1, 8, 6]] # solvable
        arr = [[2, 1, 0], [4, 8, 5], [3, 6, 7]] # solvable

        # arr = parsing(sys.argv[1])
        a_star(arr)
    else:
        print("usage: npuzzle.py 'filename'")
        print("No file!")
    # arr = [[6, 23, 21, 10, 0], [18, 22, 20, 11, 24], [14, 3, 13, 9, 15], [2, 12, 17, 4, 19], [7, 5, 8, 1, 16]]
    # arr = [[8, 12, 7, 4], [5, 6, 0, 14], [3, 13, 15, 9], [1, 11, 10, 2]]



    # [3, 2, 6]
    # [1, 4, 0]
    # [8, 7, 5]

    # sum = 2 + 2

    # [0, 5, 7]
    # [3, 2, 4]
    # [1, 8, 6]

