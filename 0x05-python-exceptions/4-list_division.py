#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length
    for l in range(len(my_list_1)):
        try:
            result[l] = my_list_1[l] / my_list_2[l]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
    return result
