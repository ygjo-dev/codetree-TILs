arr=list(map(int,input().split()))

for _ in range(0,8):
    arr.append((arr[-1]+arr[-2])%10)

for n in arr:
    print(n,end=" ")