# Создать класс прямоугольник:
#
# а) при создании указывается ширина и длина
#
# r1 = Rect(10, 56)
# б) методы для площади и периметра
#
# print(r1.area())  # возвращает площадь
# print(r1.perimeter())  # периметр
# в) масштабирование и поворот
#
# r1.scale(10) - высота и ширина увеличиваются в 10 раз
# r1.scale(0.1) - высота и ширина уменьшаются в 10 раз
# r1.rotate() - меняется ширина и высота местами

class Rect:
    def __init__(self,width, height ):
        if width <= 0 or height <= 0:
            raise ValueError("Размеры фигуры должны быть положительными.")


        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 *(self.width + self.height)


    def scale(self,koef):
        # Создаем новый прямоугольник, старый не трогаем
        return  Rect(self.width * koef, self.height * koef)
        # модифицируем self, имеющуюся фигуру
        # self.height *= koef
        # self.width *= koef

    def rotate(self):
        return Rect(self.height, self.width) # Меняем высоту и ширину местами, тем самым вращаем прямоугольник


r1 = Rect(10,56)
print(r1.area())
print(r1.perimeter())

# Первый способ - меняем существующий прямоугольник
r1.scale(10)  # высота и ширина увеличиваются в 10 раз
print(r1.height, r1.width)

# Второй способ - создать новый прямоугольник
r2 = r1.scale(10) # r1 останется прежним, но появится r2 большего размера

r1.scale(0.1)  # высота и ширина уменьшаются в 10 раз
r3 = r1.rotate()  # меняется ширина и высота местами

print(r3.height, r3.width)