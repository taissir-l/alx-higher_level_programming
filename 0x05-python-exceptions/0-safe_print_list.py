#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n_list = my_list[:x]
        print(''.join(str(s) for s in n_list))
        count = 0
        for i in n_list:
            count += 1
        return count
    except IndexError:
        num = my_list[-1:]
        count2 = 0
        for i in my_list:
            count2 += 1
        return
