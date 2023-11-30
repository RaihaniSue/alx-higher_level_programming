#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    leng = len(argv) - 1
    if leng == 0:
        print("{}".format("0 arguments."))
    elif leng == 1:
        print("{}".format("1 argument:"))
        print("1: {}".format(argv[1]))
    else:
        print("{:d} {}".format(leng, "arguments:"))
        for i in range(1, leng + 1):
            print("{:d}: {}".format(i, argv[i]))
