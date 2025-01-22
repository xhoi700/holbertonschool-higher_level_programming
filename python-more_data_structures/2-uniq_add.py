#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = set(my_list)
    sum1= 0
    for num in my_list:
        sum1 += num 
    return sum1
