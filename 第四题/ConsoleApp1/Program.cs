using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

    class Program
    {
        public static void Main(string[] args)
        {
        string s = "";
        Console.WriteLine("请输入第一个数字");
        double num1 = 0, num2 = 0;
        s = Console.ReadLine();
        num1 = double.Parse(s);
        Console.WriteLine("请输入第二个数字");
        s = Console.ReadLine();
        num2 = double.Parse(s);
        Console.WriteLine("两个数的积为：");
        Console.WriteLine(num1*num2);
        Console.ReadLine();
        }
    } 

