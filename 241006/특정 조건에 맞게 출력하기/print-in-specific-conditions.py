arr=list(map(int,input().split()))

cnt=0
for n in arr:
    if n==0:
        break
    cnt+=1

for idx in range(cnt):
    n=arr[idx]
    if n%2==0:
        print(n//2,end=" ")
    else:
        print(n+3,end=" ")