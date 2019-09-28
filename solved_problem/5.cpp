#include<iostream>
using namespace std;
int main()
{
    int dp[100001],num,s[100],w[100],size;
    while (cin>>num)
    {
        for(int i=0;i<num;i++)
        {
            cin>>s[i]>>w[i];
        }
        cin>>size;
        for(int i=0;i<=size;i++)
        {
            dp[i] = 0;
        }
        for(int i=0;i<num;i++)
        {
            for(int j=size;j>=s[i];j--)
            {
                dp[j] = dp[j] > dp[j - s[i]] + w[i]?dp[j]:dp[j - s[i]] + w[i];
            }
        }
        cout<<dp[size]<<endl;
    }
}