
#dp
#find max score if starting from a[0] and end at last.. if no hop just add the score at a[i]
#if one hop skip the hopeed one and add 2*a[i] to sum if 2 hop 1 * * 2 then 3*a[i] add to score
# unlimited single hop but inly 1 2 hop find max sore input - 6 and 4,5,6,7,4,5 gives 35.
n=int(input())
a=list(map(int,input().split(',')))
dp=[[0,0,0] for _ in range(n+1)]
for i in range(1,n+1):
    if i<=2:
        dp[i][0]=dp[i][1]=a[i-1]

    if i>2:
        dp[i][0]=max(dp[i-1][2]+a[i-1],dp[i-2][-1]+a[i-1]*2)
        dp[i][1]=max(dp[i-1][1]+a[i-1],dp[i-2][1]+a[i-1]*2)
        dp[i][2]=max(0,dp[i-3][1]+a[i-1]*3)

print(dp)