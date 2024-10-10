n=int(input())

arr2d = [[0 for _ in range(n)] for _ in range(n)]

cnt=1

for j in range(n-1,-1,-1):
    if j%2!=0:
        for i in range(n-1,-1,-1):
            arr2d[i][j] = cnt
            cnt+=1
    if j%2==0:
        for i in range(n):
            arr2d[i][j] = cnt
            cnt+=1

for i in range(n):
    for j in range(n):
        print(arr2d[i][j],end=" ")
    print()