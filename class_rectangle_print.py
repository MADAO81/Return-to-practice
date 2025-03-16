class Rect:
    def __init__(self, w, h):
        if w <= 0 or h <= 0:
            raise ValueError("Размеры прямоугольника должны быть положительными")

        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def scale(self, k):
        # создаём новый прямоугольник, старый не трогаем
        # Для неизменяемых типов (immutable), например, строки, числа, кортежи
        return Rect(self.w * k, self.h * k)

    def rotate(self):
        # пошли по второму пути, immutable
        return Rect(self.h, self.w)

    def __str__(self):
        #return 'прямоугольник ' + str(self.w) + 'x' + str(selh.h)
        return f'Прямоугольник {self.w}x{self.h}'

    # пункт д)
    def __repr__(self):  # represent, представить в виде текста
        return f'Rect({self.w}, {self.h})'  # имеем право сделать любой текст, но есть общепринятый формат

r1 = Rect(10, 56)
print(r1.area())  # возвращает площадь
print(r1.perimeter())  # периметр

# Первый способ - меняем существующий прямоугольник
r1.scale(10)  # высота и ширина увеличиваются в 10 раз
print(r1.h, r1.w)

# Второй путь - создать новый
r2 = r1.scale(10)  # r1 останется прежним, но появится новый r2, и он уже будет большой
print(r1.h, r1.w)
print(r2.h, r2.w)


r1.scale(0.1)  # высота и ширина уменьшаются в 10 раз
r3 = r1.rotate()  # меняется ширина и высота местами

print(r3)

rectangles = [r1, r2, r3]
print(rectangles)