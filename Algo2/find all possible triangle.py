x=list(map(int,input().split()))
x.sort()
c=0
for i in range(len(x)-2):
    s=x[i]
    k=i+2
    for j in range(i+1,len(x)-2): # taking two pointer that is one at beggining and the other the next second one
                                    # so the next thrid elemtnt can be found be while loop having variable k
                                    #so we can also take triangles within i to k-1 moving j around as k-1-j
                                    #where k is the point where it stopped.
        s=x[i]+x[j]
        while( k<len(x) and s>x[k]):
            k+=1

        c=c+k-j-1
print(c)

