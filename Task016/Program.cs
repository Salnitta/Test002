// Пример с лекции

// int rec(int n)
// {
//     if (n == 0)
//     {
//         Console.WriteLine("Это конец рекурсии!");
//         return 1;
//     }


//     Console.WriteLine("Это рекурсия!");

//     return 2 * rec(n - 1);
// }

// Console.WriteLine("Результат рекурсии: " + rec(10)); 


// Задача 63: Задайте значение N. Напишите программу, 
// которая выведет все натуральные числа в промежутке
// от 1 до N.
// N = 5 -> "1, 2, 3, 4, 5"
// N = 6 -> "1, 2, 3, 4, 5, 6"

// Console.WriteLine("Введите число N:");
// int N = int.Parse(Console.ReadLine());

// void rec(int n)
// {
//     if (n == 0) return;
//     rec(n-1);
//     Console.Write(n + " ");
// }

// rec(N);


// Задача 65: Задайте значения M и N. Напишите программу, 
// которая выведет все натуральные числа 
// в промежутке от M до N.
// M = 1; N = 5 -> "1, 2, 3, 4, 5" 
// M = 4; N = 8 -> "4, 6, 7, 8"

// Console.WriteLine("Введите число N:");
// int N = int.Parse(Console.ReadLine());
// Console.WriteLine("Введите число M:");
// int M = int.Parse(Console.ReadLine());

// void rec(int m, int n)
// {
//     if (m > n) return;
//     Console.Write(m + " ");
//     rec(m + 1, n);
// }

// rec(M, N);

// Альтернативное решение:

// void rec(int n, int m)
// {
//     if (n == m - 1) return;
//     rec(n-1, m);
//     Console.Write(n + " ");
// }

// rec(N, M);


// Задача 67: Напишите программу, которая будет принимать
// на вход число и возвращать сумму его цифр.
// 453 -> 12 45 -> 9

// Console.WriteLine("Введите число N:");
// int N = int.Parse(Console.ReadLine());

// int rec(int n)
// {
//     if (n == 0)
//     {
//         return 0;
//     }
//     return rec(n / 10) + n % 10;
// }

// Console.WriteLine(rec(N));


// Задача 69: Напишите программу, которая на вход 
// принимает два числа A и B, и возводит число А 
// в целую степень B с помощью рекурсии.
// A = 3; B = 5 -> 243 (35) 
// A = 2; B = 3 -> 8

// Console.WriteLine("Введите число A:");
// int A = int.Parse(Console.ReadLine());

// Console.WriteLine("Введите число B:");
// int B = int.Parse(Console.ReadLine());

// double rec(int a, int b)
// {
//     if (b == 0)
//     {
//         return 1;
//     }

//     if (b < 0)
//     {
//         return 1 / rec(a, -b - 1);
//     }

//     return a * rec(a, b-1);
// }

// Console.WriteLine(rec(A, B));


// // Альтернативное решение с отрицательными дробями:

// Console.WriteLine("Введите число A: ");
// int A = int.Parse(Console.ReadLine());
// Console.WriteLine("Введите число B: ");
// int B = int.Parse(Console.ReadLine());
// double rec(int A, int B)
// {
//     if (B == 0)
//     {
//         Console.WriteLine("Это конец рекурсии!");
//         return 1;
//     }
//     if (B < 0)
//     {
//         return (1.0 / A) * rec(A, B + 1);
//     }
//     else 
//     return A * rec(A, B - 1);
// }

// Console.WriteLine("Результат рекурсии: " + rec(A, B));


