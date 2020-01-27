#include<stdio.h>
#include<string.h>
int main()
{
    char s1[2001],s2[2001];
	int t;
	scanf("%d",&t);
	while(t--)
    {
		int maxlen = 0;
		scanf("%s %s",&s1,&s2);
		for(int i=0;i<strlen(s1);i++)
        {
			if(strlen(s1) - i <= maxlen)
			    break;
			for(int j=0;j<strlen(s2);j++)
            {
				if(s1[i]==s2[j])
                {
					int k=1;
					while(s1[i+k] != '\0' && s2[j+k]!='\0' && s1[i+k]==s2[j+k])
					    k++;
					if(maxlen<k)
					    maxlen=k;
				}
			}
		}
		printf("%d\n",maxlen);
	}
	return 0;
}
