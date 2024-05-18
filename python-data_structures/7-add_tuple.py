#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b
    if len(a) < 2:
        a = a + (0, 0)
    else:
        a[:2]
    if len(b) < 2:
        b = b + (0, 0)
    else:
        b[:2]
    result = (a[0] + b[0], a[1] + b[1])
    return result
