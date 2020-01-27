#include<cstdio>
#include<iostream>
using namespace std;
long long b[12] = { 1, 10, 100, 1000, 10000, 100000, 1000000,10000000, 100000000, 1000000000, 10000000000, 100000000000 };
long long count_num (long long n,long long id );
int main() 
{
	long long a,b,count[10];
	int i;
	while(cin>>a>>b&&(a+b))
     {
		if(a>b)
        {
			long long tmp = a;
			a = b;
			b = tmp;
		}
		for(i=0; i<=9; i++)
			count[i] = count_num(b,i) - count_num(a - 1,i);
		for(i=0; i<9; i++) 
			cout<<count[i]<<" ";
		cout<<count[9]<<endl;
	}
}
long long count_num (long long n,long long id ) 
{
	long long left, m, sum = 0;
	for ( int i = 1; i < 12; i++ )
    {
		left = n / b[i] - (id==0);
		sum += left * b[i-1];
		m = (n % b[i] - n % b[i-1]) / b[i-1]; 
		if ( m > id ) 
            sum += b[i-1];
		else if (m == id) 
            sum += n % b[i-1] + 1;
		if ( n < b[i] )
            break;
	}
	return sum;
}