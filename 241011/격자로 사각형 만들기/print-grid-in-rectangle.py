n=int(input())

arr2d=[[1 for _ in range(n)] for _ in range(n)]

for i in range(1,n):
    for j in range(1,n):
        arr2d[i][j]=arr2d[i-1][j]+arr2d[i][j-1]+arr2d[i-1][j-1]

for i in range(n):
    for j in range(n):
        print(arr2d[i][j], end=" ")
    print()