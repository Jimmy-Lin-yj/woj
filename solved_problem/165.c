#include<stdio.h>
#include<math.h>
int main()
{
    int n;
    while(scanf("%d",&n) && n)
    {
        if(n == 1 || n == 2)
        {
            printf("No\n");
            continue;
        }
        int sumA = 0,sumB = 0;
        int tmp = n;
        while(tmp > 0)
        {
            sumA += tmp % 10;
            tmp /= 10;
        }
        int flag = 0;
        for(int i=2;i<=(int)sqrt(n+0.0);i++)
        {
            int cnt = 0,sum = 0;
            if(n % i == 0)
            {
                flag = 1;
                while(n%i == 0 && n > 0)
                {
                    cnt++;
                    n=n/i;
                }
                tmp = i;
                while(tmp>0)
                {
                    sum += tmp%10;
                    tmp /= 10;
                }
                sumB += cnt*sum;
            }
        }
        if(flag)
        {
            if(n != 1)
            {
                while(n > 0)
                {
                    sumB += n % 10;
                    n /= 10;
                }
            }
        }
        else
        {
            printf("No\n");
            continue;
        }
        if(sumB == sumA)
            printf("Yes\n");
        else
            printf("No\n");
    }
}
