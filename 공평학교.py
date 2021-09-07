import random

def shuffle():
    people = int(input())
    p_list = []

    for i in range(1, people+1):
        p_list.append(i)

    random.shuffle(p_list)
    print(p_list)

def table():
    a, b = map(int, input().split())
    print(a, b)
    p_list = [i for i in range(1, a+1)]
    random.shuffle(p_list)
    print(p_list)

    result = ''
    for i in range(len(p_list)):
        result += str(p_list[i]) + ' '
        if (i+1) % b == 0:
            result += '\n'
        else:
            if (i+1) % 2 == 0:
                result += '  '
    print(result)

table()