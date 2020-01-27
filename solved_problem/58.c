#include<stdio.h>
int main()
{
    long long a,b,t,c;
    while(scanf("%lld",&t)&&t)
    {
        c = 0;
        for(a = t/3;a>=0;a--)
        {
            b = (t-a*3)/2+1;
            c += b;
        }
        printf("%lld\n",c);
    }
}