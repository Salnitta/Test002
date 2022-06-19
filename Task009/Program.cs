// Напишите программу, которая принимает 
// на вход число и выдаёт количество 
// цифр в числе:
// 456 -> 3 
// 78 -> 2 
// 89126 -> 5

int Func (int num)
{
    if (num != 0)
    {
        int count = 0;
        for ( ; num != 0; num = num / 10)
        {
            count ++;
        } 
        return count;
    }
    else return 1;
}

double A = 0.28;
while (A % 1 != 0 & A != 0)
{
    Console.WriteLine("Введите целое число:");
    A = double.Parse(Console.ReadLine());
}
Console.WriteLine(Func((int)A));

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