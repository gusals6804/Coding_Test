import random

# 랜덤 10개를 뽑아서 중복 제거 하고 크기 순으로 정렬
point = list(set(list([random.randint(1, 100) for i in range(10)])))
point.sort()
print(point)

# 이미 크기 순으로 정렬되어 있으므로 처음부터 앞뒤 숫자 거리만 비교
# 첫번째 두번째 숫자 거리를 먼저 비교해서 더 작은경우 index로 업데이트
dist = point[1] - point[0]
index = 0

for i in range(1, len(point)):
    if point[i] - point[i-1] < dist:
        dist = point[i] - point[i-1]
        index = i
        print(dist, index)

print(point[index-1], point[index])