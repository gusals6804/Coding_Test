ex = input()
print(ex)

# aabcccdbb
# 첫 번째 문자를 가져옴
start = ex[0]
count = 0

result = ''
for i in ex:
    if i == start[-1]:  # 첫 문자의 갯수, [-1]은 리스트의 가장 끝, 다음 문자로 다시 시작
        count += 1
    else:
        start += str(count) + i  # 첫문자 + 갯수 + 다음 문자
        count = 1

result = start + str(count)  # 마지막 문자의 카운트 추가
print(result)