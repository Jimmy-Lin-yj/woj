#include<stdio.h>
#include<string.h>
#include<stdbool.h>
int main()
{
    int n,r,pos_flag,i,a[102];
    while (scanf("%d %d",&n,&r)!=EOF)
    {        
        if(n==0&&r==0) break;
        if(n==0)
        {
            printf("0\n");
            continue;
        }
        r*=-1;
        pos_flag=1;
        if(n<0){
            pos_flag=0;
            n*=-1;
        }
        int k=0;
        memset(a,0,sizeof(a));
        while(n!=0)
        {
            int tmp=n%r;
            a[k++]=tmp;
            n/=r;
        }
        i=0;
        while(i<k||a[i])
        {
            if(a[i]>=r)
            {
                a[i]%=r;
                a[i+1]++;
            }
            if(i%2 == pos_flag && a[i])
            {
                a[i] = r-a[i];
                a[i+1]++;
            }
            i++;
        }
        for(i=i-1;i>=0;i--)
        {
            if(a[i]>9) 
            printf("%c",'A'+a[i]-10);
            else 
            printf("%d",a[i]);
        }
        printf("\n");
    }
    return 0;
}
