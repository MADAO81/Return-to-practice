# юнит тесты
# unittest, pytest, google test - библиотеки

import algorithms

assert(algorithms.generic_search([12, 23, 45], 45) == True)
assert(algorithms.generic_search([12, 23, 45], 12) == True)
assert(algorithms.generic_search([12, 23, 45], 365) == False)
assert(algorithms.generic_search([1], 365) == False)
assert(algorithms.generic_search([1, 56, 87, 87, 65], 65) == True)
assert(algorithms.generic_search([], 365) == False)