#include<stdio.h>
int main()
{
    int a[101][101];
	int i,j;
	for(i=0;i<101;i++)
	    a[0][i]=1;
	for(i=0;i<101;i++)
	    a[1][i]=1;
	for(i=2;i<101;i++)
	    a[i][0]=1;
	for(i=2;i<101;i++)
	    a[i][1]=1;
	for(i=2;i<101;i++)
	    for(j=2;j<101;j++)
	        a[i][j] = i >= j ? a[i - j][j] + a[i][j - 1]:a[i][i];
            
	while(scanf("%d %d",&i,&j)==2)
    {
		printf("%d\n",a[i][j]);
	}
	return 0;
} 
