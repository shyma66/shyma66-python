# 5
# a = int(input())
# if a % 10 == 0 and a // 10 % 10 == 0:
#     print("YES")
# else:
#     print("NO")
# doska
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# # sum = x1 + x2 + y1 + y2
# # if  sum % 2 == 0:
# #     print("YES")
# # else:
# #     print("NO")
# slon
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if  x1 - y1 == x2 - y2:
#     print("YES")
# elif x1 + y1 == x2 + y2:
#     print("YES")
# else:
#     print("NO")
# ferz
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if  x1 - y1 == x2 - y2:
#     print("YES")
# elif x1 + y1 == x2 + y2:
#     print("YES")
# elif x1 == x2 or y1 == y2:
#     print("YES")
# else:
#     print("NO")
# konb

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# sum = x1 + x2 + y1 +y2
# if sum % 2 == 1 and x1 != x2 and y1 != y2:
#     print("YES")
# else:
#     print("NO")

# a = int(input())
# b = input()
# if 10 <= a <= 15 and b == "f":
#     print("YES")
# else:
#     print("NO")

# a = int(input())
# if 1 <= a <= 10:
#     if a == "1":
#         print("I")
#     elif a == "2":
#         print("II")
#     elif a == "3":
#             print("III")
#     elif a == "4":
#             print("IV")
#     elif a == "5":
#             print("V")
#     elif a == "6":
#             print("VI")
#     elif a == "7":
#             print("VII")
#     elif a == "8":
#             print("VIII")
#     elif a == "9":
#             print("IX")
#     elif a == "10":
#             print("X")
# else:
#     print("ошибка")

# a = int(input())
# num = {
#     1 : "I",
#     2 : "II",
#     3 : "III",
#     4 : "IV",
#     5 : "V",
#     6 : "VI",
#     7 : "VII",
#     8 : "VIII",
#     9 : "IX",
#     10 : "X"
# }
# if 0 <= a <= 10:
#     print(num[a])
# else:
#     print("ошибка")

# a = int(input())
# if a % 2 == 1:
#     print("YES")
# elif 2 <= a <= 5 and a % 2 == 0:
#     print("NO")
# elif 6 <= a <= 20 and a % 2 == 0:
#     print("YES")
# elif a > 20 and a % 2 == 0:
#     print("NO")



#6

# a = float(input())
# b = float(input())
# print(0.5 * a * b)

# a = float(input())
# b = float(input())
# c = float(input())
# print(a / (c + b))

# a = float(input())
# if a != 0:
#     print(1 / a)
# else:
#     print("Обратного числа не существует")

# a = float(input())
# print(5/9 *(a -32))

# a = float(input())
# if a <= 2:
#     print(a * 10.5)
# else:
#     print((a-2) * 4 + 21)

# a = float(input())
# print(int((a * 10) % 10 //1))

# number = float(input("Введите число: "))
# decimal_part = str(number).split(".")[1]
#
# print("Десятичная часть числа:", decimal_part)

# a = float(input())
# print(a - int(a))

# a , b , c = int(input()) , int(input()) , int(input())
# ma = max(a,b,c)
# mi = min(a,b,c)
# sred = a + b + c - mi - ma
# print(ma)
# print(sred)
# print(mi)

# num = int(input())
# a = num // 100
# b = (num % 100) // 10
# c = num % 10
# sred = a + b+ c - max(a,b,c) - min(a,b,c)
# if max(a,b,c) - min(a,b,c) == sred:
#     print("Число интересное")
# else:
#     print("Число неинтересное")


print(abs(10.31-23))