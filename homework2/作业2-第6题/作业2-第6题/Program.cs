using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 作业2_第6题
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("请输入一个整数");
            string s;
            s = Console.ReadLine();
            int n = int.Parse(s);
            Console.WriteLine("该整数的所有的素数因子为：");
            for(int i=2;i<n+1;i++)
            {
                if (n % i == 0)
                {
                    int j = 2;
                    for (; j < i + 1; j++)
                        if (i % j == 0)
                            break;
                    if(j==i)
                        Console.WriteLine(i);
                }
            }
            Console.ReadLine();
        }
    }
}
