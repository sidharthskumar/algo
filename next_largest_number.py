try:
    test = int(input())
    while (test):
        test-=1
        s=0
        l=int(input())
        #x=[int(i) for i in range(1,l+1)]
        #print(x)
        s=5
        if l==1:
            print(1)
            continue
        if l==2:
            print(5)
            continue
        for i in range(3, l+1):
            t=s+s*i+i
            s=t
        print(s%((10**9)+7))
except:
    pass