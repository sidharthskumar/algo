#include<stdio.h>
#include<stdlib.h>

struct node{
int data;
struct node *next;
struct node *prev;
};

typedef struct node* p;

int main()
{p head,temp,t,current,end;
  int n,total;
head=NULL;
scanf("%d",&n);

while(n--){
scanf("%d",&total);
while(total--){
if (head==NULL){
t=(p)malloc(sizeof(struct node));
head=t;
t->prev=NULL;
t->next=NULL;
//printf("enter for first node\n");
scanf("%d\n",&t->data );
}
else{
temp=(p)malloc(sizeof(struct node));
//printf("etner data");
scanf("%d",&temp->data);
t->next=temp;
temp->next=NULL;
temp->prev=t;
t=temp;
}
}
}
end=t;
while(t->prev!=NULL){
current=t->next;
t->next=t->prev;
t->prev=current;
t=t->prev;
}
current=t->next;
t->next=NULL;
t->prev=current;
end->prev=NULL;
printf("rev\n");
while(end->next!=NULL){

printf("%d\n",end->data);
end=end->next;
}




  return 0;
}
