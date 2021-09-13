import random

n = int(input('반복 횟수: '))

count = 0

for i in range(n):
    x = random.randint(0, 1.0)  # 0 <= x <= 1
    y = random.randint(0, 1.0)  # 0 <= y <= 1
    if (x**2 + y**2) <= 1:  # x^2 + y^2 <= 1 일때 count
        count += 1

# 위의 count 확률은 1/4 값이므로 4를 곱하여 pi 값을 구해준다.
pi = (4 * count) / n
print(pi)