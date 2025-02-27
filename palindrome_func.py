# Найдите количество чисел-палиндромов в заданном промежутке

def palindrome(number):
    return str(number) == str(number)[::-1]  # возвращает True или False


a = 10
b = 40
if a > b:
    a, b = b, a
num_palindromes = 0  # счетчик палиндромов
while a <= b:
    if palindrome(a):
        num_palindromes += 1
    a += 1
print(num_palindromes)

# Var.2
a = 10
b = 40
if a > b:
    a, b = b, a
for number in range(a, b + 1):
    if palindrome(number):
        num_palindromes += 1
print(num_palindromes)
