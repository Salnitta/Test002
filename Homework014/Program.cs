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


// Решение через двумерный массив

int n = 50;
int[,] result = new int [n, n];
result[0, 0] = 1;
result[1, 0] = 2;

int count = 2;
int m = 0;
bool primeNum = false;

for (int i = 2; i < n; i++)
{
    primeNum = false;
    for (int k = 1; k < count; k++)
    {
        for (int j = 0; j < i - 1; j++)
        {
            if (result[k, j] == 0)
            {
                j--;
                break;
            }
            else if ((i + 1) % result[k, j] != 0) primeNum = true;
            else break;
            m = j + 1;
        }
        if(primeNum)
            {
                result[k, m] = i + 1;
                break;
            }  
    }   
    if (!primeNum)
    {
        result[count, 0] = i + 1;
        count++;
    }
}

for (int i = 0; i < count; i++)
{
    Console.Write($"Группа {i + 1}: ");
    for (int j = 0; j < result.GetLength(1); j++)
    {
        if (result[i, j] != 0) Console.Write(result[i, j] + " ");
    }
    Console.WriteLine();
}





// Решение через одномерные массивы

// void Fill (int[] array)
// {
//     for (int i = 0; i < array.Length; i++)
//     {
//         array[i] = i + 1;
//     }
// }

// void PrintExceptNull (int[] array)
// {
//     for (int i = 0; i < array.Length; i++)
//     {
//         if (array[i] != 0) Console.Write(array[i] + " ");
//     }
// }

// void CopyArray (int[] arrayFirst, int[] arraySecond)
// {
//     for (int i = 0; i < arrayFirst.Length; i++)
//     {
//         arrayFirst[i] = arraySecond[i];
//     }
// }



// int n = 50;
// int[] collection = new int[n];
// int[] result = new int[n];
// int[] newCollection = new int[n];
// int count = 1;
// int k = 0;
// int group = 1;
// bool primeNum = false;

// Fill(collection);

// for (int l = 0; l < group; l++)
// {
//     result[0] = collection[0];
//     for (int i = 1; i < collection.Length; i++)
//     {
//         primeNum = false;
//         for (int j = 0; j < count; j++)
//         {
//             if (result[j] == 0 || collection[i] % result[j] == 0) break;
//             else primeNum = true;
//         }
//         if(primeNum) 
//         {
//             result[count] = collection[i];
//             count++;
//         }
//         else
//         {
//             newCollection[k] = collection[i];
//             k++;
//         }
//     }

//     Console.Write($"Группа {group++}: ");
//     PrintExceptNull(result);
//     if (newCollection[0] == 0) break;
//     Console.WriteLine();
//     CopyArray(collection, newCollection);
//     Array.Clear(newCollection);
//     Array.Clear(result);
//     k = 0;
//     count = 1;
// }







