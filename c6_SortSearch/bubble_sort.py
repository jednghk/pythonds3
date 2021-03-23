"""takes in a list of numbers
    for pass in range len(lst) - 1:
        for index in range(len(lst)-1):
            if lst[i+1] > lst[i]:
                switch values
    return lst"""


def bubble_sort(lst):
    for iter in range(len(lst) - 1, 0, -1):
        for i in range(iter):
            if lst[i+1] < lst[i]:
                lst[i+1], lst[i] = lst[i], lst[i+1]
    return lst

print(bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))