#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    size = len(sys.argv) - 1
    i = 1
    if size != 0:
        while i <= size:
            sum += int(sys.argv[i])
            i += 1
    print(sum)
