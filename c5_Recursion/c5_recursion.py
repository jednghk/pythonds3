def reverse(string):
    if len(string) == 1:
        return string
    else:
        return reverse(string[1:])+ string[0]


def calculate_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * calculate_factorial(n-1)


def change_base(num, new_base):
    """accepts a base 10 number and base as a parameter, then returns a number of that base"""
    convert_string = '0123456789ABCDEF'
    if num%new_base == num:
        return convert_string[num]
    else:
        return change_base(num//new_base, new_base) + convert_string[num % new_base]


def remove_white(s):
    new_str = s.lower()
    return ''.join(new_str.split())


def palindrome_checker(s):
    s = remove_white(s)
    if len(s) <= 1:
        return True
    else:
        front = s[0]
        back = s[-1]
        return front == back and palindrome_checker(s[1:-1])

print(palindrome_checker(''))