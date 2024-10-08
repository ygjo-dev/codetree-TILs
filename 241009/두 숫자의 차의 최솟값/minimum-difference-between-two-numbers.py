import sys

n=int(input())
arr=list(map(int,input().split()))

min_val=sys.maxsize

for i in range(1,n):
    val=arr[i]-arr[i-1]
    if val<min_val:
        min_val=val

print(min_val)