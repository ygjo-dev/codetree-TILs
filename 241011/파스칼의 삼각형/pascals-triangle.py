n=int(input())

arr2d=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr2d[i][0] = 1

for i in range(1,n):
    for j in range(1,n):
        arr2d[i][j] = arr2d[i-1][j-1] + arr2d[i-1][j]
    
for i in range(n):
    for j in range(n):
        if arr2d[i][j]!=0:
            print(arr2d[i][j], end=" ")
    print()