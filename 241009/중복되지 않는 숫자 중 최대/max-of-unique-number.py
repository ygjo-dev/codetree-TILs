N=int(input())

arr=list(map(int,input().split()))

new_arr=[]

for idx in range(N):
    cnt=0
    for n in arr[idx+1:]:
        if arr[idx]==n:
            cnt+=1
            break
    if cnt==0:
        new_arr.append(arr[idx])

if len(new_arr)==0:
    print(-1)
else:
    max_val=new_arr[0]
    for n in new_arr:
        if n>max_val:
            max_val=n
    print(max_val)