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