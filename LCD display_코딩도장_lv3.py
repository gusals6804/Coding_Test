#숫자 생성에 필요한 문자열
digit_chart = ("   ", " - ", "|  ", "| |", "  |")

# 각 숫자 생성에 필요한 문자
num_digit = ((1, 3, 0, 3, 1),  # 0
             (0, 4, 0, 4, 0),  # 1
             (1, 4, 1, 2, 1),  # 2
             (1, 4, 1, 4, 1),  # 3
             (0, 4, 1, 4, 0),  # 4
             (1, 2, 1, 4, 1),  # 5
             (1, 2, 1, 3, 1),  # 6
             (1, 4, 0, 4, 0),  # 7
             (1, 3, 1, 3, 1),  # 8
             (1, 3, 1, 4, 0))  # 9

def show_Digit(size, num):
    for i in range(5):
        output = []
        for digit in [int(n) for n in str(num)]:
            n = num_digit[digit][i]
            output.append(digit_chart[n][0] + digit_chart[n][1] * size + digit_chart[n][2]) #숫자의 필요한 문자 한개 행 씩 생성, 사이즈에 따라 "ㅡ" 추가

        for j in range(size if i == 1 or i == 3 else 1):
            print(" ".join(output), i, j)  # 1, 3번째 문자열은 세로로 size만큼 출력

show_Digit(4, 5)
