# Бегун проводил ежедневные тренировки и записывал расстояния которые пробегал за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
# Переведите все значения в футы (получить и вывести новый список)
distances_in_fut = []
# Вариант 1
for el in distances:
    new_el = el * 3.28
    distances_in_fut.append(new_el)
print(distances_in_fut)


# Вариант 2
def meter_in_foot(meter):
    return meter * 3.28


distance_foot = list(map(meter_in_foot, distances))
print(distance_foot)
