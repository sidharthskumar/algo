x=[3,4,-1,0,6,2,3]
t=[1 for i in range (len(x))]
j=0
for i in range(1,len(x)):
    j=0
    while i!=j:
        if x[j]<x[i]:
            t[i]=max(t[j]+1,t[i])
            j+=1
        else:
            j+=1
        print(t[i])
print (t)
