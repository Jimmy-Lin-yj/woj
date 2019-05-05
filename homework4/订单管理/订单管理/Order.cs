using System;

namespace 订单管理
{
    class Order
    {
        static void Main(string[] args)
        {
            int n;
            string str;
            Console.WriteLine("输入add添加订单，del删除订单，update修改订单，search查询订单,quit表示退出");
            while(true)
            {
                str = Console.ReadLine();
                if (str == "add")
                    OrderService.AddItem();
                else if (str == "del")
                    OrderService.DelItem();
                else if (str == "update")
                    OrderService.UpdateItem();
                else if (str == "search")
                    OrderService.SearchItem();
                else if (str == "quit")
                    break;
                else
                    Console.WriteLine("输入命令出错，请重新输入");
                
            }
        }
    }
}
