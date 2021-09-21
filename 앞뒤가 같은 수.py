n = int(input())

list = []

i = -1
while len(list) != n:
    i += 1
    number = str(i)
    if number == number[::-1]:
        list.append(number)

print(list[n-1])