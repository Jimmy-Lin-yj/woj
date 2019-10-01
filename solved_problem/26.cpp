#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int max(int a,int b,int c);
int main()
{
	int t,n,ans=0;
    int board[1010][1010],dp[1010][1010];
	cin>>t;
	for(int k=1;k<=t;k++)
    {
		cin>>n;
		memset(dp,0,sizeof(dp));
		for(int i=1;i<=n;i++)
		    for(int j=1;j<=n;j++)
			    cin>>board[i][j];
		for(int j=1;j<=n;j++)
            dp[1][j]=board[1][j];
		for(int i=2;i<=n;i++)
		    for(int j=1;j<=n;j++)
		        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])+board[i][j];
		for(int j=1;j<=n;j++)
		    if(ans<dp[n][j])
                ans=dp[n][j]; 
		if(k != 1)
		    puts("");
		printf("Case %d:\n",k);
		cout<<ans<<endl;	
	}
	return 0;
}
int max(int a,int b,int c){
	int max=a>b?a:b;
	max=max>c?max:c;
	return max;
} 
