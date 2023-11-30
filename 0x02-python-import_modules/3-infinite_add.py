#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    leng = len(argv)
    sum = 0
    for x in range(1, leng):
        sum += int(argv[x])
    print("{:d}".format(sum))
