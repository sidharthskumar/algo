a=list(map(int,input().strip().split()))
for i in range(len(a)):
#	print(sum(a[:i]),sum(a[i+1:]))
	if sum(a[:i])==sum(a[i+1:]):
		print(i)
