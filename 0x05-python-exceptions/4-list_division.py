#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    k = 0
    list_pr = []
    res = 0
    for k in range(0, list_length):
        try:
            res = (my_list_1[k] / my_list_2[k])
        except TypeError:
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            list_pr.append(res)
    return list_pr
