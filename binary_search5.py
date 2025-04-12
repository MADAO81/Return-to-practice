from math import e
#from matplotlib import pyplot as plt
import timeit


def vectorize(f):
    def run(input_values):
        # способ 2 - короче
        return [f(input_value) for input_value in input_values]
    return run

@vectorize
def sigmoid_precise(z):
    return 1 / (1 + e ** (-z))


def diff(y1, y2):
    # res = [abs(y2i - y1i) for y1i, y2i in zip(y1, y2)]
    res = []
    for y1i, y2i in zip(y1, y2):
        res.append(abs(y2i - y1i))
    return res

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

        if iterable[mid] > target:
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

        y = ((x-x1) * (y2 - y1) / (x2 - x1)) + y1
        return y

xs = [xi / 10 for xi in range (-90, 92, 2)]  # -9, 9 с шагом 0.2
print(xs)

ys1 = sigmoid_precise(xs)
ys2 = vectorize(Sigmoid.calculate)(xs)
print(diff(ys2, ys1))

# plt.plot(xs, ys1)
# plt.plot(xs, ys2, marker='.')
# plt.show()