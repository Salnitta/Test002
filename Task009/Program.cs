// Напишите программу, которая принимает 
// на вход число и выдаёт количество 
// цифр в числе:
// 456 -> 3 
// 78 -> 2 
// 89126 -> 5

int Func (int num)
{
    if (num == 0)
    {
        return 1;
    }
    else 
    {
        int count = 0;
        for ( ; num > 0; num = num / 10)
        {
            count ++;
        } 
        return count;
    }
}

Console.WriteLine("Введите число:");
int A = int.Parse(Console.ReadLine());
int n = Func(A);
Console.WriteLine(n);

// int count = 0;
// if (A == 0)
// {
//     Console.WriteLine("1");
// }
// else 
// {
//     for ( ; A > 0; A = A / 10)
//     {
//         count ++;
//     }
//     Console.WriteLine(count);
// }


// while (A > 0)
// {
//     A = A / 10;
//     count ++;
// }
// Console.WriteLine(count);