#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_add = [0, 0]

    if len(tuple_a) < 2:
        tuple_add[0] = tuple_a[0] if len(tuple_a) > 0 else 0
        tuple_add[1] = 0 + tuple_b[1] if len(tuple_b) > 1 else 0
    if len(tuple_b) < 2:
        tuple_add[0] = tuple_a[0] if len(tuple_a) > 0 else 0
        tuple_add[1] = tuple_a[1] if len(tuple_a) > 1 else 0
    else:
        tuple_add[0] = tuple_a[0] + tuple_b[0]
        tuple_add[1] = tuple_a[1] + tuple_b[1]

    return tuple_add[0], tuple_add[1]
