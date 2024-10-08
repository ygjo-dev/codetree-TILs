arr=list(map(int,input().split()))

max_val=arr[0]

for n in arr[1:]:
    if max_val<n:
        max_val=n

print(max_val)