from random import randrange
import time


def findmin(lst):
    min_num = lst[0]
    for n in range(len(lst)):
        if lst[n] < min_num:
            min_num = lst[n]
    return min_num
#T(n) = 1 + 2n


def findmin2(lst):
    min_num = list[0]
    for num in lst:
        for comparer in lst:
            if comparer > num:
                break


random_list = [randrange(1000) for i in range(1000000)]
start_time = time.time()
findmin(random_list)
end_time = time.time()



print(start_time - end_time)