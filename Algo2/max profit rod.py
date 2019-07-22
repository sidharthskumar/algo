
# cutting the rod to maximize the profit for eg- 0 2 5 9 6 is the profit cuorresponding to
# cutting the rod in 0 1 2 3 4 leghts of pieces..


x=list(map(int,input().split()))
dp=[[0,0,0,0,0,0] for i in range(5)]
for i in range(5):
 for j in range(6):
  if i==0:
   continue
  if j==0:
   continue
  if i>j:
   dp[i][j]=dp[i-1][j]
  else:
   dp[i][j]=max(dp[i-1][j],dp[i][j-i]+x[i])

print(str(i) for i in dp)
