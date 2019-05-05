using System;
using System.Collections.Generic;

namespace 订单管理
{
    class OrderService
    {
        private static List<OrderDetails> orderDetails=new List<OrderDetails>();
        static string no, goods_name, client;
        static int num;
        static public void AddItem()
        {
            Console.WriteLine("输入要增加的订单号");
            no = Console.ReadLine();
            Console.WriteLine("输入要增加的商品名");
            goods_name = Console.ReadLine();
            Console.WriteLine("输入要增加的客户名");
            client = Console.ReadLine();
            Console.WriteLine("输入要增加的商品数量");
            num = int.Parse(Console.ReadLine());
            OrderDetails order = new OrderDetails(no,goods_name,client,num);
            orderDetails.Add(order);
            Console.WriteLine("订单添加成功");
            
        }
        static public void DelItem()
        {
            Console.WriteLine("输入要删除的订单号");
            no = Console.ReadLine();
            try
            {
                int count = -1;
                for(int i=0;i<orderDetails.Count;i++)
                {
                    if(orderDetails[i].no==no)
                    {
                        count = i;
                        break;
                    }
                }
                orderDetails.RemoveAt(count);
                    
            }
            catch(System.Exception)
            {
                Console.WriteLine("订单删除失败");
            }

        }
        static public void UpdateItem()
        {
            Console.WriteLine("输入要修改的订单号");
            no = Console.ReadLine();
            try
            {
                int count = -1;
                for (int i = 0; i < orderDetails.Count; i++)
                {
                    if (orderDetails[i].no == no)
                    {
                        count = i;
                        break;
                    }
                }
                Console.WriteLine("输入要修改的字段：0-订单号，1-商品名，2-客户名，3-商品数量");
                int a = int.Parse(Console.ReadLine());
                Console.WriteLine("输入要修改的内容");
                string b = Console.ReadLine();
                switch(a)
                {
                    case 0:orderDetails[count].no = b;break;
                    case 1:orderDetails[count].goods_name = b;break;
                    case 2:orderDetails[count].client = b;break;
                    case 3:orderDetails[count].num = int.Parse(b);break;
                    default:break;
                }
            }
            catch (System.Exception)
            {
                Console.WriteLine("订单修改失败");
            }

        }
        static public void SearchItem()
        {
            Console.WriteLine("输入以下数字选择查询的字段：0-订单号，1-商品名，2-客户名");
            string s = Console.ReadLine();
            if (s == "0")
            {
                Console.WriteLine("输入查询的订单号");
                no = Console.ReadLine();
                foreach(OrderDetails i in orderDetails)
                {
                    if(i.no==no)
                    {
                        Console.WriteLine("查询的结果为：");
                        Console.WriteLine($"订单号{no}，商品名{i.goods_name},客户名{i.client},商品数量{i.num}");
                        return;
                    }

                }
                Console.WriteLine("没有要查询的结果");
            }
            else if(s=="1")
            {
                int count = 0;
                Console.WriteLine("输入要查询的商品名");
                goods_name = Console.ReadLine();
                foreach(OrderDetails i in orderDetails)
                {
                    if(i.goods_name==goods_name)
                    {
                        Console.WriteLine("查询的结果为：");
                        Console.WriteLine($"订单号{no}，商品名{i.goods_name},客户名{i.client},商品数量{i.num}");
                        count++;
                    }
                }
                if(count==0)
                    Console.WriteLine("没有要查询的结果");
            }
            else if(s=="2")
            {
                int count = 0;
                Console.WriteLine("输入要查询的客户名");
                client = Console.ReadLine();
                foreach(OrderDetails i in orderDetails)
                {
                    if(i.client==client)
                    {
                        Console.WriteLine("查询的结果为：");
                        Console.WriteLine($"订单号{no}，商品名{i.goods_name},客户名{i.client},商品数量{i.num}");
                        count++;
                    }
                }
                if (count == 0)
                    Console.WriteLine("没有要查询的结果");
            }

            else Console.WriteLine("输入出错");
        }
    }
}
