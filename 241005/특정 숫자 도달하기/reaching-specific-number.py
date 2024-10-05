arr = list(map(int,input().split()))

sum_val=0
cnt=0

for n in arr:
    if n>=250:
        break
    else:
        sum_val+=n
        cnt+=1

print(f"{sum_val} {sum_val/cnt:.1f}")