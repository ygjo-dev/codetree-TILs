import sys
n=int(input())
arr=list(map(int,input().split()))

min_val=sys.maxsize

for i in range(n):
    for j in range(i+1,n):
        val=arr[i]-arr[j]
        if val>0:
            continue
        if val<min_val:
            min_val=val

if min_val>=0:
    print(0)
else:
    print(min_val)