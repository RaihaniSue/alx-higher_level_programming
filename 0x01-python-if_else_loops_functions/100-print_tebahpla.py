#!/usr/bin/python3
k = 0
for alpha in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(alpha - k)), end="")
    k = 32 if k == 0 else 0
