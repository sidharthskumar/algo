#include<stdio.h>

int main()
{
int jumps,i,n,j,a[100],x,l,s;
scanf("%d",&n);

for(i=0;i<n;i++) scanf("%d",&a[i]);

x=a[0];
s=a[0];
j=0;

for(l=1;l<n;l++){

if (l+a[i]>x) x=l+a[i];

s--;

if (s==0){ j++;s=x-l;}

}

printf("%d",j);
return 0;

}
