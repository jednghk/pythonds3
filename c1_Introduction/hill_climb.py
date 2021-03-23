'''Implementation of the hill climb algorithm
Started off testing the infinite monkey theorem which states that any randomly generated string will
almost certainly form a coherent string of your choice
To test, I generated completely random strings from start to finish, but the program couldn't get past
30% of the correct letters even after more than a million iterations
Thus I implemented the hill climb algorithm which essentially saved the correct characters and only
randomized the incorrect characters.
This dramatically reduced the number of iterations, ranging from 50-150
'''

import string
import random


def gen_rand_char():
    alphabet = string.ascii_lowercase + ' '  # length: 27 characters
    random_char = alphabet[random.randrange(27)]
    return random_char


def empty_list():
    return ['0'] * 28


def convert_str(list):
    return ''.join(list)


correct_str = 'methinks it is like a weasel'
iterator = 0
top_percent_match = 0
initial_list = empty_list()

while convert_str(initial_list) != correct_str:
    score = 0
    for index in range(28):
        if initial_list[index] == '0' or correct_str[index] != initial_list[index]:
            initial_list[index] = gen_rand_char()
        else:
            score += 1
    iterator += 1
    match_ratio = (score / 28) * 100
    print(convert_str(initial_list))

    if match_ratio > top_percent_match:
        top_percent_match = match_ratio
        print(convert_str(initial_list), top_percent_match, iterator)

print(iterator)
