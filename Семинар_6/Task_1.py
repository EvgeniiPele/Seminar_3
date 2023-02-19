# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input('Введите первый элемент: '))
difference = int(input('Введите разность: '))
quantity = int(input('Введите кол-во элементов: '))
result_list = [first_element]
for i in range(quantity - 1):
    result_list.append(result_list[i] + difference)
print(result_list)

