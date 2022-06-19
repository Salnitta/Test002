// Напишите программу, которая принимает
// на вход число N и выдает произведение
// чисел от 1 до N:
// 4 -> 24
// 5 -> 120

int Func (int num)
{
    int product = 1;
    for (int i = 1; i <= num; i++)
     {
        product *= i;
    } 
    return product;
}

Console.WriteLine("Введите целое число > 0:");
int N = int.Parse(Console.ReadLine());
while (N <= 0)
        {
            Console.WriteLine("Введите целое число >0:");
            N = int.Parse(Console.ReadLine());
        }
Console.WriteLine(Func(N));


// int product = 1;
// if (N>0)
// {
//     for (int i = 1; i <= N; i++)
//     {
//         product *= i;
//     } 
// }
// else 
// {
//     while (N<=0)
//     {
//         Console.WriteLine("Введите целое число >0:");
//         N = int.Parse(Console.ReadLine());
//     }
// }