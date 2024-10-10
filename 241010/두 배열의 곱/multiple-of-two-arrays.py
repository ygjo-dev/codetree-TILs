arr2d_1 = [list(map(int,input().split())) for _ in range(3)]
trash = input()
arr2d_2 = [list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(arr2d_1[i][j]*arr2d_2[i][j], end=" ")
    print()