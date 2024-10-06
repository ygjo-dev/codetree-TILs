arr=list(map(int,input().split()))

cnt=0
for n in arr:
    if n==0:
        break
    cnt+=1

ans=[0 for _ in range(10)]

for n in arr[:cnt]:
    ans[n//10]+=1

for idx in range(1,10):
    print(f"{idx} - {ans[idx]}")