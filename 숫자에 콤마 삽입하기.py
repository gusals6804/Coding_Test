def comma(n):
    # 숫자가 3자리면 바로 출력
    if len(n) < 4:
        return n
    # 음수인 경우 '-'를 제외하고 숫자를 다시 재귀함수로 리턴
    if n[0]=="-":
        return "-"+comma(n[1:])
    # 소수 점이 있는경우 소수 점을 기준으로 숫자를 분할하여 다시 재귀함수로 리턴
    if "." in n:
        return comma(n[:n.find(".")]) + n[n.find("."):]
    # 소수점과 마이너스 부호를 제거후 4자리 이상일 경우 3자리 단위로 콤마를 붙힘
    if len(n) >= 4:
        return comma(n[:-3]) + ',' + n[-3:]

# n=input("숫자를 입력하십시오: ")
# print(comma(n))

str = 'abcabcabc'
index = str.find('b')
print(index)

ex = '4545.12'
print(ex[:ex.find('.')])
print(ex[ex.find('.'):])