def cycle(n):
    sum = 1
    while n != 1:
        if (n % 2) == 0:
            n = n/2
            sum += 1
        else:
            n = 3 * n + 1
            sum += 1

    return sum

max_num = int(input('max: '))
min_num = int(input('min: '))


comp_list = []

for i in range(min_num, max_num+1):
    comp_list.append(cycle(i))

print(max(comp_list))