# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите трехзначное число: "))
summa = 0
if number > 99 and number < 1000:
    while number > 0:
        summa += number % 10
        number = number//10
    print(f"Сумма цифр в числе равна {summa}")
else:
    input("Ввели не трехзначное число. Повторите ввод.")