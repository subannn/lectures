""" Строки """
# str()
# Строки - неизменяемый тип данных, упорядоченный тип данных
# Строки - неизменяемый, уrпорядоченный, индексируемый тип данных

# print(str1 + str2) # Конкотенация
# print((str2 + " ") * 4)d

""" Функции и методы строк """
# my_str = "Hello World"
# print(len(my_str))
# print(my_str.split('o')) # Делит по указательному делителю
# my_str = my_str.replace("l", "b")
# my_str = my_str.upper()
# my_str = my_str.lower()
# my_str = my_str.title()
# my_str = my_str.capitalize()
# my_str = my_str.casefold() # - эсцет
# my_str = my_str.count("l")
# print(my_str)

""" Индексы срезов """
# str5 = "Hello world"
# Индекс - порядковый номер символаа в строке (Начиная с 0)
# print(str5[-1])

# print(str5[0:5])

# print(str5[4:])
str5 = "Hello world"
# print(str5[::-2]) # str 5[start:stop:step]
# print(str5.find('ell')) # ищет строку и выдает индекс начала строки
# print(str5.index('W'))           
# print("*".join(['ell','as','fefew'])) # соеденяет переданный список строк по указанной строке
str8 = "        asdsda dasasd d ds    "
# print(str8.strip())
# str8.lstrip() # - Убирает слева
# str8.rstrip() # - Убирает справа
print(str5[-1])
x = "1234567890"
# print(f"asdasd {x} asdasd")
""" Методы проверки """
string_test = "My test string 123"
# print(string_test.isdigit())
# print(string_test.isalpha())
# print(string_test.isalnum())
# print(string_test.isspace())
# print(string_test.isupper())
# print(string_test.islower())
# print(string_test.endswith("123"))
# print(string_test.startswith("My"))

# num1 = 10
# num2 = 20
# print(num2 < num1)

# str1 = 'apple'
# str2 = 'hello'
# print(str1 == str2) # Сравнение по ASCII table
# ord('a') # 97
# chr(97) # "a"

""" Форматирование строк """

# stat_string = 'Привет, Фархад! Приглашаю тебя на праздние'
# name = input()
# place = input()
# str5 = 'Привет, %s! s' % name
# print(str5)
# str6 = 'Привет, {}! Приглашаю тебя на {}'.format(name,place)
# print(str6)
# str7 = f"Привет, {name}! Приглашаю тебя в {place}"
# print(str7)

# Форматирование строк = подстановка переменных в строку, создание динамической страны.

# a = 'I\'m student'
# b = "Ижет бычек качаться, \n\tВздыхает на ходу"
# print(b)                
# str8 = 'this is test string \n\r\n'
# print(str8)
# print(windows_path)
# dir(obj) # Показывает все методы которые можно использовать
# str1 = "hello"
# print(dir(str1))

num = int(input())
if chr(num).isalpha():
    print("Это буква " + str(chr(num)))
else:
    print("Это не буква, а символ " + str(chr(num)))


