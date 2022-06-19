// Напишите программу, которая принимает на вход 
// число (А) и выдает сумму чисел от 1 до А.

int Func(int num)
{
   int sum = 0;
   for (int i = 1; i <= num; i++)
   {
        sum += i;
    }
    return sum;
}

Console.WriteLine("Введите число:");
int A = int.Parse(Console.ReadLine());

int n = Func(A);
Console.WriteLine(n);

Console.WriteLine(Func(7));
Console.WriteLine(Func(4));
Console.WriteLine(Func(8));
Console.WriteLine(Func(-4));
Console.WriteLine(Func(0));
Console.WriteLine(Func(1));

// Console.WriteLine("Введите число:");
// int A = int.Parse(Console.ReadLine());

// int sum = 0;

// for (int i = 1; i <= A; i++)
// {
//     sum += i;
// }
// Console.WriteLine(sum);