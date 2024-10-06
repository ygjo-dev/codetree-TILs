n=int(input())

arr=list(map(int,input().split()))

ans=[]
for n in arr:
    if n%2==0:
        ans.append(n)

for n in ans:
    print(n,end=" ")