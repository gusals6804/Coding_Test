def dist(left, right, mid, pos, hand):
    x, y = 0, 1
    dist_l = abs(pos[left][x] - pos[mid][x]) + abs(pos[left][y] - pos[mid][y])
    dist_r = abs(pos[right][x] - pos[mid][x]) + abs(pos[right][y] - pos[mid][y])

    if dist_l < dist_r:
        return 'L'
    elif dist_l == dist_r:
        if hand == 'right':
            return 'R'
        else:
            return 'L'
    else:
        return 'R'


def solution(numbers, hand):
    left = [1, 4, 7]
    right = [3, 6, 9]

    # 좌표로 변환
    position = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    # 초기값 설정
    left_num, right_num = '*', '#'

    answer = ''
    for i in numbers:
        # 왼쪽 키패드
        if i in left:
            answer += 'L'
            left_num = i
        # 오른쪽 키패드
        elif i in right:
            answer += 'R'
            right_num = i
        # 가운데
        else:
            dist_result = dist(left_num, right_num, i, position, hand)

            if dist_result == 'L':
                left_num = i
            else:
                right_num = i

            answer += dist_result

    print(answer)
    return answer

