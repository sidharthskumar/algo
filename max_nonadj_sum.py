def maxnonadj(n):
    inc=n[0]  #inclu
    exl=0		#exclu
    for i in range(1,len(n)):
        new_exclusive=max(inc,exl)
        inc=exl+n[i]
        exl=new_exclusive
    print(n)
    print(max(inc,exl))



maxnonadj([5, 5, 10, 100, 10, 5])
