#include<stdio.h>
int main(){
	int no,in;
	float p,win;
	scanf("%d",&no);
	for(int j =0;j<no;j++){
		scanf("%d",&in);
        getchar();
		p = (float)in/100;
		win = (float)p*p/(1-2*p+2*p*p)*100;
		printf("%.2f%c\n",win,'%');
	}
	return 0;
}