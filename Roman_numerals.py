class Roman(int):
    d = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    def __repr__(self):
        return f'Roman({super().__repr__()})'

    def __str__(self):
        tmp = int(self)

        if tmp == 0:
            return '0'

        res = ''
        for n in sorted(self.d.keys(), reverse=True):
            roman_letter = self.d[n]
            res += roman_letter * (tmp // n)
            tmp %= n
        return res

    @staticmethod
    def from_string(roman_value):
        roman_doubles = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
        roman_singles = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        if not set(roman_value) <= set('MDCLXVI'): # Множество букв строки должно быть подмножеством допустимых
            raise ValueError('В римском числе есть недопустимые символы')

        res = 0
        while len(roman_value) != 0:  # Если есть неправильные буквы в строке, цикл не закончится, поэтому лучше сделать проверку
            if roman_value[:2] in roman_doubles.keys():
                res += roman_doubles[roman_value[:2]]
                roman_value = roman_value[2:]  # убрали эти буквы
            else:
                res += roman_singles[roman_value[0]]
                roman_value = roman_value[1:]

        return Roman(res)

a = Roman(5)
b = a + 10
c = Roman(2022)
d = Roman(1954)  # M CM L IV
zero = Roman(0)  # разрешим
# e = Roman('LIX')  # 59
e = Roman.from_string('MCMLIX')
f = Roman.from_string('MMMMMMIV')
print(a, b, type(b), c, d, zero, e, f, int(f))
