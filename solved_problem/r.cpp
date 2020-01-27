#include<stdio.h>
#include<iostream>
#include<cmath>
#include<string.h>
using namespace std;
const int MIN = -1e9;
char str[100010];
int dp[100010][7];
int main()
{
    scanf("%s",str + 1);
    int len = strlen(str + 1);
    for(int i=0;i <= len;i++)
        for(int j = 0;j < 6; j++)
            dp[i][j] = MIN;
    int ans = MIN;
    for(int i=1; i <= len; i++) 
	    if(str[i] == '0')
	    {
		ans = 1;
		break;
	    }
    for(int i=1; i <= len; i++)
    {
        int n = str[i] - '0';
        if(n != 0)
            dp[i][n%6]=1;
        for(int j=0; j <= 5; j++)
            dp[i][j] = max(dp[i-1][j],dp[i][j]);
        for(int j=0; j <= 5; j++)
            dp[i][(j*10 + n)%6] = max(dp[i-1][j]+1,dp[i][(j*10+n)%6]);
        ans = max(ans,dp[i][0]);
    }
    if(ans > 0)
        cout << ans << endl;
    else
        cout << "-1s" << endl;
}
