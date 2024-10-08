import sys

n=int(input())
arr=list(map(int,input().split()))

min_val=sys.maxsize

for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            diff=arr[i]-arr[j]
        else:
            diff=arr[j]-arr[i]
        
        if diff<min_val:
            min_val=diff

print(min_val)