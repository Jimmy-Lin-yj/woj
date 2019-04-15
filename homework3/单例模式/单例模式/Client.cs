using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
/*实现单例模式，仅创建一个学生对象*/
namespace 单例模式
{
    class Client
    {
        public static void Main(string[] args)
        {
            /*测试创建的对象是否唯一*/
            Console.WriteLine("现创建四个学生对象");
            Student s1, s2, s3, s4;
            s1 = Student.getInstance();
            s2 = Student.getInstance();
            s3 = Student.getInstance();
            s4 = Student.getInstance();

            if(s1==s2&&s2==s3&&s3==s4)
                Console.WriteLine("四个学生对象都相同");
            Console.WriteLine($"该学生的年龄与姓名为{s1.Age}和{s1.Name}");
            Console.ReadLine();
        }
    }
    class Student
    {
        private string name;
        private int age;
        public string Name { get { return name; } set { Name = value; } }
        public int Age { get { return age; } set { Age = value; } }
        private Student()
        {
            string s;
            int n;
            Console.WriteLine("输入学生的年龄");
            s = Console.ReadLine();
            n = int.Parse(s);
            Console.WriteLine("输入学生的姓名");
            s = Console.ReadLine();
            name = s;
            age = n;
        }
        private static Student st = null;
        /*创建唯一实例*/
        public static Student getInstance()
        {
            if (st == null)
                st = new Student();
            return st;
        }

    }
}
