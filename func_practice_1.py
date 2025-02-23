# Функция, которая определяет четное или нечетное число
def even_or_not(number):
    return number % 2 == 0  # если число четное возвращается "TRUE", если нет - "FALSE"


number = int(input("Enter the number: "))

if even_or_not(number):
    print("Your number is even!")
else:
    print("Your number is odd!")
