﻿// Напишите программу, которая принимает на вход 
// трёхзначное число и на выходе показывает 
// последнюю цифру этого числа.

Console.WriteLine("Введите трехзначное положительное число");
int N = int.Parse(Console.ReadLine());
if((N > 99) & (N < 1000))
{
    Console.WriteLine(N % 10);
} 
else Console.WriteLine("Введено некорректное число");