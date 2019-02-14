t=int(input())
while t>0:
    t-=1
    a=list(map(int,input().strip().split()))
    ans=a[0]
    for i in range(len(a)):
        cs=a[i]
        s=cs
        for j in range(i+1,len(a)):
            if s+a[j]>cs:
                cs=s+a[j]
                continue
                #print(cs)

            s=s+a[j]
        ans=max(ans,cs)


    print(ans)