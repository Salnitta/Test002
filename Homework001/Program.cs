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