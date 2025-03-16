class Rect:
    def __init__(self, w, h):
        if w <= 0 or h <= 0:
            raise ValueError("Размеры прямоугольника должны быть положительными")

        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def __repr__(self):  # represent, представить в виде текста
        return f'Rect({self.w}, {self.h})'  # имеем право сделать любой текст, но есть общепринятый формат

    def is_larger_than(self, other):
        return self.area() > other.area()  # True / False

    def __gt__(self, other):  # greater than, >
        return self.area() > other.area()

    def __lt__(self, other):  # less than, <
        return self.area() < other.area()

    def __eq__(self, other):  # equals, ==
        return self.area() == other.area()

    def __ne__(self, other):  # not equal, !=
        return self.area() != other.area()

    def __ge__(self, other):  # greater or equal, >=
        # return self > other or self == other
        return self.area() >= other.area()

    def __le__(self, other):  # less or eual , <=
        return self.area() <= other.area()

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            #raise TypeError('Прямоугольники умножаем только на числа!')  # но потом сделаем иначе
            return NotImplemented  # чтобы у питона была возможность попробовать поменять множители местами

        return Rect(self.w * (other) ** 0.5, self.h * (other) ** 0.5)  # умножаем стороны на корень


r1 = Rect(5, 6)
r2 = Rect(8, 12)
r3 = Rect(3, 10)
r4 = r1
rects = [r1, r2, r3]

print(rects)
print(r1.is_larger_than(r2))
print(r1 > r3)
print(r1 == r3)
print(r1 == r4)

print(min(r1, r2))
print(sorted(rects))

r5 = r1 * 5
print(r5, r5.area(), r1.area())