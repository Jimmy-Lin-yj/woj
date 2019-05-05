using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
/*实现一个电视生产的工厂模式，client为客户端，ITV为接口，TVFactory为工厂类*/
namespace 简单工厂模式
{
    class Client
    {
        public static void Main(string[] args)
        {
            ITV tv;
            string s;
            Console.WriteLine("输入要生产的电视名：");
            s = Console.ReadLine();
            tv = TVFactory.ProduceTV(s);
            tv.play();
            Console.ReadLine();
        }
    }

    public class TVFactory
    {
        public static ITV ProduceTV(string brand)
        {
            ITV tv = null;
            if(brand=="Haier")
            {
                Console.WriteLine("工厂生产海尔电视");
                tv = new HaierTv();
            }
            else if (brand == "HisenseTv")
            {
                Console.WriteLine("工厂生产海信电视");
                tv = new HisenseTv();
            }
            else if (brand == "TCL")
            {
                Console.WriteLine("工厂生产TCL电视");
                tv = new TCL();
            }
            return tv;
        }
    }

    public interface ITV
    {
        void play();
    }

    public class HaierTv : ITV
    {
        public void play()
        {
            Console.WriteLine("海尔电视在播放中");
        }
    }

    public class HisenseTv:ITV
    {
        public void play()
        {
            Console.WriteLine("海信电视在播放中");
        }
    }

    public class TCL:ITV
    {
        public void play()
        {
            Console.WriteLine("TCL电视在播放中");
        }
    }
}
