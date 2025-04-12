from algorithms import binary_search_closest  # наша функция поиска

class Sigmoid:
    ys = [0.00033535013046647827, 0.002472623156634775, 0.017986209962091562, 0.11920292202211757, 0.5, 0.8807970779778823,
          0.9820137900379085, 0.9975273768433653, 0.9996646498695336]
    xs = [-8, -6, -4, -2, 0, 2, 4, 6, 8]

    @classmethod
    def calculate(cls, x):
        value, index = binary_search_closest(cls.xs, x)
        return cls.ys[index]


print(Sigmoid.calculate(0))
print(Sigmoid.calculate(0.2))
print(Sigmoid.calculate(1.5))
print(Sigmoid.calculate(2.1))