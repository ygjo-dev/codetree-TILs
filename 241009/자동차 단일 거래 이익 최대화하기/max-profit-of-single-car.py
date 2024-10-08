import sys
n=int(input())
arr=list(map(int,input().split()))

min_idx=0
min_val=sys.maxsize
for idx in range(n):
    if arr[idx] < min_val:
        min_val=arr[idx]
        min_idx=idx

max_idx=0
max_val=-sys.maxsize
for i in range(min_idx,n):
    if arr[i] > max_val:
        max_val=arr[i]
        max_idx=i

if max_idx>min_idx:
    print(max_val-min_val)
else:
    print(0)