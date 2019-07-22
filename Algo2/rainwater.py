x=list(map(int,input().split()))
mx=x[0]
ml=[i for i in range(len(x))]
p=0
for i in x:
    if i>mx:
        ml[p]=i
        mx=i
        p+=1
        continue
    ml[p]=mx
    p+=1
y=[i for i in range(len(x))]
mx=x[-1]

for i in range(1,len(x)+1):
    if x[-i]>mx:
        mx=x[-i]
        y[-i]=mx
        continue
    y[-i]=mx
print(y,ml)
s=0
for i in range(0,len(x)):
    s=s+min(y[i],ml[i])-x[i]
print(s)