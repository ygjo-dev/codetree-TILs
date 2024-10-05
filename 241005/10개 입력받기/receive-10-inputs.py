arr=list(map(int,input().split()))

cnt=0
for n in arr:
    if n==0:
        break
    else:
        cnt+=1

sum_val=sum(arr[:cnt])
avg=sum_val/(cnt)

print(f"{sum_val} {avg:.1f}")