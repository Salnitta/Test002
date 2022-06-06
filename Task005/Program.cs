// Напишите программу, которая принимает на вход 
// трёхзначное число и на выходе показывает 
// последнюю цифру этого числа.

Console.WriteLine("Введите трехзначное положительное число");
int N = int.Parse(Console.ReadLine());
int result = N % 100 % 10;
if(N > 999)
{
    Console.WriteLine("Введено некорректное число");
} 
else if (N < 100)
{
    Console.WriteLine("Введено некорректное число");  
}
else Console.WriteLine(result);