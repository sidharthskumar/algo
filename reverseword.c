#include<stdio.h>

int main()
{
char a[30];
int i;


fgets(a,30,stdin);

printf("%c",a[strlen(a)]);
for(i=strlen(a)-1;i>=0;i--){


if (a[i]==' ') {a[i]='\0'; printf("%s",a[i+1]);}
}
for (i=0;i<1000;i++){
if (a[i]!=' ') printf("%c",a[i]);
else break;
}

return 0;


}
