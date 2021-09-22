def split(a):
    b = int(a)
    result = []
    for i in range(a, 0, -1):
        
        while i**2 <= b:
            result.append(i)
            b -= i**2
        if b == 0:
            print(a,'는', result,'의 제곱수로 이루어져 있습니다.')
    return

# num = int(input('숫자를 입력하세요: '))
# split(num)

for i in range(10, 0, -1):
    print(i)