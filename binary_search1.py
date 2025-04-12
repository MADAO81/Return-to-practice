a = [12, 34, 45, 67, 87, 89, 123, 234, 504]  # сортированный


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

print(binary_search(a, 45))
print(binary_search(a, 89))
print(binary_search(a, 88))
print(binary_search(a, 35))
