# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

import commands as com


path_in = 'HOMEWORKS/Homework005/RLE/input_data.txt'
path_out = 'HOMEWORKS/Homework005/RLE/output_data.txt'

while True:
      try:
        command = int(input('Нажмите 0 для сжатия данных или 1 для восстановления данных: '))
        if command not in {0, 1}:
            print('Введите 0 или 1')
        elif command:
            print(f'Восстановленные данные: {com.expansion(path_out, path_in)}')
            break
        else:
            print(f'Сжатые данные: {com.compression(path_in, path_out)}')
            break
      except ValueError:
           print('Введите цифру')        
 