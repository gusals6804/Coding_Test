def sort(ex):
    for i in range(1, len(ex)):
        for j in range(i):
            if ex[j] > ex[i]:
                ex.insert(j, ex[i])
                ex.pop(i+1)
        print(ex)
    return ex

a = [5,1,2,3,4]
print(sort(a))