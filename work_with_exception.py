# Программа открывает файл и выдает сумму чисел, находящихся в нем
summa = 0
# with open("info.txt", "r", encoding="UTF-8") as f:
#     for line in f:
#         line = line.rstrip()
#     if line.isdigit() or line[0] == "-" and line[1:].isdigit():
#         summa += int(line)
#
with open("info.txt", "r", encoding="UTF-8") as f:
    for line in f:
        try:
            summa += int(line)
        except ValueError:
            pass

print(f"Сумма чисел равна = {summa}")
