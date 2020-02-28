import sys
from parser import parsing


if __name__ == "__main__":
    if len(sys.argv) == 2:
        parsing(sys.argv[1])
    else:
        print("usage: npuzzle.py 'filename'")
        print("No file!")
