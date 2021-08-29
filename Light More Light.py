def light(n):
    if n == 0:
        return
    switch = -1
    for i in range(1, n+1):
        if n % i == 0:
          switch *= -1

    if switch == -1:
        print('no')
    else:
        print('yes')

light(5)