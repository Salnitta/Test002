// Задача 31: Задайте массив из 12 элементов, 
// заполненный случайными числами из промежутка [-9, 9]. 
// Найдите сумму отрицательных и положительных элементов массива.
// Например, в массиве [3,9,-8,1,0,-7,2,-1,8,-3,-1,6] 
// сумма положительных чисел равна 29, сумма отрицательных равна -20.

// void FillArray (int[] arr)
// {
//     for (int i = 0; i < arr.Length; i++)
//     {
//         arr[i] = new Random ().Next(-9, 10);
//     }
// }

// void PrintArray (int[] array)
// {
//     for (int i = 0; i < array.Length; i++)
//     {
//         Console.Write(array[i] + " ");
//     }
// }

// int[] mass = new int [12];
// FillArray(mass);
// PrintArray(mass);
// Console.WriteLine();

// int sumPos = 0;
// int sumNeg = 0;

// for (int i = 0; i < mass.Length; i++)
// {
//     if (mass[i] > 0)
//     {
//         sumPos += mass[i];
//     }
//     else
//     {
//         sumNeg += mass[i];
//     }
// }
// Console.WriteLine("Positive: " + sumPos);
// Console.WriteLine("Negative: " + sumNeg);


// Задача 32: Напишите программу замены 
// элементов массива: положительные элементы 
// замените на соответствующие отрицательные, 
// и наоборот.
// [-4, -8, 8, 2] -> [4, 8, -8, -2]

// void Fill(int[] arr)
// {
//     for (int i = 0; i < arr.Length; i++)
//     {
//         arr[i] = new Random().Next(-9, 10);
//     }
// }

// void Print(int[] array)
// {
//     for (int i = 0; i < array.Length; i++)
//     {
//         Console.Write(array[i] + " ");
//     }
//     Console.WriteLine();
// }

// int[] mass = new int[4];
// Fill(mass);
// Print(mass);

// for (int i = 0; i < mass.Length; i++)
// {
//     mass[i] = -mass[i];
// }

// // альтернативное решение:

// // for (int i = 0; i < mass.Length; i++)
// // {
// //     mass[i] *= -1;
// // }

// Print(mass);


// Задача 33: Задайте массив. Напишите программу, 
// которая определяет, присутствует ли заданное число в массиве.
// 4; массив [6, 7, 19, 345, 3] -> нет -3; массив [6, 7, 19, 345, 3] -> да

// void Fill(int[] arr)
// {
//     for (int i = 0; i < arr.Length; i++)
//     {
//         arr[i] = new Random().Next(-9, 10);
//     }
// }

// void Print(int[] array)
// {
//     for (int i = 0; i < array.Length; i++)
//     {
//         Console.Write(array[i] + " ");
//     }
//     Console.WriteLine();
// }

// bool IndexOf(int[] col, int find)
// {
//     bool Exist = false;
//     for (int i = 0; i < col.Length; i++)
//     {
//         if (Math.Abs(col[i]) == Math.Abs(find))
//         {
//             Exist = true;
//             break;
//         }
//     }
//     return Exist;
// }

// int[] mass = new int[8];
// Fill(mass);
// Print(mass);
// Console.WriteLine("Please, enter integer:");
// int num = int.Parse(Console.ReadLine());
// bool result = IndexOf(mass, num);

// if (result == false) Console.WriteLine("no");
// else Console.WriteLine("yes");


// Задача 35: Задайте одномерный массив 
// из 123 случайных чисел.
// Найдите количество элементов массива, 
// значения которых лежат в отрезке [10,99].
// Пример для массива из 5, а не 123 элементов. 
// В своём решении сделайте для 123
// [5, 18, 123, 6, 2] -> 1
// [1, 2, 3, 6, 2] -> 0
// [10, 11, 12, 13, 14] -> 5

// void Fill(int [] arr)
// {
//     for (int i = 0; i < arr.Length; i++)
//     {
//         arr[i] = new Random().Next (-99, 100);
//     }
// }

// void Print(int[] array)
// {
//     for (int i = 0; i < array.Length; i++)
//     {
//         Console.Write(array[i] + " ");
//     }
//     Console.WriteLine();
// }

// int Count(int[] col, int A, int B)
// {
//     int count = 0;
//     for (int i = 0; i < col.Length; i++)
//     {
//         if (col[i] >= A && col[i] <= B)
//         {
//             count++;
//         }
//     }
//     return count;
// }

// int[] mass = new int[123];
// Fill(mass);
// Print(mass);
// int first = 10;
// int last = 99;
// int num = Count(mass, first, last);
// Console.WriteLine($"Количество элементов в диапазоне от {first} до {last} - {num}");


// Задача 37: Найдите произведение пар чисел 
// в одномерном массиве. Парой считаем первый 
// и последний элемент, второй и предпоследний
// и т.д. Результат запишите в новом массиве. 
// [1 2 3 4 5] -> 5 8 3
// [6 7 3 6] -> 36 21

void Fill(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = new Random().Next(0, 10);
    }
}

void Print(int[] array)
{
    Console.WriteLine("Given array:");
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i] + " ");
    }
    Console.WriteLine();
}

void PrintProd(int[] collection)
{
    int num = collection.Length;
    int firstPos = 0;
    int lastPos = num - 1;
    Console.WriteLine("Resulting array:");
    for (int i = 0; i < num / 2; i++)
    {
        int product = collection[firstPos] * collection[lastPos];
        Console.Write(product + " ");
        firstPos ++;
        lastPos --;
    }
    if (num % 2 == 1) Console.Write (collection[num / 2] + " ");
}

int[] mass = new int[11];
Fill(mass);
Print(mass);
PrintProd(mass);


