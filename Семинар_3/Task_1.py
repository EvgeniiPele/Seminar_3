from random import random, randint

length = int(input('Введите длину списка: '))
number = int(input('Введите искомое число: '))
my_list = []
for i in range(length):
    my_list.append(randint(1, 100))
print(my_list)
found = my_list[i]
if my_list.count(number) == 0:
    for i in range(length):
        if abs(my_list[i] - number) < abs(my_list[0] - number):
            found = my_list[i]
    print(f'такого числа в списке нет, максимально близкое число к вашему - {found}')
else:
    print(f'Число {number} встречается {my_list.count(number)} раз(а)')