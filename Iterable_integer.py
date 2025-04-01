class IterableInt(int):
    def __len__(self):
        return len(str(self))

    def __contains__(self, digit):
        if digit not in {0,1,2,3,4,5,6,7,8,9}:
            raise ValueError('В оператор in нужно передавать цифру')

        return str(digit) in str(self)

    def __getitem__(self, item):
        return str(self)[::-1][item]

    def __iter__(self):
        return str(self).__iter__()  # символы, а не цифры
        # map(int, str(self)).__iter__() - теперь цифры

a = IterableInt(2136556)

print(len(a))
print(0 in a)
print(5 in a)
print(a[0])
print(a[5])
print(a[-1])
# a[3] = 6  # не будем делать
#
for digit in a:
    print(digit)