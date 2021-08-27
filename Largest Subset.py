def lagest_subset(lst):
    set_num = set(lst)
    subset = []

    for n in set_num:
        if n - 1 not in set_num:
            sub = [n]
            print(subset)
            while sub[-1] + 1 in set_num:
                sub.append(sub[-1] + 1)
            subset.append(sub)

    #print(subset)

    max_index = 0
    max_len = 0
    for i in range(len(subset)):
        if len(subset[i]) > max_len:
            max_len = len(subset[i])
            max_index = i

    return subset[max_index]

list = [1,6,5,4,7,12,15,13,14,11]
print(lagest_subset(list))