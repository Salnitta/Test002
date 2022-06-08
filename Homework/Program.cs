// Напишите программу, которая на вход принимает 
// два числа и выдаёт, какое число большее, а какое меньшее.

Console.WriteLine("Введите первое число:");
double numberA = double.Parse(Console.ReadLine());
Console.WriteLine("Введите второе число:");
double numberB = double.Parse(Console.ReadLine());
if(numberA > numberB)
{
    Console.WriteLine(numberA + "- большее число");
    Console.WriteLine(numberB + "- меньшее число");
}
else if(numberA < numberB)
{
    Console.WriteLine(numberB + "- большее число");
    Console.WriteLine(numberA + "- меньшее число");
}
else
Console.WriteLine("Введенные числа равны");


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


// Напишите программу, которая на вход принимает число 
// и выдаёт, является ли число чётным (делится ли оно 
// на два без остатка).

Console.WriteLine("Введите целое число:");
int num = int.Parse(Console.ReadLine());
if(num % 2 == 0)
{
    Console.WriteLine("Это четное число");
}
else Console.WriteLine("Это нечетное число");


// Напишите программу, которая на вход принимает число (N), 
// а на выходе показывает все чётные числа от 1 до N.

Console.WriteLine("Введите целое положительное число:");
int N = int.Parse(Console.ReadLine());
int i = 2;
while(N >= i)
    {
    Console.Write(i + " ");
    i += 2;
    }