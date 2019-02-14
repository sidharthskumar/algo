#include<stdio.h>
#include<stdlib.h>
struct node {
int data;
struct node *next;
};


typedef struct node* n;

int main()
{int a,b;
n p,head,temp;

p=(n)malloc(sizeof(struct node));

printf("enter total nodes \nenter the first number");
scanf("%d",&a);
scanf("%d",&p->data);
head=p;
printf("%d",p->data);
p->next=NULL;

while(a--){
printf("enter the data of %d",a);
temp=(n)malloc(sizeof(struct node));
p->next=temp;
scanf("%d",&temp->data);
p=temp;
temp->next=NULL;}
p=head;
while(p->next!=NULL){printf("%d",p->data); p=p->next;}





return 0;
}
