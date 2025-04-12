class Sigmoid:
    ys = [0.00033535013046647827, 0.002472623156634775, 0.017986209962091562, 0.11920292202211757, 0.5, 0.8807970779778823,
          0.9820137900379085, 0.9975273768433653, 0.9996646498695336]
    xs = [-8, -6, -4, -2, 0, 2, 4, 6, 8]

    @staticmethod
    def binary_search_two_closest(iterable, target):

        if len(iterable) == 0:
            raise IndexError('Пустой список')

        # Сложность O(1) - лучше, чем логарифмическая
        if target <= iterable[0]:
            return 0, 0

        # Сложность O(1) - лучше, чем логарифмическая
        if target >= iterable[-1]:
            return len(iterable) - 1, len(iterable) - 1

        left = 0
        right = len(iterable) - 1

        # Сложность логарифмическая
        # O(log(n))
        while left <= right:
            mid = (right - left) // 2 + left  # индекс середины относительно начала исходного списка

            if iterable[mid] == target:  # если повезло
                return mid, mid  # нашли точно это число

            elif iterable[mid] < target:
                left = mid + 1

            else:  # iterable[mid] > target
                right = mid - 1

        if mid != 0:
            res = mid - 1, mid
        else:
            res = mid, mid + 1

        return res

    @classmethod
    def calculate(cls, x):
        left, right = cls.binary_search_two_closest(cls.xs, x)

        if left == right:
            return cls.ys[left]

        x1 = cls.xs[left]
        x2 = cls.xs[right]
        y1 = cls.ys[left]
        y2 = cls.ys[right]

        y = (x-x1) * (y2 - y1) / (x2 - x1) + y1
        return y

print(Sigmoid.calculate(0))
print(Sigmoid.calculate(0.2))
print(Sigmoid.calculate(1.5))
print(Sigmoid.calculate(2.1))

#a = [12, 34, 45, 67, 87, 89, 123, 234, 504]  # сортированный

# print(binary_search_two_closest(a, 20))
# assert(binary_search_two_closest(a, 12) == (0, 0))
# assert(binary_search_two_closest(a, 10) == (0, 0))
# assert(binary_search_two_closest(a, 504) == (8, 8))
# assert(binary_search_two_closest(a, 999) == (8, 8))
#
# assert(binary_search_two_closest(a, 45) == (2, 2))
# assert(binary_search_two_closest(a, 123) == (6, 6))

# assert(binary_search_two_closest(a, 46) == (2, 3))
# assert(binary_search_two_closest(a, 66) == (2, 3))
# assert(binary_search_two_closest(a, 88) == (4, 5))
# assert(binary_search_two_closest(a, 20) == (0, 1))
# assert(binary_search_two_closest(a, 35) == (1, 2))

