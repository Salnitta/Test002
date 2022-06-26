

void PrintInt (int[,] array)
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


void PrintDouble (double[,] array)
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


// Задача 47: Задайте двумерный массив размером m×n,
// заполненный случайными вещественными числами.
// m = 3, n = 4. 
// 0,5 7 -2 -0,2 
// 1 -3,3 8 -9,9 
// 8 7,8 -7,1 9

int m = 3, n = 4;
double[,] mass = new double[m,n];

for (int i = 0; i < mass.GetLength(0); i++)
{
    for (int j = 0; j < mass.GetLength(1); j++)
    {
        mass[i,j] = new Random().Next(-10, 10) + new Random().NextDouble();
        mass[i,j] = Math.Round(mass[i,j], 1);
    }
}

PrintDouble(mass);

// Задача 50: Напишите программу, которая на вход 
// принимает позиции элемента в двумерном массиве, 
// и возвращает значение этого элемента или же указание, 
// что такого элемента нет.
// Например, задан массив: 
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 17 -> такого числа в массиве нет


// int m = 4, n = 4;
// int[,] mass = new int[m, n];

// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         mass[i, j] = new Random().Next(10, 100);
//     }
// }

// PrintInt(mass);

// Console.WriteLine("Введите позиции элемента массива:");

// Console.Write("index1 = ");
// int index1 = int.Parse(Console.ReadLine());

// Console.Write("index2 = ");
// int index2 = int.Parse(Console.ReadLine());

// if (index1 < 0 || index1 > mass.GetLength(0) 
//     || index2 < 0 || index2 > mass.GetLength(1))
//     {
//         Console.WriteLine("Такого элемента не существует");
//     }
// else Console.WriteLine($"Искомое число: {mass[index1, index2]}");


// Задача 52: Задайте двумерный массив из целых чисел. 
// Найдите среднее арифметическое элементов в каждом столбце.
// Например, задан массив: 
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.

// int m = 4, n = 4;
// int[,] mass = new int[m, n];

// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         mass[i, j] = new Random().Next(0, 10);
//     }
// }

// PrintInt(mass);
// Console.WriteLine("Среднее арифметическое каждого столбца:");
// AverageColumns(mass);