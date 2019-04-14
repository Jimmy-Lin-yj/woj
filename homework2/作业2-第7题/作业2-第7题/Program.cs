using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 作业2_第7题
{
    class Program
    {
        static void Main(string[] args)
        {
            string s;
            int n;
            Console.WriteLine("请输入数组的大小：");
            s = Console.ReadLine();
            n = int.Parse(s);
            int[] array=new int[n];
            Console.WriteLine("请输入数组中的各个元素,每输入一个回车一下：");
            for(int i=0;i<n;i++)
            {
                s = Console.ReadLine();
                array[i] = int.Parse(s);
            }
 
            int max = array[0];
            int min = array[0];
            int sum = 0;
            foreach (int i in array)
            {
                if (i > max)
                    max = i;
                if (i < min)
                    min = i;
                sum += i;
            }
            Console.WriteLine($"数组中最大的值为：{max}");
            Console.WriteLine($"数组中最小的值为:{min}");
            Console.WriteLine($"数组的平均值为：{(float)sum/n}");
            Console.WriteLine($"数组的总和为：{sum}");
            Console.ReadLine();
        }
    }
}
