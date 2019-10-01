#include<cstdio>
#include<cstring>
#include<queue>
using namespace std;
int main() 
{
    int n,k,a[100002];
    queue<int> q;
	while(scanf("%d %d",&n,&k) == 2)
    {
		memset(a,0x7f,sizeof(a));
		q.push(n);
		a[n]=0;
		while (q.size()) 
        {
			if (q.front()*2 <= 100000 && a[q.front()*2] > a[q.front()] + 1) 
            {
				q.push(q.front()*2);
				a[q.front()*2] = a[q.front()] + 1;
				if(q.front()*2 == k)
                    break;
			}
			if (q.front()+1 <= 100000 && a[q.front() + 1] > a[q.front()] + 1) 
            {
				q.push(q.front() + 1);
				a[q.front() + 1] = a[q.front()] + 1;
				if(q.front() + 1 == k)
                    break;
			}
			if (q.front() - 1 >= 0 && a[q.front() - 1] > a[q.front()] + 1) 
            {
				q.push(q.front() - 1);
				a[q.front() - 1] = a[q.front()] + 1;
				if(q.front() - 1 == k)
                    break;
			}
			q.pop();
		}
		printf("%d\n",a[k]);
	}
	return 0;
}