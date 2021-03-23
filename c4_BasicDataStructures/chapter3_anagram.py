'''
method 1: sort and compare: call sort method and compare equality of sorted list
method 2: convert to set, call count method on each element in set on both strings, return False once count is not the
same
method 3: just call count on each letter from string 1 and 2, then compare
'''
import time

def sort_and_compare(str1, str2):
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    if str1_sorted == str2_sorted:
        return True
    else:
        return False


def count_letters(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        letter_set = set(str1)
        for letter in letter_set:
            if str1.count(letter) != str2.count(letter):
                return False
            else:
                pass
        return True

def check_off(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        list1 = list(str1)
        list2 = list(str2)
        for i in range(len(list1)):
            if list1[i] in list2:
                list2.remove(list1[i])
            else:
                return False
        return True
#2 + n^2

start_time = time.time()
print(count_letters("apple", "pleap"))  # expected: True
print(count_letters("abcd", "dcba"))  # expected: True
print(count_letters("abcd", "dcda"))  # expected: False
end_time = time.time()

print(end_time-start_time)