class CarFieldError(Exception):
    pass  # создали свой тип исключения


class Car:
    valid_fields = {
        "kmage",
        "model",
        "generation",
        "price",
        "year",
        "transmission",
        "body",
        "drive",
        "color",
        "volume",
        "power",
        "fuel"}

    def __init__(self, data):
        if not isinstance(data, dict):
            TypeError('В конструктор нужно передать словарь с данными')

        # заполняем поля, способ 1 - скучный, но понятный
        # self.kmage = data['kmage'] либо data.get('kmage')
        # self.model = data['mode']
        # ...

        # Способ 2 - хитрый
        # лучше проверить валидность ключей (пусть будет список допустимых ключей)
        for key in data:
            if key not in self.valid_fields:
                raise CarFieldError(f'Параметр не поддерживается: {key}')
            setattr(self, key, data[key])

        missing_keys = self.valid_fields - set(data.keys())
        for key in missing_keys:
            setattr(self, key, None)

    def matches(self, params):
        if not isinstance(params, dict):
            raise TypeError

        # надо проверить, что все ключи - допустимые
        if not set(params.keys()) <= self.valid_fields:
            raise CarFieldError(f'Недопустимые поля в фильтре: {set(params.keys()) - self.valid_fields}')

        for k, v in params.items():
            if isinstance(v, tuple):
                # диапазон значений
                if not (v[0] <= getattr(self, k) <= v[1]):
                    return False

            elif isinstance(v, set):
                # что-то из указанного набора
                if getattr(self, k) not in v:
                    return False

            elif isinstance(v, (int, str, float)):
                # конкретное значение
                # если это float, то лучше проверить через math.isclose()
                if getattr(self, k) != v:
                    return False

            else:
                # что-то непонятное дали, выкинем исключение
                raise TypeError(f'Значение параметра {k} имеет неподдерживаемый тип данных')

            # все проверки прошли
            return True

    def __repr__(self):
        res = 'Car({'
        for param in self.valid_fields:
            res += repr(param) + ': ' + repr(getattr(self, param)) + ', '
        res += '})'
        return res

car1_data = {
            "kmage": 25000,
            "model": "Porsche 911",
            "generation": "VII (991) Рестайлинг Turbo S",
            "price": 11200000,
            "year": 2016,
            "transmission": "робот",
            "body": "купе",
            "color": "золотистый",
            "volume": 3.8,
            "power": 580
        }

car1 = Car(car1_data)
print(car1)

print(car1.model, car1.fuel)

# Численные значения
print(car1.matches({'year': 2005}))  # точно указанный год
print(car1.matches({'year': (2005, 2010)}))  # кортеж - диапазон лет, пусть начало и конец включается

# Нечисленные значения
print(car1.matches({'color': 'золотистый'}))  # точно указанный цвет
print(car1.matches({'color': {'красный', 'бордовый', 'малиновый'}}))  # множество - машина должна быть одного из этих цветов

# Несколько критериев - машина должна удовлетворять всем, чтобы вернуть True
print(car1.matches({'year': (2005, 2010), 'color': {'красный', 'бордовый', 'малиновый'}, 'transmission': 'автомат'}))

# print(car1.matches({'doors': 4, 'color': {'красный', 'бордовый', 'малиновый'}, 'transmission': 'автомат'}))