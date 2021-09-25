def compare(n):
    if not n:
        return []
    good, bad = [], []
    for i in range(1, len(n)):
        q = input('what is great?(%d, %d) :' % (n[0], n[i]))
        if int(q) == n[0]:
            bad.append(n[i])
        else:
            good.append(n[i])
    print(good, n[0], bad)
    return compare(good) + [n[0]] + compare(bad)


number = input()
reports = compare([i for i in range(1, int(number) + 1)])
print(reports)
for i in range(int(number)):
    print('rank %d : %d' % (i+1, reports[i]))