total = 0
diff_ang = [90, 270] # 90도 270도
for hour in range(0, 24):
    for ang in diff_ang:
        move_ang = (360 * hour) + ang # 0, 90, 270, 450...
        m = move_ang / 5.5 # 직각일 때 분을 계산
        # 분을 60으로 나누어 시간을 계산
        h = m // 60
        if h < 24:
            print('%02d : %02d' % (h, (m % 60)))
            total += 1

print('total %d번!' % total)