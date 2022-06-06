// Напишите программу, которая на вход принимает 
// одно число (N), а на выходе показывает все 
// целые числа в промежутке от -N до N

Console.WriteLine("Введите целое положительное число");
int N = int.Parse(Console.ReadLine());
int num = N * 2 + 1;
int count = 1;
while(num > count)
{
Console.Write(-N + ", ");
count++;
N--;
}
Console.Write(-N);