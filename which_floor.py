#Существует бесконечно высокий дом, в котором нумерация квартир начинается с единицы.
#Известен номер квартиры N. Определите на каком этаже находится данная квартира,
#если всего на этаже располагается по 12 квартир.
#Формат входных данных
#Дано целое положительное число
#Формат выходных данных
#Вывести целое число - номер этажа, на котором расположена квартира

import  math
apartment_number = int(input("Enter the apartment number: "))
apartment_on_floor = 12

# #Method 1
# floor_number = (apartment_number - 1) // apartment_on_floor + 1

#Method 2
floor_number = math.ceil(apartment_number/apartment_on_floor)

print("Your apartment is on the ", floor_number,"floor.")