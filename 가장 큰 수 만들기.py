num_list = list(map(int, input().split()))
print(num_list)

num_len = []
for num in num_list:
    num_len.append(len(str(num)))

max_num_len = max(num_len)
print(max_num_len)

sort_list = []
compare_list = []
num_size =1
while num_size <= max_num_len:
    for num in num_list:
        if len(num):
            compare_list.append(str(num)[num_size-1])



    num_size += 1

sort_list.sort()
sort_list.reverse()

print(sort_list)
#3 30 34 5 9