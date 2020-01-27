#include<stdio.h>
int countScore(double a,double b)
{
    double d = a*a + b*b;
    if(d <= 9.00)
        return 100;
    if(d > 9.00 && d <= 36.00)
        return 80;
    if(d > 36.00 && d <= 81.00)
        return 60;
    if(d > 81.00 && d <= 144.00)
        return 40;
    if(d > 144.00 && d <= 225.00)
        return 20;
    else
        return 0;
}
int main()
{
    int score_a,score_b;
    double a[12];
    while(1)
    {
        for(int i=0;i<12;i++)
            scanf("%lf",&a[i]);
        if(a[0] == -100)
            break;
        score_a = countScore(a[0],a[1]) + countScore(a[2],a[3]) + countScore(a[4],a[5]);
        score_b = countScore(a[6],a[7]) + countScore(a[8],a[9]) + countScore(a[10],a[11]);
        if(score_a > score_b)
            printf("SCORE: %d to %d, PLAYER 1 WINS.\n",score_a,score_b);
        else if(score_a < score_b)
            printf("SCORE: %d to %d, PLAYER 2 WINS.\n",score_a,score_b);
        else
            printf("SCORE: %d to %d, TIE.\n",score_a,score_b);
    }
    return 0;
}