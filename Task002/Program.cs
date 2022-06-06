// Напишите программу, которая на вход 
// принимает два числа и проверяет, 
// является ли первое число квадратом второго

Console.WriteLine("Введите первое число:");
double numberA = double.Parse(Console.ReadLine());
Console.WriteLine("Введите второе число:");
double numberB = double.Parse(Console.ReadLine());
double Result = numberB * numberB;
if(numberA == Result)
{
   Console.WriteLine("Число: " + numberA + " является квадратом числа " + numberB); 
}
else
{
    Console.WriteLine("Число: " + numberA + " не является квадратом числа " + numberB); 
}
