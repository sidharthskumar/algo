
#a person from back can bribe a person in front and form a seq like 12354 where 5 bribed , find minimum swaps if swaps>2 its chaotic

tt=int(input())
while tt>0:
        tt -= 1
        adsf=input()
        x=list(map(int,input().rstrip().split()))
        c=0
        no=0
        for i in range(len(x)-1,-1,-1):
            skip=0
          #  print(x)
            if i==1:
                if x[1]!=2:
                    c+=1
                    break
            else:
               # print(x)
                if x[i]!=i+1:
                    if x[i-1]==i+1:
                        skip=1

                       # print(skip)
                    if x[i-2]==i+1:
                        skip=2
                    if skip!=1 and skip!=2:
                        #print('%d %d', x[i-1],i+1)
                        skip=3
                #(skip)
                if skip==3:
                    print('Too chaotic')
                    no=1
                    break
                else:
                    while skip:
                        t=x[i-skip]
                        x[i-skip]=x[i-skip+1]
                        x[i-skip+1]=t
                        skip-=1
                        c+=1

        if no!=1:
            print(c)



