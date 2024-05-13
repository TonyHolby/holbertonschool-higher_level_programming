#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b
    a = a + (0, 0) if len(a) < 2 else a[:2]
    b = b + (0, 0) if len(b) < 2 else b[:2]
    result = (a[0] + b[0], a[1] + b[1])
    return result
