//  Задача 54: Задайте двумерный массив. 
// Напишите программу, которая упорядочит 
// по убыванию элементы каждой строки двумерного массива.

// void PrintArray (int[,] array)
// {
//     for (int i = 0; i < array.GetLength(0); i++)
//     {
//         for (int j = 0; j < array.GetLength(1); j++)
//         {
//             // Console.Write(i + " " + j + ", ");
//             Console.Write(array[i, j] + " ");
//         }
//         Console.WriteLine();
//     }
// }

void FillArray (int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i,j] = new Random().Next(0, 10);
        }
    }
}

void SortArrayString (int[,] array)
{
    int max = 0;
    int help = 0;
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = j + 1; k < array.GetLength(1); k++)
            {
                max = array[i,j];
                if (array[i,k] > max) 
                {
                    help = array[i,j];
                    array[i,j] = array[i,k];
                    array[i,k] = help;
                }
            }
        }
    }
}

// int a = 3, b = 7;
// int[,] mass = new int[a,b];
// FillArray(mass);
// PrintArray(mass);
// Console.WriteLine();
// SortArrayString(mass);
// PrintArray(mass);


// Задача 56: Задайте прямоугольный двумерный массив. 
// Напишите программу, которая будет находить строку 
// с наименьшей суммой элементов.


// int a = 6, b = 4;
// int[,] mass = new int[a,b];
// FillArray(mass);
// PrintArray(mass);
// Console.WriteLine();

// int[] arr = new int[mass.GetLength(0)];
// int sum = 0;
// for (int i = 0; i < mass.GetLength(0); i++)
//     {
//         sum = 0;
//         for (int j = 0; j < mass.GetLength(1); j++)
//         {
//             sum += mass[i,j];
//         }
//         arr[i] = sum;
//         Console.WriteLine($"Сумма элементов строки с индексом {i} = {sum}");
//     }


// int posMin = 0;
// for (int i = 1; i < arr.Length; i++)
// {
//     if (arr[i] < arr[posMin]) 
//     {
//         posMin = i;
//     }
// }

// Console.WriteLine();
// Console.WriteLine($"Индекс строки с наименьшей суммой элементов: {posMin}");

// // Альтернативный вариант решения:

// int minSum = 0;
// int posMin = 0;
// for (int j = 0; j < mass.GetLength(1); j++)
// {
//     minSum += mass[posMin,j];
// }
// Console.WriteLine($"Сумма элементов строки с индексом {posMin} = {minSum}");


// int sum = 0;
// for (int i = 1; i < mass.GetLength(0); i++)
//     {
//         sum = 0;
//         for (int j = 0; j < mass.GetLength(1); j++)
//         {
//             sum += mass[i,j];
//         }
//         Console.WriteLine($"Сумма элементов строки с индексом {i} = {sum}");

//         if (sum < minSum)
//         {
//             minSum = sum;
//             posMin = i;
//         }
//     }

// Console.WriteLine($"Индекс строки с наименьшей суммой элементов: {posMin}");

// * Задача 58: Задайте две матрицы. Напишите программу, 
// которая будет находить произведение двух матриц.

// int a = 3, b = 3;
// int[,] matrix1 = new int[a,b];
// FillArray(matrix1);
// Console.WriteLine("Первая матрица:");
// PrintArray(matrix1);
// Console.WriteLine();

// int c = 3, d = 2;
// int[,] matrix2 = new int[c,d];
// FillArray(matrix2);
// Console.WriteLine("Вторая матрица:");
// PrintArray(matrix2);
// Console.WriteLine();

// if (matrix1.GetLength(1) == matrix2.GetLength(0))
// {
//     int[,] result = new int[matrix1.GetLength(0), matrix2.GetLength(1)];
//     int multiple = 1;
//     int sum = 0;
//     for (int i = 0; i < matrix1.GetLength(0); i++)
//     {
//         for (int k = 0; k < matrix2.GetLength(1); k++)
//         {
//             sum = 0;
//             for (int j = 0; j < matrix1.GetLength(1); j++)
//             {
//                 multiple = matrix1[i,j] * matrix2[j,k];
//                 // Console.WriteLine($"{matrix1[i,j]} * {matrix2[j,k]} = {multiple}");
//                 sum += multiple;
//             }
//             // Console.WriteLine(sum);
//             result[i,k] = sum;
//         } 
//     }
//     Console.WriteLine("Произведение матриц:");
//     PrintArray(result);
// }
// else Console.WriteLine("Матрицы нельзя перемножить");


// Задача 60: Сформируйте трёхмерный массив из 
// неповторяющихся двузначных чисел. Напишите программу, 
// которая будет построчно выводить массив, добавляя 
// индексы каждого элемента.

// int a = 4, b = 2, c = 3;
// int[,,] mass = new int[a,b,c];
// for (int i = 0; i < mass.GetLength(0); i++)
//     {
//         for (int j = 0; j < mass.GetLength(1); j++)
//         {
//             for (int k = 0; k < mass.GetLength(2); k++)
//             {
//                 mass[i,j,k] = new Random().Next(10, 100);
//                 Console.Write($"{mass[i,j,k]} ({i},{j},{k}) ");
//             }
//         }
//         Console.WriteLine();
//     }


// bool Contains(int[,,] array, int find)
// {
//     for (int i = 0; i < array.GetLength(0); i++)
//     {
//         for (int j = 0; j < array.GetLength(1); j++)
//         {
//             for (int k = 0; k < array.GetLength(2); k++)
//             {
//                 if (array[i,j,k] == find) return true;
//             }
//         }
//     }
//     return false;
// }

// int a = 3, b = 2, c = 2;
// int[,,] mass = new int[a,b,c];
// int rnd = 0;
// for (int i = 0; i < mass.GetLength(0); i++)
//     {
//         for (int j = 0; j < mass.GetLength(1); j++)
//         {
//             for (int k = 0; k < mass.GetLength(2); k++)
//             {
//                 rnd = new Random().Next(10, 22);
//                 if (!Contains(mass, rnd))
//                 {
//                     mass[i,j,k] = rnd;
//                     Console.Write($"{mass[i,j,k]} ({i},{j},{k}) ");
//                 }
//                 else k--;
//             }
//         }
//         Console.WriteLine();
//     }

// * Задача 62: Заполните спирально массив 4 на 4.

void PrintArray (int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            if (array[i,j] < 10) Console.Write($"0{array[i,j]} ");
            else Console.Write(array[i, j] + " ");
        }
        Console.WriteLine();
    }
}

int n = 4;
int m = 4;
        
int str = n - 1;
int col = m - 1;
int help = 0;
        
int i = 0;
int j = 0;

int num = 1;

int [,] mass = new int [n,m];
                
while (num < n * m) // узкое место - не получается в цикле поставить <=, т.к. при нечетных m и n возникает ошибка переполнения
{ 
    for (; j < col; j++) 
    {
        mass[i,j] = num;
        num++;            
    }
        
    for (; i < str; i++)
    {
        mass[i,j] = num;
        num++;
    }
            
    for (; j > help; j--) 
    {
        mass[i,j] = num;
        num++;      
    }

    for (; i > help; i--) 
    {
        mass[i,j] = num;
        num++;              
    }   

    str --;
    col --;
    help ++; 
    j ++;
    i ++;    
}

if (n * m % 2 == 1 && num == n * m) // условие, позволяющее обойти узкое место, указанное выше
    {
        mass[i,j] = num;
        num++; 
    }

Console.WriteLine();
PrintArray(mass);

// * Задача 61: Вывести первые N строк треугольника Паскаля. 
// Сделать вывод в виде равнобедренного треугольника