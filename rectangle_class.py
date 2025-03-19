class Rect:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Размеры прямоугольника должны быть положительными")

        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __repr__(self):  # represent представить в виде текста
        return f"Rect({self.width}, {self.height}"

    def is_larger_than(self, other):
        return self.area() > other.area()  # True/False

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

r1 = Rect(5, 6)
r2 = Rect(8, 12)
r3 = Rect(3, 10)
r4 = r1

rects = [r1, r2, r3]

print(rects)
print(r1.is_larger_than(r2))
print(r1 > r3)
print(r1 == r3)
