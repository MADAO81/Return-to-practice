from multiprocessing import Pool

m = 50000000

def calculate_sigma(ns):
    global sigma  # чтобы иметь право писать в глобальную переменную
    tmp = 0
    for n in ns:
        tmp += (-1) ** (n + 1) / (2 * n - 1)

    return tmp


if __name__ == '__main__':  # без такой конструкции Pool не запустится
    pool = Pool(4)  # не больше, чем логических ядер

    print('начинаем')
    res = pool.map(calculate_sigma, [range(1, m+1, 4), range(2, m+1, 4), range(3, m+1, 4), range(4, m+1, 4)])
    pool.close()
    print('посчитали')
    print(sum(res) * 4)