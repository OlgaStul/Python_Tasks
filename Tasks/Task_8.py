# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите количество долек шоколадки в длину: n = "))
m = int(input("Введите количество долек шоколадки в ширину: m = "))
k = int(input("Введите количество долек, которых нужно отломить: k = "))
if k < n or k < m:
    print(f"Шоколадку размером {n}x{m} долек можно разломить на {k} части(ей)")
else:
    print(f"Шоколадку размером {n}x{m} долек нельзя разломить на {k} части(ей)")