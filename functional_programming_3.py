# эта функция будет декоратором
def rounded(f):
    def run(value):  # часто такую функцию называют wrapper (обёртка)
        result = f(value)
        return round(result, 2)
    return run


@rounded
def cm_to_inch(cm):
    return cm / 2.54


@rounded
def kg_to_lb(kg):
    return kg * 2.20462


print(cm_to_inch(100))
print(cm_to_inch(3.5))
print(kg_to_lb(100))
print(kg_to_lb(51.35))

# print(rounded(cm_to_inch)(100))
# print(cm_to_inch(3.5))
# print(rounded(kg_to_lb)(100))
# print(kg_to_lb(51.35))

lengths_cm = [34, 56, 67, 43, 567, 87, 98, 34, 45]
lengths_kgs = [56, 76, 43, 22, 123, 156, 245, 86]
lengths_inch = cm_to_inch(lengths_cm)