namespace 订单管理
{
    class OrderDetails
    {
        public string no;//商品号
        public string goods_name;//商品名
        public string client;
        public int num;//货物数量

        public OrderDetails(string no,string goods_name,string client,int num)
        {
            this.no = no;
            this.goods_name = goods_name;
            this.client = client;
            this.num = num;
        }
    }
}
