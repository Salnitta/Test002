// Задача 64: Задайте значения M и N. Напишите программу, 
// которая выведет все натуральные числа в промежутке от M до N.
// M = 1; N = 5. -> "1, 2, 3, 4, 5"
// M = 4; N = 8. -> "4, 6, 7, 8"

// Console.WriteLine("Введите число M:");
// int M = int.Parse(Console.ReadLine());
// Console.WriteLine("Введите число N:");
// int N = int.Parse(Console.ReadLine());

// int rec(int m, int n)
// {
//     if (m > n) 
//     {
//        Console.Write(m + " ");
//        return rec(m - 1, n); 
//     }
    
//     if (m == n) 
//     {
//         Console.WriteLine(n);
//         return n;
//     }
    
//     Console.Write(m + " ");
//     return rec(m + 1, n);
// }

// rec(M, N);


// Задача 66: Задайте значения M и N. Напишите программу, которая 
// найдёт сумму натуральных элементов в промежутке от M до N.
// M = 1; N = 15 -> 120
// M = 4; N = 8. -> 30

// Console.WriteLine("Введите число M:");
// int M = int.Parse(Console.ReadLine());
// Console.WriteLine("Введите число N:");
// int N = int.Parse(Console.ReadLine());

// int rec(int m, int n)
// {
//     if (m > n) 
//     {
//        return m + rec(m - 1, n); 
//     }
    
//     if (m == n) 
//     {
//         return n;
//     }
    
//     return m + rec(m + 1, n);
// }

// Console.WriteLine(rec(M, N));


// Задача 68: Напишите программу вычисления функции Аккермана 
// с помощью рекурсии. Даны два неотрицательных числа m и n.
// m = 3, n = 2 -> A(m,n) = 29
// m = 3, n = 5 -> A(m,n) = 253
// m = 0, n = 0 -> A(m,n) = 1
// m = 0, n = 5 -> A(m,n) = 6

Console.WriteLine("Введите целое неотрицательное число M:");
int M = int.Parse(Console.ReadLine());
Console.WriteLine("Введите целое неотрицательное число N:");
int N = int.Parse(Console.ReadLine());

int Ackermann(int m, int n)
{
    if (m == 0) 
    {
       return n + 1; 
    }
    
    if (m > 0 && n == 0) 
    {
        return Ackermann(m - 1, 1);
    }

    if (m > 0 && n > 0)
    {
        return Ackermann(m - 1, Ackermann(m, n-1));
    }
    
    return -1;
}

int result = Ackermann(M, N);

if(result < 0) Console.WriteLine("Некорректный ввод значений");
else Console.WriteLine(result);


