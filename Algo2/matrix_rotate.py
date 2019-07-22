a=[[i for i in range(0,4)] for k in range(0,4)]
for i in range(0,4):
    for k in range(0,4):
        a[i][k]=int(input())


print(len(a))
b=[[i for i in range(0,4)] for k in range(0,4)]



for i in range(len(a)):
    for j in range(len(a)):

        b[len(a)-1-j][i]=a[i][j]

print(b)