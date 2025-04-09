# Вдохновляемся numpy.vectorize
def vectorize(f):
    def run(input_values):
        if not hasattr(input_values, '__iter__'):
            raise TypeError(f'Нужно передать что-то итерабельное, а не {type(input_values)}')

        # output_values = []
        # for input_value in input_values:
        #     output_values.append(f(input_value))
        #
        # return output_values

        # способ 2 - короче
        #return [f(input_value) for input_value in input_values]

        # Способ 3 - ещё короче
        return list(map(f, input_values))
    return run

def rounded(f):
    def run(value):  # часто такую функцию называют wrapper (обёртка)
        result = f(value)
        return round(result, 2)
    return run


# Применили два декоратора потому что имеем право
@vectorize
@rounded
def cm_to_inch(cm):
    return cm / 2.54


@vectorize
def kg_to_lb(kg):
    return kg * 2.20462


lengths_cm = [34, 56, 67, 43, 567, 87, 98, 34, 45]
lengths_kgs = [56, 76, 43, 22, 123, 156, 245, 86]
lengths_inch = cm_to_inch(lengths_cm)
#lengths_inch = vectorize(cm_to_inch)(lengths_cm)
print(lengths_inch)