#include<stdio.h>  
#include<iostream>  
#include<string>  
using namespace std;    
int main()
{  
    char* names[8] = {"littleken", "knuthocean", "dongfangxu", "zap", "kittig", "robertcui", "forest", "flirly" };  
    char a[8] = { 'l', 'k', 'd', 'z', 'k', 'r', 'f', 'f' };  
    char b[8] = { 'i', 'n', 'o', 'a', 'i', 'o', 'o','l' };  
    int next[8] = { 9, 10, 10, 3, 6, 9, 6, 6 };  
    int n;  
    cin >> n;  
    for (int i = 0; i < n; i++)
    {  
        string str;  
        cin >> str;  
        int max = 0;  
        int flag = 0;  
        int c[8] = { 0 };  
        for (string::iterator it = str.begin(); it != str.end();)
        {  
            for (int j = 0; j < 8; j++)
            {  
                if (*it == a[j] && *(it + 1) == b[j])
                {  
                    it += next[j];  
                    c[j]++;  
                    break;  
                }  
            }  
        }  
        for (int j = 0; j < 8; j++)
            if (max < c[j])  
            {  
                max = c[j];  
                flag = j;  
            }    
        printf("%s\n", names[flag]);  
    }  
}  