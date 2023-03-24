#  Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих 
#   строках записаны N целых чисел Ai. Последняя строка содержит число X
#  *Пример:*
#      5
#      1 2 3 4 5
#      6
#      -> 5

from random import randint
import math

n = int(input("Введите количество элементов в массиве: n = "))
list_1 = list()
for i in range(n):
    list_1.append(randint(1, 100))
print(list_1)
x = int(input("Введите число: x = "))
difference_1 = abs(x - list_1[0])
index = 0
for i in range(len(list_1)):
    difference_2 = abs(x - list_1[i])
    if difference_2 < difference_1:
        difference_1 = difference_2
        index = i
print(f"Значение {list_1[index]} самое близкое по величине к заданному числу {x}")
