// Напишите программу, которая принимает на вход 
// три числа и выдаёт максимальное из этих чисел.

Console.WriteLine("Введите первое число:");
double a = double.Parse(Console.ReadLine());
Console.WriteLine("Введите второе число:");
double b = double.Parse(Console.ReadLine());
Console.WriteLine("Введите третье число:");
double c = double.Parse(Console.ReadLine());
double max = a;
if(b > max) max = b;
if(c > max) max = c;
Console.WriteLine("max = " + max);