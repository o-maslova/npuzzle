import sys
from algorithm.aStarSearch import a_star
# from parser import parsing
# from queue import PriorityQueue

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # arr = [[4, 3, 11, 9], [0, 5, 15, 10], [13, 2, 6, 7], [12, 1, 14, 8]] # not solvable
        # arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 15, 14, 0]] # not solvable
        # arr = [[ 7, 4, 3, 5], [6, 2, 11, 8], [12, 10, 13, 9], [0, 14, 1, 15]] # solvable generator
        # arr = [[8, 12, 7, 4], [5, 6, 0, 14], [3, 13, 15, 9], [1, 11, 10, 2]] # solvable
        arr = [[10, 1, 14, 6], [3, 13, 5, 2], [4, 15, 9, 0], [8, 12, 7, 11]]

        # arr = [[5,7,2,0], [13,4,8,11], [14,10,15,1], [12,3,6,9]] # solvable 100%
        # arr = [[3, 2, 6], [1, 4, 0], [8, 7, 5]] # not solvable
        # arr = [[2, 7, 0], [3, 4, 1], [5, 6, 8]] # not solvable
        # arr = [[0, 5, 7], [3, 2, 4], [1, 8, 6]] # solvable
        # arr = [[2, 1, 0], [4, 8, 5], [3, 6, 7]] # solvable something wrong
        # arr = [[8, 5, 0], [7, 6, 2], [1, 3, 4]] # solvable something wrong
        # arr = [[4, 8, 0], [2, 3, 7], [6, 5, 1]] # solvable something wrong
        # arr = [[4, 2, 3], [7, 5, 6], [8, 1, 0]] # solvable something wrong
        # arr = [[7, 3, 4], [6, 0, 5], [8, 1, 2]] # solvable something wrong
        # arr = [[4, 2, 5], [7, 6, 3], [8, 1, 0]] # solvable something wrong
        # arr = [[7, 1, 4], [5, 8, 2], [3, 6, 0]] # solvable something wrong
        # arr = parsing(sys.argv[1])
        a_star(arr)
    else:
        print("usage: npuzzle.py 'filename'")
        print("No file!")
    # arr = [[6, 23, 21, 10, 0], [18, 22, 20, 11, 24], [14, 3, 13, 9, 15], [2, 12, 17, 4, 19], [7, 5, 8, 1, 16]]
    # arr = [[8, 12, 7, 4], [5, 6, 0, 14], [3, 13, 15, 9], [1, 11, 10, 2]]



# arr = [[8, 5, 0], [7, 6, 2], [1, 3, 4]]
#
# arr = [[4, 8, 0], [2, 3, 7], [6, 5, 1]]
#
# arr = [[4, 2, 3], [7, 5, 6], [8, 1, 0]]

# arr = [[7, 3, 4], [6, 0, 5], [8, 1, 2]]
# arr = [[4, 2, 5], [7, 6, 3], [8, 1, 0]]

# arr = [[7, 1, 4], [5, 8, 2], [3, 6, 0]]

# [1, 2, 3]
# [8, 0, 4]
# [7, 6, 5]

# [ 1,  2,  3,  4]
# [12, 13, 14,  5]
# [11,  0, 15,  6]
# [10,  9,  8,  7]

# arr = [[10, 1, 14, 6], [3, 13, 5, 2], [4, 15, 9, 0], [8, 12, 7, 11]]




