// 10. Напишите программу, которая выводит 
// случайное число из отрезка [10, 99] и 
// показывает наибольшую цифру числа.

// int num = new Random().Next(10, 100);
// Console.WriteLine(num);

// int c1 = num / 10; // 12345 / 10 = 1234
// int c2 = num % 10; // 12345 % 10 = 5

// if (c1 > c2)
// {
//     Console.WriteLine(c1);
// }
// else Console.WriteLine(c2);

// 11. Напишите программу, котоорая выводит 
// случайное трехзначное число и удаляет 
// вторую цифру этого числа

// int num = new Random().Next(100, 1000);
// Console.WriteLine(num);

// int c1 = num / 100; // 345 / 100 = 3
// int c2 = num % 10; // 345 % 10 = 5

// Console.WriteLine($"{c1}{c2}");
// Console.WriteLine(c1*10+c2);

// 12. Напишите программу, которая будет принимать на вход 
// два числа и выводить, является ли второе число кратным 
// первому. Если число 2 не кратно числу 1, то программа 
// выводит остаток от деления

// Console.WriteLine("Введите первое число:");
// int a = int.Parse(Console.ReadLine());

// Console.WriteLine("Введите второе число:");
// int b = int.Parse(Console.ReadLine());

// if (a % b == 0)
// {
//     Console.WriteLine("Кратно");
// }
// else
// {
//     Console.WriteLine("Не кратно, остаток " + a % b);
// }

// 14. Напишите программу, которая принимает на вход 
// число и проверяет, кратно ли оно одновременно 7 и 2

// Console.WriteLine("Введите число:");
// int a = int.Parse(Console.ReadLine());

// if ((a % 161 == 0))
// {
//     Console.Write("Число кратно 7 и 23");
// }
// else Console.WriteLine("Число не кратно 7 и 23");

// 13. Напишите программу, которая выводит третью 
// цифру заданного числа или сообщает, что 
// третьей цифры нет

// Console.WriteLine("Введите число:");
// int a = int.Parse(Console.ReadLine());

// if (a < 100)
// {
//     Console.WriteLine ("Третьей цифры нет");
// }
// else
// {
//     while (a > 999)
//     {
//     a /= 10;
//     }
// Console.WriteLine(a % 10);
// }

// 13. Второй вариант решения через строку




