// * Задача 61: Вывести первые N строк треугольника Паскаля. 
// Сделать вывод в виде равнобедренного треугольника

Console.WriteLine("Введите число N:");
int n = int.Parse(Console.ReadLine());

int Factorial(int n)
{
    int x = 1;
    for (int i = 1; i <= n; i++)
    {
        x *= i;
    }
    return x;
}

int c = 0;
int i = 0;
int result = 0;
for (i = 0; i < n; i++)
{
    for (c = 0; c <= (n - i); c++) // создаём после каждой строки n-i отступов от левой стороны консоли, чем ниже строка, тем меньше отступ
    {
        Console.Write(" "); 
    }
    for (c = 0; c <= i; c++)
    {
        Console.Write(" "); // создаём пробелы между элементами треугольника
        result = Factorial(i) / (Factorial(c) * Factorial(i - c)); //формула вычисления элементов треугольника
        if (result < 10) Console.Write("0" + result);
        else Console.Write(result); 
    }
    Console.WriteLine();
    Console.WriteLine(); // после каждой строки с числами отступаем две пустые строчки
}
