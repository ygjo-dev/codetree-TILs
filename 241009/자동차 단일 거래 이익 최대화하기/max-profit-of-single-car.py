import sys
n=int(input())
arr=list(map(int,input().split()))

max_val=0
min_val=sys.maxsize

for idx in range(n):
    if arr[idx]<min_val:
        min_val=arr[idx]
    
    val= arr[idx]-min_val
    if val>max_val:
        max_val=val

print(max_val)