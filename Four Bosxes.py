class RectBox:
    # 생성자 함수
    # 딕셔러니형태로 만들어준다.
    def __init__(self):
        self.box = {}

    # 각 꼭지점 사가경 범위 안에 가능한 좌표 값에 따라 넓이가 1인 사각형을 만들어준다.
    # 딕셔러니 키 값은 중복이 되지 않으므로 사각형의 중복되는 경우는 자동 제거 된다.
    def add(self, x1, y1, x2, y2):
        for x in range(x1, x2):
            for y in range(y1, y2):
                self.box[(x, y)] = 1

    # 중복을 제거한 넓이가 1인 사각형의 갯수를 세어준다.
    def area(self):
        return len(self.box)

rect = RectBox()
rect.add(1, 2, 4, 4)
rect.add(2, 3, 5, 7)
rect.add(3, 1, 6, 5)
rect.add(7, 3, 8, 6)
print(rect.area())