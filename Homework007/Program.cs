// Задача 25. Напишите цикл, который принимает 
// на вход два числа (A и B) и возводит 
// число A в натуральную степень B:
// 3, 5 -> 243
// 2, 4 -> 16

int Pow (int num1, int num2)
{
    int result = 1;
    for (int i = 0; i < num2; i++)
    {
        result *= num1;
    }
    return result;
}

int A = -1;
int B = -1;
while(A < 0 || B < 0)
{
    Console.WriteLine("Please, enter two positive integers:");
    A = int.Parse(Console.ReadLine());
    B = int.Parse(Console.ReadLine());
}
Console.WriteLine(Pow(A, B));


// Задача 27. Напишите программу, которая принимает 
// на вход число и выдаёт сумму цифр в числе:
// 452 -> 11 
// 82 -> 10 
// 9012 -> 12

// int SumOfNumbers (int N)
// {
//     int result = 0;
//     for (int i = 0; N > 0; i++)
//     {
//         result += N % 10;
//         N = N / 10;
//     }
//     return result;
// }

// Console.WriteLine("Please, enter integer:");
// int num = int.Parse(Console.ReadLine());
// Console.WriteLine(SumOfNumbers(Math.Abs(num)));


// Задача 29. Напишите программу, которая задаёт массив 
// из N элементов и выводит их на экран:
// 1, 2, 5, 7, 19 -> [1, 2, 5, 7, 19] 
// 6, 1, 33 -> [6, 1, 33]

// 1 способ - рандомные числа:

// void FillArray(int[] collection)
// {
//     for (int i = 0; i < collection.Length; i++)
//     {
//         collection[i] = new Random().Next(0, 100);
//     }
// }

// void PrintArray(int[] col)
// {
//     for (int pos = 0; pos < col.Length; pos++)
//     {
//         Console.Write(col[pos] + " ");
//     } 
// }

// Console.WriteLine("Please, enter the number of array elements:");
// int N = int.Parse(Console.ReadLine());
// int[] array = new int[N];

// FillArray(array);
// PrintArray(array);

// 2 способ - ввод с консоли:

// void FillArray(int[] collection)
// {
//     Console.WriteLine("Please, enter array elements:");
//     for (int i = 0; i < collection.Length; i++)
//     {
//         collection[i] = int.Parse(Console.ReadLine());
//     }
// }

// void PrintArray(int[] col)
// {
//     for (int pos = 0; pos < col.Length; pos++)
//     {
//         Console.Write(col[pos] + " ");
//     } 
// }

// Console.WriteLine("Please, enter the number of array elements:");
// int N = int.Parse(Console.ReadLine());
// int[] array = new int[N];

// FillArray(array);
// PrintArray(array);