def n_k():
    ex = input()
    n = int(ex)
    k = 0

    if n == 1:
        print("1(0)")
    else:
        while (n ** 0.5) % 1 == 0:
            n = int(n ** 0.5)
            k += 1
            break
        print("{}({})".format(n, k))


def k_n():
    n, k = map(int, input().split())
    print(n, k)

    result = (n ** (2 ** k))
    print(result)


n_k()
# k_n()
