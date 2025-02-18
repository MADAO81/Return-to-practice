# Задание
# Даны два целых числа
# Выведите на экран все целые кратные 5 числа
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    a,b = b,a

while a<=b:
    if a % 5 == 0:
        print(a)
    a +=1

