# Напишите функцию, которая проверяет является ли число палиндромом

def palindrome_number(number):
    return str(number) == str(number)[::-1]

number = int(input("Enter the number: "))

if palindrome_number(number):
    print("This number is palindrome!")
else:
    print("This number is not palindrome!")