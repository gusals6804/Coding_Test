import random

list = [2, 3, 1, 6, 5, 7]

list_len = 0

if len(list) % 2 == 0:
    list_len = len(list) / 2
else:
    list_len = (len(list) / 2) + random.randint(0, 1)

for i in range(int(list_len)):
    list.pop(random.randint(0, len(list)-1))

print(list)