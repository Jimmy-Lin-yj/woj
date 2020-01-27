#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
using namespace std;
typedef struct Node{
    int p, s; 
    char l;
}node;
node e[105][105];
int n,m,dist[105],g[105][105],fa[105],plove,slove;
 
inline bool relax(int u,int v)
{
    if(dist[u]+g[u][v]<dist[v]) 
    {
        dist[v]=dist[u]+g[u][v];
        return true;
    }
    return false;
}
inline bool judge(node e)
{
	return ((plove>e.p)&&(slove>e.s));
}
 
void spfa(int s)
{
    int vis[n+5];
    memset(vis,0,sizeof(vis));
    queue<int> q;
    q.push(s);
    vis[s] = true;
    dist[s] = 0;
    while(!q.empty())
    {
        int temp=q.front();
        q.pop();
        for(int i=0;i<n;i++) 
            if(g[temp][i]&&judge(e[temp][i])&&relax(temp,i))
            {
                q.push(i);
                fa[i]=temp;
                vis[i]=true;
            }
        vis[temp]=false;
    }
}
int main()
{
    int i,j,a,b,p,s,c;
	char l;
    while(scanf("%d %d",&n,&m)==2)
    {
    	memset(g,0,sizeof(g));
    	memset(e,0,sizeof(e));
    	memset(fa,-1,sizeof(fa));
    	for(i=0;i<n;i++)
    	dist[i]=0x7fffffff;
		for(i=0;i<m;i++)
        {
			scanf("%d%d%d%d%d %c",&a,&b,&p,&s,&c,&l);
			g[a][b]=g[b][a]=c;
			e[a][b].p=e[b][a].p=p;
			e[a][b].s=e[b][a].s=s;
			e[a][b].l=e[b][a].l=l;
		}
		scanf("%d %d",&plove,&slove);
		spfa(0);
		i=n-1,j=0;
		node st[105];
		while(i)
        {
			st[j++]=e[fa[i]][i];
			i=fa[i];
		}
		for(i=j-1;i>=0;i--)
		printf("%c",st[i].l);
		printf("\n\n");
	}
	return 0;
}
