// Задача 73: Есть число N. Сколько групп M, можно получить 
// при разбиении всех чисел на группы, так чтобы в одной группе 
// все числа были взаимно просты (все числа в группе друг на друга 
// не делятся)? Найдите M при заданном N и получите одно из разбиений
// на группы N ≤ 1020.
// Например, для N = 50, M получается 6
// Группа 1: 1
// Группа 2: 2 3 11 13 17 19 23 29 31 37 41 43 47
// Группа 3: 4 6 9 10 14 15 21 22 25 26 33 34 35 38 39 46 49 
// Группа 4: 8 12 18 20 27 28 30 42 44 45 50
// Группа 5: 7 16 24 36 40
// Группа 6: 5 32 48

int n = 50;
int[,] b = new int [n, n];
b[0, 0] = 1;
b[1, 0] = 2;

int count = 2;
int m = 0;
bool exist = false;

for (int i = 2; i < n; i++)
{
    exist = false;
    for (int k = 1; k < count; k++)
    {
        for (int j = 0; j < i - 1; j++)
        {
            if (b[k, j] == 0)
            {
                j--;
                break;
            }
            else if ((i + 1) % b[k, j] != 0) exist = true;
            else 
            {
                exist = false;
                break;
            }
            m = j + 1;
        }
        if(exist)
            {
                b[k, m] = i + 1;
                break;
            }  
    }   
    if (!exist)
    {
        b[count, 0] = i + 1;
        count++;
    }
}

for (int i = 0; i < count; i++)
{
    Console.Write($"Группа {i + 1}: ");
    for (int j = 0; j < b.GetLength(1); j++)
    {
        if (b[i, j] != 0) Console.Write(b[i, j] + " ");
    }
    Console.WriteLine();
}








