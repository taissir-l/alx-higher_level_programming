#!/usr/bin/python3
def no_c(my_string):
    up_str = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            up_str += i
    return (up_str)
