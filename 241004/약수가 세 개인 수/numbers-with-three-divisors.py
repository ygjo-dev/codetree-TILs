start,end=input().split()
start,end=int(start),int(end)

ans=0

for val in range(start, end+1):
    div_cnt=0
    for divisor in range(1,val+1):
        if val%divisor==0:
            div_cnt+=1
    if div_cnt==3:
        ans+=1
print(ans)