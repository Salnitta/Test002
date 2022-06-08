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