arr=list(map(int,input().split()))

cnt=0

for n in arr:
    if n==999 or n==-999:
        break
    else:
        cnt+=1

min_val=arr[0]
max_val=arr[0]
for n in arr[:cnt]:
    if n>max_val:
        max_val=n
    if n<min_val:
        min_val=n

print(max_val, min_val)