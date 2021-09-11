def count(num):
    result = 1
    for i in range(1, num+1):
        result = result * i

    count = 0
    for number in str(result)[::-1]:
        if number == '0':
            count += 1
        elif number != '0':
            print(count)
            break

count(12)
count(25)