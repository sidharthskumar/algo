def maxnonadj(n):
    i=n[0]
    e=0
    for i in range(1,len(n)):
        i=max(e+n[i],i)
        e=i
    print(max(e,i))
    print(n)

maxnonadj([4,1,1,4,2,1])
