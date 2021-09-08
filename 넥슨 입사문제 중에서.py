# 제네레이터 구해주는 함수
def gen(n):
    # 숫자 단위에 따라 각 자리수를 몫과 나머지로 구할 수 있지만 str형식 list로 받아서 각 자리수를 분해
    d = 0
    for i in list(str(n)):
         d = d + int(i)
    return d + n

# 셀프 넘버 구하고 합산하는 함수
def self(n):
    g = []
    s = []
    for i in range(1, n):
        g.append(gen(i))

    for i in range(1, n):
        if i in g:
            pass
        else:
            s.append(i)

    sum = 0
    for i in s:
        sum = sum + i

    print(s)
    print(sum)

self(5000)



