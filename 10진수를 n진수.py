digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

def convert(num, n):
    result = []
    while num >= 1:
        if (num % n < 10):
            result.append(str(int(num % n)))
        else:
            result.append(digit[int(num % n)])

        num = num / n
    result.reverse()

    last = ''
    for i in result:
        last += i
    print(last)

ex = int(input('숫자를 입력하세여: '))
print(ex)
n = int(input('진수를 입력하세요: '))
convert(ex, n)