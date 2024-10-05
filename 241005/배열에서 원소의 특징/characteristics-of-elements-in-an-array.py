arr=list(map(int,input().split()))

cnt=0
for n in arr:
    if n%3==0:
        break
    cnt+=1

print(arr[cnt-1])