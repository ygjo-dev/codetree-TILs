n=int(input())

for i in range(n):
    for _ in range(n-i,1,-1):
        print(" ",end="")
    for _ in range(2*i+1):
        print("*",end="")
    print()

for i in range(n-1):
    for _ in range(i+1):
        print(" ",end="")
    for _ in range(2*(n-1-i)-1):
        print("*",end="")
    print()