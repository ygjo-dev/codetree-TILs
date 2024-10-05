arr=list(map(int,input().split()))

idx=0
for n in arr:
    if n == 0:
        break
    idx+=1

for n in arr[idx-1::-1]:
    print(n,end=" ")