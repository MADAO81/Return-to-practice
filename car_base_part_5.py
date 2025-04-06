import json
from car import Car, CarFieldError

f = open(r"auto.json",
         'r',
         encoding='utf8')
text = f.read()
#print(text)
data = json.loads(text)

class Selection:
    def __init__(self, elements):
        self.cars = []

        #if not isinstance(elements, (list, set)):
        if not hasattr(elements, '__iter__'):
            raise TypeError('Дай мне список машин')

        for element in elements:
            if isinstance(element, Car):
                self.cars.append(element)
            elif isinstance(element, dict):
                try:
                    self.cars.append(Car(element))
                except CarFieldError:
                    print('Ошибка в данных о машине: ', element)
            else:
                raise TypeError('Нужен список машин или словарей с данными о машинах')

    def __len__(self):
        return len(self.cars)

    def filter(self, criteria: dict):

        # способ 1
        # result = []
        # for car in self.cars:
        #     if car.matches(criteria):
        #         result.append(car)

        # Способ 2
        # то же, что в способе 1, но в одну строку
        #result = [car for car in self.cars if car.matches(criteria)]

        # Способ 3
        result = filter(lambda car: car.matches(criteria), self.cars)

        return Selection(result)

    def sort_by(self, param):
        #result = sorted(self.cars, key=lambda car: getattr(car, param))  # читаем напрямую атрибут чужого класса
        result = sorted(self.cars, key=lambda car: car.get_value(param))  # читаем результат публичного метода, так можно
        return Selection(result)

    def __repr__(self):
        return repr(self.cars)


database = Selection(data['data'])

print(len(database))

sel = database.filter({'year': (2005, 2010), 'color': {'красный', 'бордовый', 'малиновый'}, 'transmission': 'автомат'})
#sel = database.filter(year=(2005, 2010), color={'красный', 'бордовый', 'малиновый'}, transmission='автомат')
print(sel)

print(sel.sort_by('price'))