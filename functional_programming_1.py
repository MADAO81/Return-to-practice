def is_even(x):
    return x % 2 == 0

a = [23, -65, 7, 87, -10, 4]

res = []
for ai in a:
    if is_even(ai):
        res.append(ai)
print(res)

res2 = [ai for ai in a if is_even(ai)]
print(res2)

res3 = filter(is_even, a)
print(list(res3))

res4 = filter(lambda x: x < 0, a)
print(list(res4))