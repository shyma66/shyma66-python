# print("4\n8\n15\n16\n23\n42")
# print("*\n**\n***\n****\n*****\n******\n*******")
#
#
# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!\n')
#
# name1 = 'Timur'
# name2 = 'Gvido'
# print(name1,name2)
# name1, name2 = name2, name1
# print(name1,name2)

# a = int(input())
# print(a)
# print(a + 1)
# print(a + 2)

# a = int(input())
# b = int(input())
# c = int(input())
# print(a + b + c)

# a = int(input())
# v = a ** 3
# print("Объем =", v)
# s = 6 * a**2
# print("Площадь полной поверхности =", s)

# a = int(input())
# b = int(input())
# c = 3 * (a + b)**3
# d = 275 * b**2 - 127 * a - 41
# print(c)
# print(d)
# print(c+ d)
# print(3 *(a + b)**3 + 257*b**2-127*a-41)

# print(20%5)
# a = int(input())
# b = int(input())
# d = b % a
# print(b // a)
# print(d)
# a = 5
# print((a -1) // 4 +1)

# a = int(input())
# b = a // 60
# c = a - (b*60)
# print(a ,f"мин - это {b} час {c} минут.")

# a = int(input())
# b = a % 10
# c = a // 10 % 10
# d = a // 100
# print(f"Сумма цифр = {b+c+d}")
# print(f"Произведение цифр = {b*c*d}")

# d = int(input())
# b = d % 10
# a = d // 10 % 10
# c = d // 100
# print(a,b,c)
# print(a,c,b)
# print(b,a,c)
# print(b,c,a)
# print(c,b,a)
# print(c,a,b)

# num = int(input())
# print(f"Цифра в позиции тысяч равна {num // 1000}")
# print(f"Цифра в позиции сотен равна {num // 100 % 10}")
# print(f"Цифра в позиции десятков равна {num // 10 %10}")
# print(f"Цифра в позиции единиц равна {num %10}")

# print(12345 % 10)

# print('Поэма "Мёртвые души" одна из самых интересных')

# print("*" * 17 )
# print("*" ," "* 13,"*")
# print("*" ," "* 13,"*")
# print("*" * 17 )

# print(int(input()) ** int(input())+int(input()) ** int(input()))
#
# a = input()
# print(int(a)+ int(a*2) + int(a*3))

# i = 4
# if i % 2 != 0:
#     print(i, 'нечётное')
# else:
#     print(i, 'чётное')
#
# a = int(input())
# if a % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# a = int(input())
# fourth = a % 10
# third = a // 10 % 10
# second = a // 100 % 10
# first = a // 1000 % 10
# if fourth + first == second - third:
#     print("ДА")
# else:
#     print("НЕТ")


# a = int(input())
# b = int(input())
# c = int(input())
# if b - a == c - b:
#     print("YES")
# else:
#     print("NO")

#
# a = 2
# b = 2
# c = 3
# d = 4
# if a < b :
#
#
# a = int(input())
# if a <= 13:
#     print("детство")
# elif 14 <= a <= 24:
#     print("молодость")
# elif 25 <= a <= 59:
#     print("зрелость")
# else:
#     print("старость")

# a = int(input())
# b = int(input())
# c = int(input())
# sum1 , sum2, sum3 = 0,0,0
# if a > 0:
#     sum1 = a
# if b > 0:
#     sum2 = b
# if c > 0:
#     sum3 = c
# print(sum1+sum2+sum3)
#
# print(True or False)
# print(False or True )
# print(81 % 9)
# a = int(input())
# if -1 <= a <= 17:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")
#
# a = int(input())
# if 1000 <= a <= 9999 and (a % 7 == 0 or a % 17 == 0):
#     print("YES")
# else:
#     print("NO")

# a = 2020
# if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
#     print("YES")
# else:
#     print("NO")

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 == x2 or y1 == y2:
#     print("YES")
# else:
#     print("NO")

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x2 - x1 == (1 or -1) or y2 - y1 == (1 or -1):
#     print("YES")
# else:
#     print("NO")

# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print("Равносторонний")
# elif a == b or a == c or b == c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# a = int(input())
# b = int(input())
# c = int(input())
# if a < b < c or c < b < a:
#     print(b)
# elif a < c < b or b < c < a:
#     print(c)
# elif b < a < c or c < a < b:
#     print(a)
# a = int(input())
# if a == 2:
#     print("28")
# elif a == (6 or 9 or 11 or 4):
#     print("30")
# elif  a == (1 or 3 or 5 or 7 or 8 or 10 or 12 ):
#     print("31")

# a = int(input())
# b = int(input())
# c = input()
# if c == "*":
#     print(a*b)
# elif c == "+":
#     print(a+b)
# elif c == "-":
#     print(a-b)
# elif c == "/":
#     if b == 0:
#         print("На ноль делить нельзя!")
#     else :
#         print(a/b)

# a = input()
# b = input()
# if a == "красный" and b =="синий" or a == "синий" and b =="красный" :
#     print("фиолетовый")
# elif a == "красный" and b == "красный":
#     print("красный")
# elif a == "красный" and b =="желтый" or a == "желтый" and b =="красный" :
#     print("оранжевый")
# elif a == "синий" and b =="желтый" or a == "желтый" and b =="синий" :
#     print("зеленый")
# elif a == "синий" and b =="желтый" or a == "желтый" and b =="синий" :
#     print("зеленый")
# elif a == "синий" and b == "синий":
#     print("синий")
# elif a == "желтый" and b == "желтый":
#     print("желтый")
# else:
#     print("ошибка цвета")
# while True:
#     a = int(input())
#     if 0 <= a <=36:
#         if 1 <= a <= 10:
#             if a % 2 == 0:
#                 print("черный")
#             else:
#                 print("красный")
#         elif 11 <= a <= 18:
#             if a % 2 == 0:
#                 print("красный")
#             else:
#                 print("черный")
#         elif 19 <= a <= 28:
#             if a % 2 == 0:
#                 print("черный")
#             else:
#                 print("красный")
#         elif 20 <= a <= 36:
#             if a % 2 == 0:
#                 print("красный")
#             else:
#                 print("черный")
#         elif a == 0:
#             print("зеленый")
#     else:
#         print("ошибка ввода")

# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
#
# # Находим максимум начал первого отрезка и минимум конца второго отрезка
# start_intersection = max(a1, a2)
# end_intersection = min(b1, b2)
#
# # Проверяем, есть ли пересечение
# if start_intersection <= end_intersection:
#     # Если начало пересечения равно концу пересечения, то это точка
#     if start_intersection == end_intersection:
#         print("Точка:", start_intersection)
#     else:
#         print("Отрезок:", start_intersection, "-", end_intersection)
# else:
#     print("Пустое множество")
