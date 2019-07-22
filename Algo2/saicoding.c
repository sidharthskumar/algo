#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int minimum(int a,int b,int c){
printf("a %d  b %d  c %d",a,b,c);
if (a>b && a>c){printf("%d\n",a);
 return a;}
if (b>a && b>c) {printf("%d\n",b);return b;}
else {printf("%d\n",c);return c;}


}
int find(char *a,char *b,int al,int bl){int i,j;
int t[al+1][bl+1];

for(int i=0;i<al;i++){

	for(int j=0;j<bl;j++){

		if (i==0) t[0][j]=j;
		else if (j==0) t[i][0]=i;
		else  if (a[i-1]==b[j-1]) t[i][j]=t[i-1][j-1];
      else t[i][j]=1+minimum(t[i-1][j],t[i-1][j-1],t[i][j-1]);








		}
	}

  for(int i=0;i<al;i++) {

  	for(int j=0;j<bl;j++) {
        printf("   ans%d -->i%d j%d",t[i][j],i,j ); }printf("\n" );}
return t[al][bl];



}

int main()
{

char a[]="sunday";
char b[]="saturday";
int al=6,bl=8;

//scanf("%s",&a);
//scanf("%s",&b);


int ans=find(a,b,strlen(a),strlen(b));
printf("%d\n",ans );

return 0;
}
