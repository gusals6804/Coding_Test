def spatial(a,b):
    matrix = [[0 for i in range(a)] for i in range(b)]

    row_size = a
    col_size = b
    inc = 1
    num = 0
    row = 0
    col = -1
    while row_size > 0 and col_size > 0:
        # 오른쪽으로 열의 위치가 증가할 때 마다 1씩 증가
        for i in range(row_size):
            col = col + inc
            matrix[row][col] = num
            num = num + 1

        # 밑으로 내려갈 때 증가하는 범위가 하
        # 나 씩 줄어듬
        col_size -= 1

        # 밑으로 내려가면서 1씩 증가
        for i in range(col_size):
            row = row + inc
            matrix[row][col] = num
            num = num + 1

        row_size -= 1

        # 반대방향
        inc *= -1

    # 출력
    for i in range(b):
        for j in range(a):
            print(matrix[i][j], end="\t")
        print()

spatial(6, 6)