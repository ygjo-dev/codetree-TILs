n,m=tuple(map(int,input().split()))

arr2d=[[0 for _ in range(m)] for _ in range(n)]

cnt=1
for i in range(n):
    for j in range(m):
        arr2d[i][j] = cnt
        cnt+=1

for i in range(n):
    for j in range(m):
        print(arr2d[i][j],end=" ")
    print()