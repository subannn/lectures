""" Условные выражения """
# <
# >
# ==
# !=
# >=
# <=

# print(123 > 3)
# print(bool(0.124)) # true
# print(bool("")) # false
# print(bool(set[])) # false
# print(None) # false
""" if """

# num = 0
# if num > 3:
#     print("1241")
# else:
#     print("asd")

# temp = 543
# if temp < 20:
#     print("Холодно")
# elif temp < 30:
#     print("Тепло")
# elif temp < 35:
#     print("Жарко")
# else: 
#     print("Очень жарко")

# in - проверка на вхождение
# string = "Привет, как твои дела?"
# if "Привет" not in string:
#     print("Есть")
# else:
#     print("Нет")

# a = 10
# [выражение, действие 2][условие]
# print(['ok', 'not ok'][a > 10])

""" Тернарный оператор """
# a = ''
# msg = input('Введите сообщение ')
# if len(msg) > 10:
#     a = "Сообщение больше 10 исмволов"
# else:
#     a = "Сообщение меньше 10 символов"
# print(a)

# print("Сообщение больше 10 исмволов" if len(msg) > 10 else "Сообщение меньше 10 символов")

# colour = input("Col: ")
# match colour:
#     case 'red':
#         print("ok, red")
#     case 'white':
#         print("ok, white")
#     case 'blue':
#         print("ok, blue")
#     case 'balck':
#         print("ok, black")