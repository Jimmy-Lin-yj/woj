using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 模拟闹钟
{
    class Program
    {
        private static object console;

        static void Main(string[] args)
        {
            
            var Clock1 = new Clock();

            Clock1.clock_warning += Warning;
            Clock1.TimeCount();
        }

        static void Warning(object sender, EventArgs e)
        {
            Console.WriteLine("闹钟已经到时间了");
            Console.ReadLine();
        }
    }

    public delegate void ClockEventHandler(object sender, EventArgs e);

    public  class Clock
    {
        public event ClockEventHandler clock_warning;
        public void TimeCount()
        {
            string s;
            int hour, min;
            Console.WriteLine("请输入闹钟的小时");
            s = Console.ReadLine();
            hour = int.Parse(s);
            Console.WriteLine("请输入闹钟的分钟");
            s = Console.ReadLine();
            min = int.Parse(s);
            while (true)
            {
                int h = DateTime.Now.Hour;
           
                int m = DateTime.Now.Minute;
                if(h==hour&&m==min)
                {
                    EventArgs e = new EventArgs();
                    clock_warning(this, e);
                    break;
                }
            }
        }

    }
}
