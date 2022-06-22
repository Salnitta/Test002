﻿// Задача 34: Задайте массив заполненный 
// случайными положительными трёхзначными числами. 
// Напишите программу, которая покажет количество 
// чётных чисел в массиве:
// [345, 897, 568, 234] -> 2

// void Fill(int[] arr)
// {
//     for (int i = 0; i < arr.Length; i++)
//     {
//         arr[i] = new Random().Next(100, 1000);
//     }
// }

void Print(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        Console.Write(arr[i] + " ");
    } 
    Console.WriteLine();
}

// int SearchEvenNumbers(int[] arr)
// {
//     int count = 0;
//     for (int i = 0; i < arr.Length; i++)
//     {
//         if (arr[i] % 2 == 0) count ++;
//     }
//     return count;
// }

// int[] array = new int[10];
// Fill(array);
// Print(array);
// int num = SearchEvenNumbers(array);
// Console.WriteLine(num);


// Задача 36: Задайте одномерный массив, заполненный 
// случайными числами. Найдите сумму элементов, 
// стоящих на нечётных позициях:
// [3, 7, 23, 12] -> 19 
// [-4, -6, 89, 6] -> 0

// void Fill(int[] arr)
// {
//     for (int i = 0; i < arr.Length; i++)
//     {
//         arr[i] = new Random().Next(-9, 10);
//     }
// }

// int SumOddIndex(int[] arr)
// {
//     int sum = 0;
//     for (int i = 0; i < arr.Length; i++)
//     {
//         if (i % 2 == 1) sum += arr[i];
//     }
//     return sum;
// }

// int[] array = new int[10];
// Fill(array);
// Print(array);
// int amount = SumOddIndex(array);
// Console.WriteLine(amount);



// Задача 38: Задайте массив вещественных чисел. 
// Найдите разницу между максимальным и минимальным 
// элементов массива.
// [3 7 22 2 78] -> 76

void Fill(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = new Random().Next(0, 100);
    }
}

int SearchMax(int[] arr)
{
    int maxPos = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] > arr[maxPos]) maxPos = i;
    }
    return arr[maxPos];
}

int SearchMin(int[] arr)
{
    int minPos = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] < arr[minPos]) minPos = i;
    }
    return arr[minPos];
}

int[] array = new int[10];
Fill(array);
Print(array);
int max = SearchMax(array);
int min = SearchMin(array);
int diff = max - min;
Console.WriteLine($"Разница между max и min = {diff}");


