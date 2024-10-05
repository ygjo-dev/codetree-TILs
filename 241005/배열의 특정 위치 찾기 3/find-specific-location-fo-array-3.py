arr=list(map(int,input().split()))

cnt=0
for n in arr:
    if n==0:
        break
    else:
        cnt+=1

filtered_arr=arr[:cnt]

sum_val=0
for idx in range(-1,-4,-1):
    sum_val+=filtered_arr[idx]

print(sum_val)