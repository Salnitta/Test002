// Задача 46: Задайте двумерный массив размером m×n,
// заполненный случайными целыми числами.
// m = 3, n = 4. 1 4 8 19
// 5 -2 33 -2 77 3 8 1

// void Print(int[,] arr)
// {
//     for (int i = 0; i < arr.GetLength(0); i++)
//     {
//         for (int j = 0; j < arr.GetLength(1); j++)
//         {
//             Console.Write(arr[i, j] + " ");
//         }
//         Console.WriteLine();
//     }
// }

// int m = 3, n = 4;
// int[,] mass = new int[m, n];

// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         mass[i, j] = new Random().Next(-100, 100);
//     }
// }

// Print(mass);

// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         mass[i, j] = mass[i, j] - 100;
//     }
// }

// Print(mass);

// void Print (int[,] array)
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

// int m = 3, n = 4;
// int[,] mass = new int[m,n];

// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         mass[i,j] = new Random().Next(-100, 100);
//     }
//     Console.WriteLine();
// }

// Print(mass);

// Задача 48: Задайте двумерный массив размера 
// m на n, каждый элемент в массиве находится 
// по формуле: Aₙₙ = m+n. Выведите полученный массив на экран.
// m = 3, n = 4. 
// 0 1 2 3
// 1 2 3 4
// 2 3 4 5 

// int m = 3, n = 4;
// int[,] mass = new int[m,n];

// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         mass[i,j] = i + j;
//     }
// }

// Print(mass);

// Задача 49: Задайте двумерный массив. Найдите элементы, у
// которых оба индекса чётные, и замените эти элементы на их
// квадраты
// 

// int m = 3, n = 4;
// int[,] mass = new int[m,n];

// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         mass[i,j] = new Random().Next(1, 10);
//     }
// }

// Print(mass);
// Console.WriteLine();


// for (int i = 0; i < mass.GetLength(0); i += 2)
// {
//     for (int j = 0; j < mass.GetLength(1); j += 2)
//     { 
//         mass[i,j] = mass[i,j] * mass[i,j];
//     }
// }

// Print(mass);

// Задача 51: Задайте двумерный массив. 
// Найдите сумму элементов, находящихся на 
// главной диагонали (с индексами (0,0); (1;1) и т.д.

// int m = 3, n = 4;
// int[,] mass = new int[m,n];

// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         mass[i,j] = new Random().Next(1, 10);
//     }
// }

// Print(mass);
// Console.WriteLine();

// int sum = 0;

// for (int i = 0; i < Math.Min (mass.GetLength(0), mass.GetLength(1)); i++)
// {
//     sum += mass[i,i];
// }

// Console.WriteLine($"Сумма элементов главной диагонали: {sum}");

// Задача 47: Задайте двумерный массив размером m×n,
// заполненный случайными вещественными числами.
// m = 3, n = 4. 
// 0,5 7 -2 -0,2 
// 1 -3,3 8 -9,9 
// 8 7,8 -7,1 9

// void Print (double[,] array)
// {
//     for (int i = 0; i < array.GetLength(0); i++)
//     {
//         for (int j = 0; j < array.GetLength(1); j++)
//         {
//             Console.Write(array[i, j] + " ");
//         }
//         Console.WriteLine();
//     }
// }

// int m = 3, n = 4;
// double[,] mass = new double[m,n];

// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         mass[i,j] = new Random().Next(-10, 10) + new Random().NextDouble();
//         mass[i,j] = Math.Round(mass[i,j], 1);
//     }
// }

// Print(mass);

// Задача 50: Напишите программу, которая на вход 
// принимает позиции элемента в двумерном массиве, 
// и возвращает значение этого элемента или же указание, 
// что такого элемента нет.
// Например, задан массив: 
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 17 -> такого числа в массиве нет

// void Print(int[,] array)
// {
//     for (int i = 0; i < array.GetLength(0); i++)
//     {
//         for (int j = 0; j < array.GetLength(1); j++)
//         {
//             Console.Write(array[i, j] + " ");
//         }
//         Console.WriteLine();
//     }
// }


// int m = 4, n = 4;
// int[,] mass = new int[m, n];

// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         mass[i, j] = new Random().Next(10, 100);
//     }
// }

// Print(mass);

// Console.WriteLine("Введите позиции элемента массива:");

// Console.Write("index1 = ");
// int index1 = int.Parse(Console.ReadLine());

// Console.Write("index2 = ");
// int index2 = int.Parse(Console.ReadLine());

// if (index1 < 0 || index1 > mass.GetLength(0) 
//     || index2 < 0 || index2 > mass.GetLength(1))

//     Console.WriteLine("Такого элемента не существует");

// else Console.WriteLine($"Искомое число: {mass[index1, index2]}");


// Задача 52: Задайте двумерный массив из целых чисел. 
// Найдите среднее арифметическое элементов в каждом столбце.
// Например, задан массив: 
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.


void Print(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write(array[i, j] + " ");
        }
        Console.WriteLine();
    }
}

void AverageColumns(int[,] array)
{
    double sum = 0;
    double avg = 1;

    for (int j = 0; j < array.GetLength(1); j++)
    {
        sum = 0; 
        for (int i = 0; i < array.GetLength(0); i++)
        {
            sum += array[i,j];
        }
        avg = sum / array.GetLength(0);
        Console.Write(avg + "; ");
    }
}


int m = 5, n = 4;
int[,] mass = new int[m, n];

for (int i = 0; i < mass.GetLength(0); i++)
{
    for (int j = 0; j < mass.GetLength(1); j++)
    {
        mass[i, j] = new Random().Next(0, 10);
    }
}

Print(mass);
Console.WriteLine("Среднее арифметическое каждого столбца:");
AverageColumns(mass);


