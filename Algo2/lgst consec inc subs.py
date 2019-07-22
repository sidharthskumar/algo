
import heapq

try:
    k=int(input())
    n=int(input())
    st=[]

    for i in range(n):
        st.append(int(input()))
    #print (a.minmaxGasDist(st,k))

    st.sort()
    q = []
    n = len(st)
    for i in range(n-1):
        heapq.heappush(q, (st[i]-st[i+1], 1, i, i + 1))
    ans = q[0][0]
    while k:
        _, num, i, j = heapq.heappop(q)
        threshold = -q[0][0]
        cnt = int((st[j] - st[i]) / threshold) + 1
        x = min(k, cnt - num)
        k -= x
        heapq.heappush(q, (-1.0 * (st[j] - st[i]) / (num+x), num+x, i, j))
    #print (q)
    print(int(sum(q[0])))

except:
    pass