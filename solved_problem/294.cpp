#include<iostream>
using namespace std;
int main()
{
    int adult[20],child[20],mouse[20];
    child[0] = mouse[0] = 1;
    adult[0] = 0;
    for(int i=1;i<=18;i++)
    {
        adult[i]=adult[i-1]*3+child[i-1];
        child[i]=adult[i-1]*2+child[i-1]*2;
        mouse[i]=adult[i]+child[i];
    }
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int m;
        cin>>m;
        cout<<mouse[m]<<endl;
    }
}