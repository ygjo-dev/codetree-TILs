n, m = tuple(map(int,input().split()))

arr2d_1 = [list(map(int,input().split())) for _ in range(n)]
arr2d_2 = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr2d_1[i][j]==arr2d_2[i][j]:
            print("0",end= " ")
        else:
            print("1",end=" ")
    print()