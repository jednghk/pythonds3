"""
Binary search algorithm
1. assign start and end to start and end of list
2. check midpoint(start+end)/2
3. if num, return true, elif > midpoint + 1, assign start to midpoint elif < midpoint, assign end to midpoint
4. do until first <= last
"""
from random import randrange
from c6_SortSearch import quick_sort

def binary_search(lst, num):
    first = 0
    last = len(lst) - 1
    while first <= last:
        midpoint = (first + last)//2
        if lst[midpoint] == num:
            return True
        elif num > lst[midpoint]:
            first = midpoint + 1
        elif num < lst[midpoint]:
            last = midpoint - 1
    return False


def rec_bin_search(lst, num):
    if len(lst) == 1:
        return num == lst[0]
    else:
        midpoint = (len(lst))//2
        if num > lst[midpoint]:
            return rec_bin_search(lst[midpoint+1:], num)
        elif num < lst[midpoint]:
            return rec_bin_search(lst[:midpoint], num)
        else:
            return True


def rand_sort_list(length):
    lst = [randrange(0,1000) for i in range(length)]
    lst = quick_sort(lst, 0, length-1)
    return lst

print(rand_sort_list(10))
'''print(rec_bin_search(rand_sort_list(10), randrange(0, 1000)))'''
