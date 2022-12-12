# ЗАДАЧА 2: Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for i in range(2):
    X = i
    for j in range(2):
        Y = j
        for k in range(2):
            Z = k
            bool1 = not (X or Y or Z)
            bool2 = (not X) and (not Y) and (not Z)
            result = bool1 == bool2
            print(f'{X, Y, Z} - {result}')