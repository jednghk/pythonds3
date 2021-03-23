from c4_BasicDataStructures.chapter4_stack import Stack
import string

'''
1. Implement infix to post fix algorithm
2. Implement infix to prefix algorithm
3. Implement pre to post fix algorithm
'''


def infix_postfix(statement):
    list_statement = statement.split()
    op_stack = Stack()
    postfix = []
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    for elem in list_statement:
        stack_top = op_stack.peek()
        if elem in string.ascii_letters or elem in '0123456789':
            postfix.append(elem)
        else:
            if op_stack.is_empty():
                op_stack.push(elem)
            else:
                if elem == '(':
                    op_stack.push(elem)
                elif elem == ')':
                    while op_stack.peek() != '(':
                        postfix.append(op_stack.pop())
                    op_stack.pop()
                elif prec[elem] > prec[stack_top] or stack_top == '(':
                    op_stack.push(elem)
                elif prec[elem] <= prec[stack_top]:
                    while not op_stack.is_empty():
                        postfix.append(op_stack.pop())
                    op_stack.push(elem)

    while not op_stack.is_empty():
        postfix.append(op_stack.pop())
    return ' '.join(postfix)


print(infix_postfix('( A + B ) * C - ( D - E ) * ( F + G )'))


def calculate_postfix(str):
    postfix_statement = str.split()
    op_stack = Stack()
    for elem in postfix_statement:
        if elem in '0123456789':
            op_stack.push(elem)
        elif elem in '+-/*':
            num2 = int(op_stack.pop())
            num1 = int(op_stack.pop())
            if elem == '+':
                op_stack.push(num1 + num2)
            elif elem == '-':
                op_stack.push(num1 - num2)
            elif elem == '*':
                op_stack.push(num1 * num2)
            elif elem == '/':
                if num2 == 0:
                    raise ZeroDivisionError('Cannot divide by 0')
                op_stack.push(num1/num2)
        else:
            raise NameError(f'name {elem} is not defined')
    return op_stack.peek()

def infix_eval(statement):
    postfix = infix_postfix(statement)
    result = calculate_postfix(postfix)
    return result

print(infix_eval('1 + 2 + 3 + 4 + 5'))