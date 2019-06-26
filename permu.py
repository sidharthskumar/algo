def per(s):
    if len(s)==0:
        return []
    if len(s)==1:
        return [s]
    else:
        l=[]
        for i in range(len(s)):
            x=s[i]
            xs=s[:i]+s[i+1:]
            for k in per(xs):
                l.append(x+k)
        return l




print(per('abc'))
