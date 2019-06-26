	a=list(map(int,input().split()))

	def bsearch(l,r,t):
	    m=int((l+r)/2)
	    print(a[m])
	    if a[m]==t:
		print('found')
		return 1
	    if l<=r:
		if a[m]>t:
		    r=m
		    bsearch(l,r,t)
		else:
		    l=m+1
		    bsearch(l,r,t)
	    else:
		return -1


	bsearch(0,len(a)-1,4)
