import random

cat = random.randint(1,7)
find = random.randint(1,7)
day = 1

if cat == find:
    print('{} day'.format(day))
else:
    while 1:
        day += 1
        while 1:
            move = random.randint(-1,1)
            if move != 0:
                break
        cat += move

        if cat < 1:
            cat += 2
        elif cat > 7:
            cat -= 2

        find = random.randint(1,7)

        if find == cat:
            print('{} days'.format(day))
            break

