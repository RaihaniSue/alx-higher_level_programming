#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    l_ist = my_list[0]
    for i in my_list:
        if i > l_ist:
            l_ist = i
    return (l_ist)
