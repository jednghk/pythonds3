"""
1. Have accumulator to check largest
2. Iterator should reduce by 1 every iteration
3. once end of iterator reached, swap index of number with last index
"""


def selection_sort(lst):
    largest_index = 0
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j+1] > lst[j]:
                largest_index = j+1
        lst[largest_index], lst[i] = lst[i], lst[largest_index]
    return lst

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)