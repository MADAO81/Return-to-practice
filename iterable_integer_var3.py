# Сделаем итератор через функцию с yield (функция-генератор)
def iterate_digits_1(number):
    digits = []
    while number != 0:
        digits.append(number % 10)
        number //= 10
    return digits

def iterate_digits_2(number):  # генератор
    while number != 0:
        digit = number % 10
        number //= 10
        yield digit  # Вместо return - именно внутри цикла

for d in iterate_digits_2(546876):
    print(d)

print(iterate_digits_1(59486739548679354867).__sizeof__())
print(iterate_digits_2(59486739548679354867).__sizeof__())


# ----------------

class IterableInt(int):
    def iterate_digits(self):  # служебный (приватный) метод
        number = abs(self)
        while number != 0:
            digit = number % 10
            number //= 10
            print('Работает функция-генератор')
            yield digit

    def __iter__(self):
        return self.iterate_digits()  # вернули функцию-генератор, у неё всё есть (__next__)



a = IterableInt(2136556)

print('Цикл')
for digit in a:
    print(digit)