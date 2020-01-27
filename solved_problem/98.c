#include<stdio.h>
#include<string.h> 
int count(char line[],char key[]);
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        char a[100000];
        char d[]="dongfangxu";
        char z[]="zap";
        int dongfangxu = 0,zap = 0;
        scanf("%s",a);
        dongfangxu = count(a,d);
        zap=count(a,z);
        if(dongfangxu>=zap)
        printf("dongfangxu!\n");
        else
        printf("zap!\n");
    }
    return 0;
} 
int count(char line[],char key[])
{
    int lenl,lenk,i,j,count=0,max=0;
    lenl=strlen(line);
    lenk=strlen(key);
    for (i = 0; i < lenl; i++) 
    { 
        for (j = 0; j < lenk; j++) 
        { 
            if (line[i + j] != key[j]) 
            { 
                count=0; 
                break; 
            } 
        } 
        if (j == lenk) 
        {  
            i += lenk - 1; 
            count++; 
        } 
        if(max<count) 
            max=count; 
    } 
    return max; 
} 