# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной 
# и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

n = int(input("Введите количество монеток: n = "))
count0 = 0
count1 = 0
line = " "
for i in range(1, n+1):    
    picture = randint(0, 1)        # заполняется 0 и 1 (орел/решка)
    line += str(picture)
    if picture == 0:
        count0 += 1
    else:
        count1 += 1
print(line)
if count0 > count1:
    print(f"Необходимо перевернуть монет - {count1}")
    print(line.replace('1', '0'))
else:
    print(f"Необходимо перевернуть монет - {count0}")
    print(line.replace('0', '1'))