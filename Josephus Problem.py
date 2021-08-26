num_people, k = map(int, input().split())
print(num_people, k)

num_list = list(range(1, num_people+1))
comp_list = list(range(1, num_people+1))

count = k - 1
while count < len(comp_list):
    num_list.remove(comp_list[count])
    print(num_list, comp_list, comp_list[count])
    count += k
    if count >= len(comp_list):
        comp_list.extend(num_list)

print(num_list[0])