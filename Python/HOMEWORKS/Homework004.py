# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

import random

def create_polynom(coef: int) -> str:
    polynom_str = ''
    for i in range(coef, -1, -1):
        r = random.randint(-100, 100)
        if r != 0:
            polynom_str += str(f' + {r}*x**{i}')
    return polynom_str

def format_polynom(polynom_str: str):
    polynom_str = polynom_str + ' = 0'
    polynom_str = polynom_str.replace('x**1 ', 'x ').replace('*x**0', '')\
        .replace(' 1*x', ' x').replace(' -1*x', ' -x')
    polynom_str = polynom_str[3:]
    polynom_str = polynom_str.replace('+ -', '- ')
    return polynom_str

def reformat_polynom(polynom_str: str):
    polynom_str = polynom_str.replace('- ', '+ -').replace('-x', '-1*x')\
        .replace(' x', ' 1*x').replace('*x ', '*x**1 ')
    if polynom_str[0] == 'x':
        polynom_str = '1*' + polynom_str
    return polynom_str
    
def create_coef_dict(polynom_str: list) -> dict:
    polynom_dict = {}
    polynom_str = polynom_str[:-4].split(' + ')
    for item in polynom_str:
        d = item.split('*x**')
        if len(d) > 1:
            polynom_dict[int(d[1])] = int(d[0])
        else:
            polynom_dict[0] = int(d[0])
    return polynom_dict

def dictionaries_sum(dict_1: dict, dict_2: dict) -> dict:
    result_dict = {}
    result_keys = set()
    for key in dict_1:
        result_keys.add(key)
    for key in dict_2:
        result_keys.add(key)
    for i in result_keys:
        result_dict[i] = dict_1.get(i, 0) + dict_2.get(i, 0)
        if result_dict[i] == 0:
            result_dict.pop(i)  
    return result_dict

def recreate_polynom(given_dict: dict) -> str:
    polynom_str = ''
    for key, value in given_dict.items():
        polynom_str = str(f' + {value}*x**{key}') + polynom_str
    return polynom_str

k = int(input('Введите натуральную степень k: '))
polynom_A = format_polynom(create_polynom(k))
with open('file_A.txt', 'w') as data:
    data.write(polynom_A)
print(f'Первое уравнение:\n{polynom_A}')

l = int(input('Введите натуральную степень l: '))
polynom_B = format_polynom(create_polynom(l))
with open('file_B.txt', 'w') as data:
    data.write(polynom_B)
print(f'Второе уравнение:\n{polynom_B}')

with open('file_A.txt', 'r') as data:
    polynom_file_A = data.read()
coef_A = create_coef_dict(reformat_polynom(polynom_file_A))

with open('file_B.txt', 'r') as data:
    polynom_file_B = data.read()
coef_B = create_coef_dict(reformat_polynom(polynom_file_B))

final_coef = dictionaries_sum(coef_A, coef_B)
result_polynom = format_polynom(recreate_polynom(final_coef))
with open('file_result.txt', 'w') as data:
    data.write(result_polynom)
print(f'Сумма уравнений:\n{result_polynom}')

