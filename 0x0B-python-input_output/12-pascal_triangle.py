#!/usr/bin/python3
"""function for pascal triangle"""


def pascal_triangle(n):
    """function of a pascal triangle"""
    outer_list = []
    if (n <= 0):
        return (outer_list)
    n = n + 1
    for x in range(1, n):
        if x != 1:
            mey = outer_list[x - 2].copy()
            meya = []
            for a, b in enumerate(mey):
                if a != 0:
                    meya.append(mey[a - 1] + b)
                else:
                    meya.append(1)
            meya.append(1)
            outer_list.append(meya)
        else:
            outer_list.append([1])
    return (outer_list)
