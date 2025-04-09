a = [45, 7, -7, 5, -98, 71, -100]

print(sorted(a))
print(sorted(a, reverse=True))
print(sorted(a, key=abs))  # также есть в min(), max()

b = ['Ростов', 'Москва', 'Нижний Новгород', 'Астрахань', 'Яхрома']
print(sorted(b))
print(sorted(b, key=len))
