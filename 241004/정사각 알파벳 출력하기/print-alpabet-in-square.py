n=int(input())

cnt=0
for _ in range(n):
    for _ in range(n):
        print(chr(ord('A')+cnt),end="")
        cnt+=1
    print()