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

        for k, v in params.items():
            if isinstance(v, tuple):
                # диапазон значений
                if not (v[0] <= getattr(self, k) <= v[1]):
                    return False

            elif isinstance(v, set):
                # что-то из указанного набора
                pass
            elif isinstance(v, (int, str, float)):
                # конекретное значение
                pass
            else:
                # что-то непонятное дали, выкинем исключение
                pass

            # все проверки прошли
            return True


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

print(car1.model, car1.fuel)
