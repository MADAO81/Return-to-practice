class SuperList(list):

    def __init__(self, elements=None):

        # что-то делаем проприетарное
        print('конструктор супер листа')

        # сделали всё своё, теперь вызовем конструктор родителя
        # чтобы он доделал инициализацию
        if elements is None:
            super().__init__()
        else:
            super().__init__(elements)  # вызовется одноименный метод list'a

    def __add__(self, other):
        if not isinstance(other, list):  # на самом деле хотим проверить, является ли other итерабельным (iterable)
        # одиночный элемент, который прибавляем ко всем своим элементам
            res = SuperList()  # либо, если хотим обобщить для будущих производных классов self.__class__()
            for element in self:
                res.append(element + other)
            return res

        # В противном случае
        # значит что other - другой список
        if len(self) != len(other):
            raise IndexError('Списки должны быть одинаковой длины!')

        res = SuperList()
        for ai, bi in zip(self, other):
            res.append(ai + bi)
        return res

    # умножение, сравнение - аналогично

a = SuperList()
a.append(87)
a.append(45)
a.append(54)

b = SuperList(range(3, 15))

print(a, b, type(b))
print(a + 3)
print(a + [56, 67, 76])