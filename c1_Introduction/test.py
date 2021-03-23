'''
Testing O(1) for list index operator
a. testing
    1. create a list of random length, from 1 to 100000
    2. generate a random index within the list length
    3. repeat process 1000 times and record timing for each iteration
    3. use time it on the function list[index]
b. evaluation
    1.
'''

import timeit
from random import randrange


def list_index_test():
    random_list = [randrange(10001) for i in range(randrange(10001))]
    random_idx = randrange(10001)
    return random_list[random_idx]

def dict_get_test():
    random_length = randrange(1000)
    random_dict = {i: None for i in range(random_length)}
    return random_dict.get(randrange(1000))


def dict_set_test():
    random_length = randrange(1000)
    random_dict = {i: None for i in range(random_length)}
    random_dict[random_length] = randrange(1000)


def smallest_num_test(list_len):
    '''generates a random length list of random numbers, and finds smallest number'''
    random_list = [randrange(1000) for i in range(list_len)]
    min_so_far = random_list[0]
    for elem in random_list:
        if elem < min_so_far:
            min_so_far = elem
    return min_so_far


for n in [1, 10, 100, 1000, 10000]:
    list_l = n
    T = timeit.Timer('smallest_num_test(list_l)', '''from __main__ import smallest_num_test
from __main__ import list_l''')
    print(T.timeit(number = 1000))
