n,m=tuple(map(int,input().split()))

arr2d = [[0 for _ in range(m)] for _ in range(n)]

cnt=0
for j in range(m):
    if j%2==0:
        for i in range(0,n):
            arr2d[i][j] = cnt
            cnt+=1
    else:
        for i in range(n-1,-1,-1):
            arr2d[i][j] = cnt
            cnt+=1

for i in range(n):
    for j in range(m):
        print(arr2d[i][j], end=" ")
    print()