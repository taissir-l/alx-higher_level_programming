#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        x = 0
        biggest = ""
        for i in my_list:
            if a_dictionary[i] > x:
                x = a_dictionary[i]
                biggest = i
        return biggest
