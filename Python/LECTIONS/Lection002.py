
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.write('\nLINE 12\n')
# data.write('LINE 13\n')
# data.close()  # обязательно закрыть файл, иначе потеря памяти и ошибки при работе с файлом

# with open('file.txt', 'a') as data:      # альтернативный вариант записи в файл, после которого не нужна команда close()
#     data.write('line 1\n')
#     data.write('line 2\n')


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()  # команда, которая останавливает выполнение кода, расположенного после нее


# ФУНКЦИИ

# Работа с функциями из других файлов
# import Lection001 as l

# print(l.f(1))


# def new_string(symbol, count = 3): # в count указано значение по умолчанию
#     return symbol * count

# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))     # !!!
# print(new_string(4))       # 12


# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1', 'd', '2'))  # a1d2
# print(concatenatio(1, 2, 3, 4))        # TypeError: ...


# РЕКУРСИЯ

# def fib(n):
#     if n in (1, 2):
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34


# КОРТЕЖИ - неизменяемый списки

# a, b = 3, 4 # множественное присваивание
# a = (3, 4, 5)  # кортеж
# a = (3,)  # если один элемент, нужна запятая, иначе будет ошибка
# print(a)
# print(a[0])

# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue']) # создаем список
# red, green, blue = t # конвертируем список в кортеж
# print('r:{} g:{} b:{}'.format(red, green, blue)) # распаковываем кортеж и работает с ним как с отдельными переменными
# r:red g:green b:blue


# СЛОВАРИ


# МНОЖЕСТВА

