"""
test:
1. for seq and binary search, run on a sorted list of increasing length
2. test
"""
from random import randrange
import timeit


def quick_sort(arr, start, end):
    if start < end:
        pIndex = partition(arr, start, end)
        arr = quick_sort(arr, start, pIndex - 1)
        arr = quick_sort(arr, pIndex + 1, end)
    return arr


def partition(arr, start, end):
    """takes end as pivot, sets pIndex to first elem, if pIndex < pivot, swap with elem at pI and pI+=1, else pass"""
    pIndex = start
    pivot = arr[end]
    for i in range(start, end):#start + 1?
        if arr[i] < pivot:
            arr[pIndex], arr[i] = arr[i], arr[pIndex]
            pIndex += 1
    arr[end], arr[pIndex] = arr[pIndex], arr[end]
    return pIndex


def seq_search(lst, elem):
    for item in lst:
        if item == elem:
            return True
    return False


def bin_search(lst, elem):
    """base case: n < 2, change: search recursively called on half of list"""
    midpoint = len(lst)//2
    if len(lst) < 2:
        return elem == lst[0]
    else:
        if elem == lst[midpoint]:
            return True
        elif elem > lst[midpoint]:
            return bin_search(lst[midpoint:], elem)
        else:
            return bin_search(lst[:midpoint], elem)


def rand_sort_list(length):
    lst = [randrange(0,1000) for i in range(length)]
    lst = quick_sort(lst, 0, length-1)
    return lst


print('for seq search...')
for i in [2**n for n in range(1, 11)]:
    rand_list = rand_sort_list(i)
    rand_elem = randrange(0,1000)
    T = timeit.Timer('seq_search(rand_list, rand_elem)', '''from __main__ import seq_search,rand_list,rand_elem''')
    print(T.timeit(number=1000))

print('for binary search...')

for i in [2**n for n in range(1, 11)]:
    rand_list = rand_sort_list(i)
    rand_elem = randrange(0,1000)
    T = timeit.Timer('bin_search(rand_list, rand_elem)', '''from __main__ import bin_search,rand_list,rand_elem''')
    print(T.timeit(number=1000))