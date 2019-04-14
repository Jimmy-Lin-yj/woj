using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 作业2_9题
{
    class Program
    {
        public static void Main(string[] args)
        {
            bool[] array = new bool[99];
            for(int i=2;i<101;i++)
            {
                array[i - 2] = true;
            }
            Console.WriteLine("2到100之间的素数有：");
            for(int i=2;i<101;i++)
            {
                for(int j=2;j<101;j++)
                {
                    if (j % i == 0 && j > i)
                        array[j - 2] = false;
                }
            }
           for(int i=2;i<101;i++)
            {
                if(array[i-2])
                    Console.WriteLine(i);
            }
            Console.ReadLine();
        }
    }
}
