
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


# КОРТЕЖИ - неизменяемый списки (нельзя присвоить элементу другое значение)

# a, b = 3, 4 # множественное присваивание
# a = (3, 4, 5)  # кортеж
# print(a) # (3, 4, 5)
# print(a[0]) # 3
# print(a[-2]) # 4
# a = (3,)  # если один элемент, нужна запятая, иначе будет ошибка

# for item in a:
#     print(item)

# t = tuple(['red', 'green', 'blue']) # создаем список
# print(t[0]) # red
# print(t[2]) # blue
# print(t[-2]) # green
# for e in t:
#     print(e) # red green blue
# t[0] = black # TypeError: 'tuple' j,ject does not support item assignment

# red, green, blue = t # конвертируем список в кортеж # двойное преобразование для работы с элементами списка как с отдельными переменными
# print('r:{} g:{} b:{}'.format(red, green, blue)) # распаковываем кортеж 
# r:red g:green b:blue

# СЛОВАРИ - неупорядоченные коллеции произвольных объектов с доступом по ключу

# dictionary = {}
# dictionary = \
#     {
#         'right': '->',
    #     'left': '<-'
    # }
# print(dictionary) # {'right': '->', 'left': '<-'}
# print(dictionary['left']) # <-
# типы ключей могут отличаться

# for k in dictionary.keys():
#     print(k)                  # right left

# for k in dictionary.values():
#     print(k)                  # -> <-

# for k in dictionary:
#     print(dictionary[k])      # -> <- 

# print(dictionary['left'])     # <- 
# dictionary['left'] = 'влево'
# print(dictionary['left'])     # влево

# МНОЖЕСТВА - уникальные элементы (неупорядоченные)

# colors = {'red', 'green', 'blue'}

# print(colors)                   # {'red', 'green', 'blue'}
# print(type(colors))             # set

# colors.add('red')               # если элемент уже есть, он не добавится
# print(colors)                   # {'red', 'green', 'blue'}
# colors.add('gray')             
# print(colors)                   # {'red', 'green', 'blue', 'gray}
# colors.remove('red')            # удаление элемента
# print(colors)                   # {'green', 'blue', 'gray}
# colors.remove('red')            # при удалении несуществующего элемента будет ошибка KeyError: 'red'
# colors.discard('red')           # удаление элемента, если его нет, то ничего не произвойдет, ошибок не будет
# colors.clear()                  # очистить множество 
# print(colors)                   # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()                    # c = {1, 2, 3, 5, 8}
# u = a.union(b)                  # u = (1, 2, 3, 5, 8, 13, 21)
# i = a.intersection(b)           # i = {8, 2, 5}
# dl = a.difference(b)            # dl = {1,3}
# dr = b.difference(a)            # dr = {13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))  # {1, 21, 3, 13}

# s = frozenset(a)                # замороженное неизменяемое множество

# # СПИСКИ

# list1 = [1, 2, 3, 4, 5]
# list2 = list1                    # ТАК ДЕЛАТЬ НЕЖЕЛАТЕЛЬНО, любые дальнейшие изменения будут производиться в одновременно в обоих списках

# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)

# list1[0] = 123
# list2[1] = 333
# print()

# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)

# print(len(list1))  
# print(list1.pop())   # извлечение / удаление последнего эелемента из списка
# print(list1)         # [1, 2, 3, 4]
# print(list1.pop())   # 4
# print(list1)         # [1, 2, 3]
# print(list1.pop(1))  # 3 # удаление элемента с определенным индексом
# print(list1)         # [1, 3]

# print(list1.insert(2, 11))  # добавление элемента 11 на место с индексом 2
# print(list1)         # [1, 3, 11]

# print(list1.append(120))    # добавление эелемнта 120 в конец
# print(list1)

