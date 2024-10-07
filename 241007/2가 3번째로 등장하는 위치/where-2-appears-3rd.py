n=int(input())
arr=list(map(int,input().split()))

cnt=0
ans=0
for idx in range(n):
    if arr[idx]==2:
        cnt+=1
        ans=idx
    
    if cnt==3:
        break

print(ans+1)