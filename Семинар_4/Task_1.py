# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Введите длину первого множества: '))
m = int(input('Введите длину воторого множества: '))
first_list = []
second_list = []
for i in range(n):
    num = int(input(f' Введите {i + 1} элемент первого массива: '))
    first_list.append(num)
for j in range(m):
    num = int(input(f' Введите {j + 1} элемент второго массива: '))
    second_list.append(num)
print(first_list)
print(second_list)
first_list = set(first_list)
second_list = set(second_list)
finaly_list = list(first_list.intersection(second_list))
print(sorted(finaly_list))