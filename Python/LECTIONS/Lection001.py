# print('hello мир')

# типы данных и переменные
# int, float, boolean, str, list, None

value = None
# print(type(value))
a = 123
b = 1.23
# print (type(a))
# print (type(b))
value = 12344

# s = 'hello \nworld' # перенос на новую строку с помощью оператора \n

# print (s) # вывод строки

# s = 'hello world'
# print (a, '-' ,b, '-',s)
# print ('{} - {} - {}'.format(a, b, s)) # формитирование 1 вариант
# print (f'{a} - {b} - {s}') # форматирование 2 вариант
# print ('{1} - {2} - {0}'.format(a, b, s)) # форматирование, смена порядка

# f = False
# print(f)

# list = ['1', '2', '3']
# col = ['hello', 1, 2, 3, 4.5, True ] # нежелательно задавать в списках разные типы данных
# print(list)
# print(col)

# print('Введите а')
# a = int(input()) # если не задаем типизацию, то по умолчанию идет работа со строками
# print('Введите b')
# b = float(input())
# print(a, ' + ', b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметические операции 
# +, -, *, /, %, //, **
# **, , , *, /, //, %, +, -
# / - деление вещественных чисел
# // - целочисленное деление
# ** - возведение в степень
# * - при умножении вещественных чисел есть особенность, связанная с их хранением, необходимо округление
# (), Сокращенные операции
# a = 1.31232676
# b = 3
# c = round(a * b, 5)
# print(c)

# a = 3
# a += 5 # сокращенная операция присваивания, работает также для других операторов
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 1 < 3 < 5 # можно использовать тройные и четверные неравенства
# Print(a)

# f = 1 > 2 or 4 < 6
# Print(f) # результат True (дизъюнкция)

# f = [1, 2, 3, 4]

# print(f)
# print(2 in f) # проверяем, что в списке есть 2
# print(not 2 in f) # проверяем, что в списке нет 2

# is_odd = f[0] % 2 == 0 # проверяем четность
# is_odd = not f[1] % 2 # проверяем четность вариант 2
# print(is_odd)

# Управляющие конструкции
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)


# Управляющие конструкции
# for

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i**2)

# r = range(10) # перечисление от 0 до 9
# for i in r:
#     print(i)

# for i in range(1, 10, 2): # перечислание диапазона от и до с интервалом приращения
#     print(i)

# for i in 'qwe - rty':
#     print(i)

# text = 'съешь еще этих мягких французских булок'

# text.                           # вывод подсказок
# help(text.istitle)              # вывод справки по функции text.istitle, выход по клавише q
# print(len(text))                # 39 - количество символов в строке
# print('еще' in text)            # True - проверка, есть ли подстрока в строке
# print(text.isdigit())           # False - проверка, являются ли все символы в строке числами
# print(text.islower())           # True - проверка, являются ли все символы в строке символами нижнего регистра
# print(text.replace('еще', 'ЕЩЕ'))   # замена одной подстроки на другую

# API для работы со строками (срезы)

# for c in text:
#     print(с)

# text = 'съешь еще этих мягких французских булок'
# print(text[0])                    # c
# print(text[1])                    # ъ
# print(text[len(text)])            # IndexError
# print(text[len(text) - 1])        # к
# print(text[-5])                   # б
# print(text[:])                    # print(text)
# print(text[:2])                   # съ
# print(text[len(text)-2:])         # ок
# print(text[2:9])                  # ешь еще
# print(text[6:-18])                # еще этих мягких
# print(text[0:len(text):6])        # сеикакл
# print(text[::6])                  # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# СПИСКИ

# numbers = [1, 2, 3, 4, 5]
# print(numbers)                      # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(numbers)                      # [1, 2, 3, 4, 5]
# print(type(numbers))

# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)                      # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)                        # [20, 4, 6, 8, 10]
# print(numbers)                      # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)                          # red green blue

# for e in colors:
#     print(e*2)                        # redred greengreen blueblue

# colors.append('gray')                 # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red')                  # удалить элемент
# del colors[0]                         # удалить элемент


# ФУНКЦИИ

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 1
# print(f(arg))
# print(type(f(arg)))

