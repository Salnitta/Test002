# ЗАДАЧА 1. Дана строка. Разделить строку на фрагменты по три подряд 
# идущих символа. В каждом фрагменте средний символ заменить
# на случайный символ, не совпадающий ни с одним из символов
# этого фрагмента. Показать фрагменты, упорядоченные по алфавиту (последнее не сделано)

# from string import ascii_letters
# import random

# string = 'This is the official documentation for Python 3.11.1. Parts of the documentation: Whats new in Python 3.11? or all "Whats new" documents since 2.0.'

# new_list = []

# while len(string) > 0:
#     element = string[:3]
#     while True:  # чтобы генерились элементы до тех пор, пока не найдется тот, что соответствует условию
#         letter = random.choice(ascii_letters)
#         if letter != element[0] and letter != element[2]:
#             new_element = element[0] + letter + element[2]
#             break
#     new_list.append(new_element)
#     string = string[3:]

# print(new_list)


# ЗАДАЧА 2. Дан текст, найдите наибольшее кол-во идущих подряд цифр

# count = 0
# max = 0

# string = 'This is the official documentat7777777ion for Python 3.11.1. Parts890890 of the docum90entation: Whats new in Python 3.1133? or all "Whats n67687ew" documents since 2.0.'

# for letter in string:
#     if letter.isdigit():
#         count += 1
#     else:
#         if count > max:
#             max = count
#         count = 0

# print(max)


# ЗАДАЧА 3. Даны две строки. Определите можно ли из некоторых символов 
# первой строки составить вторую строку

# string = 'Определите можно ли из некоторых символов первой строки составить вторую строку'
# new_string = 'собака'

# def histogram(string: str) -> dict:
#     histogram = {}
#     for letter in string.lower():
#         histogram[letter] = histogram.get(letter, 0) + 1
#     return histogram

# def comparison(main_string: str, sub_string: str) -> bool:
#     main = histogram(main_string)
#     sub = histogram(sub_string)
#     for letter in sub_string:
#         if sub.get(letter) > main.get(letter, 0):
#             print(f'В главной строке не хватает буквы "{letter}"')
#             return False
#     return True

# print(comparison(string, new_string))


# ЗАДАЧА 4. Дана строка. Придумать алгоритм шифрования данной строки и 
# дешифрования (не дорешали)


my_string = input('Введите строку для шифрования: ')

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
alphabet += alphabet.upper()

# Вариант 1:

special = '.,!"():; '

def shifter(string: str, shift: int) -> str:
    def swap_letters(letter):
        return alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
    return ''.join([swap_letters(letter)
                    if letter not in special else letter
                    for letter in string
                    ])

new_string = shifter(my_string, 3)
print(new_string)


# Вариант 2:

# def cipher(letter: str) -> str:
#     for i in range(len(alphabet)):
#         if alphabet[i] == letter:
#             if i < len(alphabet) - 3:
#                 return alphabet[i + 3]
#             else:
#                 return alphabet[i - len(alphabet) + 3] 

# def string_cipher(string: str) -> str:
#     new_string = ''
#     for letter in string:
#         if letter == ' ':
#             new_string += ' '
#         else:
#             new_string += cipher(letter)
#     return new_string

# new_string = string_cipher(my_string)
# print(new_string)















