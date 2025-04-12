# самый базовый поиск
# Сложность O(n) если не повезёт, O(1) - если повезёт
def generic_search(iterable, target):
    for element in iterable:
        if element == target:
            return True
    return False

# Бинарный поиск
# Сложность O(log(n)), это лучше, чем O(n)
def binary_search(iterable, target):
    left = 0
    right = len(iterable) - 1

    while left <= right:
        mid = (right - left) // 2 + left  # индекс середины относительно начала исходного списка

        if iterable[mid] == target:  # если повезло
            return True  # либо вернуть его индекс (mid)

        elif iterable[mid] < target:
            left = mid + 1

        else:  # iterable[mid] > target
            right = mid - 1

    return False

def binary_search_closest(iterable, target):

    # Сложность O(1) - лучше, чем логарифмическая
    if target <= iterable[0]:
        return iterable[0], 0

    # Сложность O(1) - лучше, чем логарифмическая
    if target >= iterable[-1]:
        return iterable[-1], len(iterable) - 1

    left = 0
    right = len(iterable) - 1

    # Сложность логарифмическая
    # O(log(n))
    while left <= right:
        mid = (right - left) // 2 + left  # индекс середины относительно начала исходного списка

        if iterable[mid] == target:  # если повезло
            return iterable[mid], mid  # нашли точно это число

        elif iterable[mid] < target:
            left = mid + 1

        else:  # iterable[mid] > target
            right = mid - 1

    #return iterable[mid], mid  # не нашли точное число, но mid указывает на ближайшее
    if abs(iterable[mid] - target) > abs(iterable[mid - 1] - target) and mid != 0:
        res = iterable[mid - 1], mid - 1
    else:
        res = iterable[mid], mid

    return res