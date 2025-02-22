# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

fruits = ["яблоко", "бананья", "киви", "ананас", "груша", "манго", "папайя"]

max_len = 0
for fruit in fruits:
    if len(fruit) > max_len:
        max_len = len(fruit)

for num, fruit in enumerate(fruits,1):
    print(f"{num} {fruit:>{max_len}}")