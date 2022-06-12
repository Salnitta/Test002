// 19. Напишите программу, которая принимает 
// на вход пятизначное число и проверяет, 
// является ли оно палиндромом:
// 14212 -> нет
// 23432 -> да
// 12821 -> да


Console.WriteLine("Введите целое положительное пятизначное число:");
int num = int.Parse(Console.ReadLine());
if (num < 10000)
{
    Console.WriteLine("Введено некорректное число");
}
else if (num / 10000 == num % 10 && num / 1000 % 10 == num % 100 / 10)
{
    Console.WriteLine("Да, палиндром");
}
else Console.WriteLine("Нет, не палиндром");


// 21. Напишите программу, которая принимает на вход 
// координаты двух точек и находит расстояние 
// между ними в 3D пространстве:
// A (3,6,8); B (2,1,-7), -> 15.84 
// A (7,-5, 0); B (1,-1,9) -> 11.53


// Console.WriteLine("Введите координаты x, y, z первой точки:");
// double x1 = double.Parse(Console.ReadLine());
// double y1 = double.Parse(Console.ReadLine());
// double z1 = double.Parse(Console.ReadLine());

// Console.WriteLine("Введите координаты x, y, z второй точки:");
// double x2 = double.Parse(Console.ReadLine());
// double y2 = double.Parse(Console.ReadLine());
// double z2 = double.Parse(Console.ReadLine());

// double num1 = Math.Pow(x2-x1,2);
// double num2 = Math.Pow(y2-y1,2);
// double num3 = Math.Pow(z2-z1,2);

// double result = Math.Sqrt(num1 + num2 + num3);
// Console.WriteLine("Расстояние между точками равно " + Math.Round(result,2));


// 23. Напишите программу, которая принимает 
// на вход число (N) и выдаёт таблицу кубов 
// чисел от 1 до N:
// 3 -> 1, 8, 27
// 5 -> 1, 8, 27, 64, 125


// Console.WriteLine("Введите целое число > 1:");
// int N = int.Parse(Console.ReadLine());
// int i = 1;

// if (N > 1)
// {
//     while (i <= N)
//     {
//         Console.Write(Math.Pow(i, 3) + " ");
//         i++;
//     }
// }
// else Console.WriteLine("Введено некорректное число");

