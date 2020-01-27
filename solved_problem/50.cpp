#include<iostream>
#include<cstdio>
#include<cmath> 
#include<algorithm>
using namespace std;
const int maxn=105,maxm=5000;
int matrix[maxn][maxn];
struct v{
	int x,y,c;
};
v u[maxm];
int r[maxm];
int p[maxn];
int n,t;
int cmp(const int i,const int j)
{
    return u[i].c<u[j].c;
}
int find(int a)
{
    while(a!=p[a])
        a=p[a];
    return a;
}
int main()
{
    int i,j,m=-1,ans;
    scanf("%d",&t);
    while(t--)
    {
    	scanf("%d",&n);
        ans=0;
        m=-1;
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                scanf("%d",&matrix[i][j]);
        for(i=0;i<n;i++) 
            for(j=i+1;j<n;j++)
            {
                m++;
				u[m].x=i;
				u[m].y=j;
				u[m].c=matrix[i][j];               
            }  
        for(i=0;i<n;i++)
            p[i]=i;
        for(i=0;i<=m;i++)
            r[i]=i;
        sort(r,r+m+1,cmp);
        for(i=0;i<=m;i++)
        {
            int e = r[i];
            int x = find(u[e].x);
            int y = find(u[e].y);
            if(x != y)
            {
                ans += u[e].c;
                p[x] = y;
            } 
        }
        printf("%d\n",ans);
    }
    return 0;
}
