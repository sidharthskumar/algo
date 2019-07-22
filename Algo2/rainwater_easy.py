x=[10,4,3,11,13,5,6,12,7]


s=[1 for i in range(len(x))]

for i in range(len(x)):
    j=0
    while(i!=j):
        if x[j]+1==x[i]:
            s[i]=max(s[j]+1,s[i])
            j+=1
        else:
            j+=1

print (s)