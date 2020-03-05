import sys
from algorithm.aStarSearch import a_star
from parser import parsing


if __name__ == "__main__":
    if len(sys.argv) == 2:
        arr = [[0, 5, 7], [3, 2, 4], [1, 8, 6]]
        # arr = parsing(sys.argv[1])
        a_star(arr)
    else:
        print("usage: npuzzle.py 'filename'")
        print("No file!")
    # arr = [[6, 23, 21, 10, 0], [18, 22, 20, 11, 24], [14, 3, 13, 9, 15], [2, 12, 17, 4, 19], [7, 5, 8, 1, 16]]
    # arr = [[8, 12, 7, 4], [5, 6, 0, 14], [3, 13, 15, 9], [1, 11, 10, 2]]
