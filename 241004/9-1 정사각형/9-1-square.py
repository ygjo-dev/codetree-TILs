n=int(input())

cnt=9
for _ in range(n):
    for _ in range(n):
        print(cnt, end="")
        cnt-=1
        if cnt==0:
            cnt=9
    print()