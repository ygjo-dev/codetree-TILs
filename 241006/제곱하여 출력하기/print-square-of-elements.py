n=int(input())

arr=list(map(int,input().split()))

ans=[n**2 for n in arr]

for n in ans:
    print(n,end=" ")