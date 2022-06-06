// Напишите программу, которая на вход принимает 
// одно число (N), а на выходе показывает все 
// целые числа в промежутке от -N до N

Console.WriteLine("Введите целое положительное число");
int N = int.Parse(Console.ReadLine());
int i = -N;
while(i < N)
{
Console.Write(i + ", ");
i++;
}
Console.Write(N);