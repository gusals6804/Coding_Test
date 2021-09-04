def part(str):
    part = []
    for i in range(len(str)):
        for j in range(len(str) + 1):
            if len(str[i:j]) > 0:
                part.append(str[i:j])

    return part

def sort(a, b):
    a_part = part(a)
    b_part = part(b)

    comp = []
    comp_len = []
    for i in range(len(a_part)):
        for j in range(len(b_part)):
            if (a_part[i] == b_part[j]):
                comp.append(b_part[j])
                comp_len.append(len(b_part[j]))

    index = comp_len.index(max(comp_len))
    return max(comp_len), comp[index]

a = input()
b = input()
result = sort(a, b)
print(result)
