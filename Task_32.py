# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

from random import randint

def filling(arg):
    list_result = list()
    for i in range(arg):
        list_result.append(randint(-10, 10))
    return list_result

def selection(arg1, arg2, arg3):
    list_2 = list()
    for i in range(len(arg1)):
        if arg1[i] > arg2 and arg1[i] < arg3:
            list_2.append(i)
    return list_2
     

n = int(input("Введите количество элементов первого массива: n = "))
n_min = int(input("Задайте минимум: min = "))
n_max = int(input("Задайте максимум: max = "))
list_1 = filling(n)

print(list_1)
print(f'{selection(list_1, n_min, n_max)} - индексы элементов, которые больше {n_min} и меньше {n_max}')

