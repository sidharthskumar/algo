x=input().strip() #karappa input -------- for 2 ans 4 && for 3 ans 5 #longest substring with m unique characters in a given string
i=1
n=int(input("n?"))
j=0
d={x[j]:1}
m=0
while(i<len(x)):

    if d.get(x[i],0) ==0:
        d[x[i]]=1
    else:
        d[x[i]]+=1

    if len(d)>n:
        print(d)
        di= x[j]
        print("b4 llooop",x[j])

        print("di is ",di)
        while(x[j]==di):
            j+=1
        print("after llooop",x[j])
        print("before del dic",d)
        del d[di]

        print("after del dic",d)

        d[x[j]]=1
        #i+=1
    print(j,i)
    if abs(i-j)>m:
        m=abs(i-j)
    i+=1
print(d)
print(m+1)




