# LAMBDA ФУНКЦИИ

# def f(x):
#     return x**2

# g = f

# print(f(2))
# print(g(3))
# print(type(f))
# print(type(g))

# def calc1(x):
#     return x + 10

# print(calc1(10))

# def calc2(x):
#     return x * 10

# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)

# def sum(x, y):
#     return x + y

# sum = lambda x, y: x + y + 1

# def mult(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)

# calc(lambda x, y: x+y+1, 4, 5)

# LIST COMPREHENSION

# list = []

# for i in  range(1, 101):
#     # if(i%2 == 0):
#     list.append(i)

# print(list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)

# АНОНИМНЫЕ, LAMBDA ФУНКЦИИ

# f = lambda x: x**2

# list = [(i, f(i)) for i in [1, 2, 3, 5, 8, 15, 23, 38] if i % 2 == 0]
# print(list)

# ЗАДАЧА
# Solution 1:

# path = '/Users/salnitta/Desktop/Examples/Python/LECTIONS/file_numbers.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos + 1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(out)

# Solution 2:

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x ** 2), res)
# print(res)

# Solution 3

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# Solution 4

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# FUNCTION MAP

# li = [x for x in range(1, 20)]
# li = list(map(lambda x: x + 10, li))
# print(li)

# data = list(map(int, input().split()))
# print(data)

# data = map(int, '1 2 77 56 902 33'.split())
# for e in data:
#     print(e*10)

# print('--')

# for e in data:      # данные выведутся на печать только один раз, т.к. map работает как итератор, 
#     print(e*10)     # чтобы их повторно использовать надо сохранить в список

# FUNCTION FILTER  # нельзя пройтись дважды

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x % 2, data))
# print(res)

# FUNCTION ZIP   # нельзя пройтись дважды # проходит по минимальному списку

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(zip(users, ids, salary))
# print(data)

# FUNCTION ENUMERATE

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# data = list(enumerate(users))
# print(data)







