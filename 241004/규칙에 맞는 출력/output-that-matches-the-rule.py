n=int(input())

for i in range(n):
    for j in range(n):
        if j<=i:
            print(n-i+j,end=" ")
    print()