#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    k = 0
    j = 0
    for k in range(0, x):
        try:
            print("{:d}".format(my_list[k]), end="")
            j += 1
        except (ValueError, TypeError):
            continue
    print()
    return j
