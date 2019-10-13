#include <stdio.h>
int main()
{
    char a[1000];
    while (gets(a) && a[0] != '$')
    {
        int i = 0;
        while (a[i] >= 'A'&&a[i] <= 'Z') 
        {
            a[i] -= i + 1;
            while (a[i] < 'A') 
                a[i] += 26;
            printf("%c", a[i]);
            i++;
        }

        printf("\n");
        while (a[i] >= 'A'&&a[i] <= 'Z') 
            a[i] = 0;
    }

    return 0;
}