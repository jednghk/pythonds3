"""
1. Starts from second element
2. Have current index and current value
3. While the prev value is bigger than current value and current index > 0 (stops at 1, and checks elem at 0)
4. current index = prev value
"""

def insertion_sort(lst):
    for pos in range(1, len(lst)):
        cur_pos = pos
        cur_val = lst[pos]
        while lst[cur_pos-1] > cur_val and cur_pos > 0: #check this
            lst[cur_pos] = lst[cur_pos-1]
            cur_pos -= 1
        lst[cur_pos] = cur_val
    return lst

print(insertion_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))