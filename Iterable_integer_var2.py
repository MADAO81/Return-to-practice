class IterableInt(int):
    def __len__(self):
        if self == 0:
            return 1

        # O(n), где n - длина числа
        tmp = abs(self)  # заодно возьмём модуль
        res = 0
        while tmp != 0:
            res += 1
            tmp //= 10
        return res

    def __contains__(self, search_digit):
        # O(n), но зависит от удачи
        # В лучшем случае O(1), в худшем O(n)
        tmp = abs(self)
        while tmp != 0:
            digit = tmp % 10  # последняя цифра (младший разряд)
            if digit == search_digit:
                return True
            tmp //= 10
        # если мы здесь, то цифры такой нет
        return False

    def __getitem__(self, position):
        # O(n + p)
        # n - количество цифр в числе
        # if len(self) <= position:
        #     raise IndexError("...")

        # Сложность O(p)
        # p - position, если оно не больше длины числа. p = n, если больше
        # Не самый хороший способ
        n = 0
        tmp = abs(self)
        while tmp != 0:
            if position == n:
                return tmp % 10
            n += 1
            tmp //= 10
            print('работает getitem')

        # Если мы находимся здесь, такого разряда нет
        raise IndexError('Такого разряда нет')

        # O(1)
        # Способ получше
        # tmp = abs(self)
        # digit = (tmp // (10 ** position)) % 10
        # return digit

    def __iter__(self):
        return IterableIntIterator(self)


class IterableIntIterator:
    def __init__(self, value):
        self.value = value  # value - значение целого числа
        # self.iszero == (value == 0)

    def __next__(self):
        if self.value == 0:
            raise StopIteration  # Не ошибка, а сообщение циклу for

        digit = self.value % 10
        self.value //= 10
        print('работает итератор')
        return digit


a = IterableInt(2136556)

print(len(a))
print(len(IterableInt(0)))
print(len(IterableInt(2)))
print(len(IterableInt(-456)))
print(0 in a)
print(5 in a)
print(a[0])
print(a[5])
print(a[6])
#print(a[7])
#print(a[-1])
# # a[3] = 6  # не будем делать
# #

# Без iter, через getitem сложность будет
# O(n**2) (или n**2 / 2)
print('Цикл')
for digit in a:
    print(digit)