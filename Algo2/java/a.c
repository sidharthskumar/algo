#include<stdio.h>
unsigned getValue (unsigned num, unsigned m, unsigned n){ return ((num >> (m+1-n)&~(~0<<n)));}




int main()


{

//printf("%d",getValue(100,5,3));


int a=~(~0<<3);
int b=3;

int d=b&a;
int c=100>>d;

printf("a %d b %d c %d",a,b,c);


return 0;
}


/*
unsigned getValue(unsigned num, unsigned m, unsigned n){return((num >> (m+1 – n)&~(~0<<n));}
*/
