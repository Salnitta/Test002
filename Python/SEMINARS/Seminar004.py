# Теоретическая часть

# my_string = '\tПитон самый лучший в мире язык\n'
# new_string = my_string.split() # делит строку по указанному символу, по умолчанию пробел, на выходе получаем уже не строку, а список
# print(my_string)
# print(new_string)
# new_string = my_string.replace('и', '$').replace('п', '!!!') # заменяет символы
# print(new_string)
# new_string = my_string.strip() # убирает табуляции и лишние пробелы в начале и конце
# new_string = my_string.lstrip() # чистит слева
# new_string = my_string.rstrip() # чистит справа
# if my_string.lower().startswith('пит'): # проверка, с чего начинается # lower переводит в нижний регистр
#     print('Да, все верно')
# if my_string.endswith('зык'): # проверка, на что заканчивается
#     print('Да, все верно') 
# print(my_string.upper()) # upper переводит в верхний регистр

# my_list = ['23', 'gh', '655', '788']
# add = '-ss'
# print(add.join(my_list)) # склеивает список строк через выбранный символ
# print(' '.join(my_list))

# my_dict = {32:'23', 1:'Один', 3:45, 'Ключ': 2132323, 'Список': [12, 34, 56, 343]}
# print(my_dict(1))
# print(my_dict.get(2, 'Нет такого ключа'))
# print(my_dict.get(3, 0))
# print(my_dict.get(2, 0) + my_dict(3, 0))
# my_dict['New'] = 'value'
# print(my_dict)
# my_dict['32'] = 'value' # если такой ключ уже есть, значение перезаписывается
# my_dict[3] = my_dict.get(3) + 1 # увеличили значение на 1

# Задача

# my_dict = {}

# num_list = '23565654663847875898397662534254324556'
# for dig in num_list:
#     my_dict[dig] = my_dict.get(dig, 0) + 1
# print(my_dict)

# Задача 2

#'A*x**2 + B*x + C = 0'

# '32*x**2 + 4*x + 6 = 0'
# my_string = 'A*x**2 + B*x + C = 0'
# def conv(my_string):
#     new_string = my_string.split('x')
#     print(new_string)
#     new_string2 = []
#     for i in range(len(new_string)):
#         new_string2.append(new_string[i].replace('**2', '').replace('*', '').replace('+', '').replace('=', '').replace('0', '').replace(' ', ''))
#     return new_string2


# string_a = '-3*x**2 + 78*x -9=0'
# str_res = conv(string_a)
# for i in range(3):
#     str_res[i] = int(str_res[i])
# print(str_res)
# x = (-str_res[i])

equation = '-3*x**2 + 78*x -9=0'

def create_koef(equation: str) -> tuple:
    new_coef = []
    nq = equation.replace(' ', '').replace('=0', '').\
        replace('+', ' ').replace('-', ' -').split()
    for item in nq:
        new_coef.append(int(item.split('*x')[0]))
    return new_coef

    



