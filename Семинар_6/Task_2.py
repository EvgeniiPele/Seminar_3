# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
res = []
for i in range(15):
    res.append(randint(1, 100))
print(res)
max_value = int(input('Введите максимальное значение: '))
min_value = int(input('Введите минимальное значение: '))
for i in res:
    if min_value <= i <= max_value:
        print(i)