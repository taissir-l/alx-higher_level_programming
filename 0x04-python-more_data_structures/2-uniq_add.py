#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    new_sum = 0

    for num in my_list:
        if num not in new_list:
            new_sum += num
            new_list.append(num)
    return new_sum
