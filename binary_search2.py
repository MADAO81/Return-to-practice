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


a = [12, 34, 45, 67, 87, 89, 123, 234, 504]  # сортированный

# Test driven development (TDD)
assert(binary_search_closest(a, 67) == (67, 3))
assert(binary_search_closest(a, 45) == (45, 2))
assert(binary_search_closest(a, 234) == (234, 7))
assert(binary_search_closest(a, 504) == (504, 8))
assert(binary_search_closest(a, 12) == (12, 0))

assert(binary_search_closest(a, 68) == (67, 3))
assert(binary_search_closest(a, 70) == (67, 3))
assert(binary_search_closest(a, 505) == (504, 8))
assert(binary_search_closest(a, 500) == (504, 8))
assert(binary_search_closest(a, 40) == (45, 2))
assert(binary_search_closest(a, 39) != (45, 2))
assert(binary_search_closest(a, 39) == (34, 1))
assert(binary_search_closest(a, 10) == (12, 0))
assert(binary_search_closest(a, 13) == (12, 0))

