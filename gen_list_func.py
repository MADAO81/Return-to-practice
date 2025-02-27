import random
def gen_list(size, at=-10, to=10):
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(at,to))
    return result_list