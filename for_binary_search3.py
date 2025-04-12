import math
from math import e
from matplotlib import pyplot as plt  # нужно установить pip install matplotlib

def vectorize(f):
    def run(input_values):
        # способ 2 - короче
        return [f(input_value) for input_value in input_values]
    return run

@vectorize
def sigmoid1(z):
    return 1 / (1 + e ** (-z))

#assert(sigmoid1(0) == 0.5)
#zs = [-344, -34, -56, 0, -5, 10, 100, 9999, 6454]
zs = range(-8, 10, 2)
ys = sigmoid1(zs)
print(ys)
print(list(zs))

plt.plot(zs, ys)
plt.show()

assert(math.isclose(sigmoid2(0.1), 0.5, abs_tol=0.000001))
assert(math.isclose(sigmoid2(2.1), 0.8807970779778823, abs_tol=0.000001))