# родительский класс, он же parent, он же superclass, иногда - абстрактный класс
class Rect:
    def __init__(self, w, h):
        if w <= 0 or h <= 0:
            raise ValueError("Размеры прямоугольника должны быть положительными")

        self.w = w
        self.h = h

    def area(self):
        print('Считаем площадь прямоугольника')
        return self.w * self.h

class Square(Rect):  # мы пишем не с нуля, а основываем его на Rect
    def __init__(self, a):
        self.h = a
        self.w = a

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        print('Считаем площадь круга')
        return self.r ** 2 * 3.14


shapes = [Rect(23, 56), Rect(3, 3), Square(7), Circle(5)]

for shape in shapes:
    print(shape.area())
