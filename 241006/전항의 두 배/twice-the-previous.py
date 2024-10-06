ans=list(map(int,input().split()))

for _ in range(8):
    ans.append(ans[-2]*2+ans[-1])

for n in ans:
    print(n,end=" ")