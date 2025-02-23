# Напишите функцию, которая возвращает максимальное число из введенных

def my_max_number(*args):  # *args - означает все переданные аргументы и они упаковываются в кортеж
    max_el = args[0]  # первый элемент для сравнения берем из перечня введенных чисел.
    for el in args:
        if el > max_el:
            max_el = el
    return max_el


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
number4 = int(input("Enter the fourth number: "))

max_num = my_max_number(number1, number2, number3, number4)
print("Max number is: ", max_num)
