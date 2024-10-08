import sys

N=int(input())

arr=list(map(int,input().split()))

max_val=-sys.maxsize
for n in arr:
    if n>max_val:
        cnt=0
        for m in arr:
            if n==m:
                cnt+=1
        
        if cnt==1:
            max_val=n

print(max_val)