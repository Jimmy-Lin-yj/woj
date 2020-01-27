#include<stdio.h>
#include<string.h>
int main()
{
    char c[205];
    char s[15];
	while(scanf("%s",&s)&&strcmp(s,"ENDOFINPUT"))
    {
		getchar();
		gets(c);
		int i=0;
		while(c[i]!='\0')
        {
			if(c[i]>='A'&&c[i]<='Z')
            {
				c[i] -= 5;
				if(c[i]<'A')
				c[i] += 26;
			}
			i++;
		}
		scanf("%s",&s);
		printf("%s\n",c); 
	}
	return 0;
}
