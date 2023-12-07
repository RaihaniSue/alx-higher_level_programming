#!/usr/bin/python3
def search_replace(my_list, search, replace):
    l_ist = my_list[:]
    for x in range(len(l_ist)):
        if l_ist[x] == search:
            l_ist[x] = replace
    return (l_ist)
