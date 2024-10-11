n, m = tuple(map(int,input().split()))

arr2d=[[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c = tuple(map(int,input().split()))
    arr2d[r-1][c-1] = 1

for i in range(n):
    for j in range(n):
        print(arr2d[i][j], end=" ")
    print()