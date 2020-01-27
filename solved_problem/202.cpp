#include<iostream>
using namespace std;
int main()
{
    int n,m,sum=0;
    cin>>n;
    for(int i=0;i<2*n+1;i++)
    {
        cin>>m;
        sum ^= m;
    }
    cout<<sum<<endl;
}