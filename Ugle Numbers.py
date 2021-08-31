import time

def ugly(n):
    start = time.time()

    i = 0
    next_num = 1

    while i < n:
        test = next_num
        while True:
            if (test % 5) != 0:
                break
            test = test / 5
        while True:
            if (test % 3) != 0:
                break
            test = test / 3
        while True:
            if (test % 2) != 0:
                break
            test = test / 2
        if test == 1:
            i += 1
        next_num += 1
    print(next_num - 1)
    print(time.time() - start)

ugly(11)