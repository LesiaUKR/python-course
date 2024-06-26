from copy import copy, deepcopy

# copy - це модуль, який містить функції для копіювання об'єктів
# copy - не підходить, якщо є вкладеність [1,3 [a,b,c]] -
# воно скопіює тільки зовнішній список [1,3], а внутрішній [a,b,c] - посилання
# copy - використовується, якщо потрібно зробити поверхневу копію і зекономити пам'ять
l = [1, 3, ['a', 'b', 'c']]
# l2 = copy(l)
# l2[2][0] = 'x'  # змінить і в l
# print(l)

# deepcopy - копіює всі об'єкти, включаючи вкладені
l2 = deepcopy(l)
l2[2][0] = 'x'  # не змінить l
print(l2)  # [1, 3, ['x', 'b', 'c']]
print(l)  # [1, 3, ['a', 'b', 'c']]

# на практиці використовується deepcopy
