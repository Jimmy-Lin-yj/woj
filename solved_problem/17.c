#include <stdio.h> 
#include <math.h> 
double distance( int m0, int n0, int m1, int n1 )
{
	return sqrt( pow((m0 - m1), 2) + pow((n0 - n1), 2) );   
}
double min( int x0, int y0, int x1, int y1, int x2, int y2)
{
    double a, b, c, cosA;
    a = distance( x0, y0, x1, y1);    
    b = distance( x0, y0, x2, y2);     
	c = distance( x1, y1, x2, y2);
	cosA = (b*b + c*c - a*a) / (2.0*b*c);
    return 2*b*c*(1-cosA*cosA)/a; 
}
int main()
{
    int num;
    while(scanf("%d", &num)!=EOF) 
    { 
        for(int i=0; i<num; i++)  
        { 
          double len = 0;
          int t[3][2]; 
          for(int j=0; j<3; j++)   
              scanf("%d %d", &t[j][0], &t[j][1]); 
          len = min(t[0][0], t[0][1], t[1][0], t[1][1], t[2][0], t[2][1]);
          printf("%4.3f\n", len);  
        } 
    }
	return 0;
}
