import threading
from multiprocessing.pool import ThreadPool

sigma = 0
sigma_lock = threading.Lock()
m = 10000000

def calculate_sigma(ns):
    global sigma  # чтобы иметь право писать в глобальную переменную
    tmp = 0
    for n in ns:
        tmp += (-1) ** (n + 1) / (2 * n - 1)

    sigma_lock.acquire()
    sigma += tmp
    sigma_lock.release()


pool = ThreadPool(4)

print('начинаем')
pool.map(calculate_sigma, [range(1, m+1, 4), range(2, m+1, 4), range(3, m+1, 4), range(4, m+1, 4)])
pool.close()
print('посчитали')
pi = 4 * sigma
print(pi)