n,m=tuple(map(int,input().split()))

arr2d= [[0 for _ in range(m)] for _ in range(n)]

cnt=1

main_row, main_col=0,0

while True:
    if main_row == n-1 and main_col == m-1:
        arr2d[main_row][main_col] = cnt
        break

    row = main_row
    for col in range(main_col,-1,-1):
        arr2d[row][col] = cnt
        cnt+=1
        row+=1

        if row > n-1:
            break

        if arr2d[row][col] != 0:
            continue  
    
    if main_col==m-1 and main_row < n-1:
        main_row+=1
    if main_col < m-1:
        main_col+=1

for i in range(n):
    for j in range(m):
        print(arr2d[i][j], end=" ")
    print()