#!/usr/bin/python3
def uniq_add(my_list=[]):
    once = 0
    for i in set(my_list):
        once += i
    return (once)
