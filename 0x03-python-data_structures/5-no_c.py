#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for i in my_string:
        if i != 103 and i != 143:
            new += i
        return new
