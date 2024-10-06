n=int(input())
ans=[0 for _ in range(10)]

arr = list(map(int,input().split()))

for n in arr:
    ans[n]+=1

for n in ans[1:]:
    print(n)