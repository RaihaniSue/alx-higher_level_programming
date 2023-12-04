#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    l_ist = []
    for i in my_list:
        if i % 2 == 0:
            l_ist.append(True)
        else:
            l_ist.append(False)
    return (l_ist)
