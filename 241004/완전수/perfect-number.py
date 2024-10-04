start,end=input().split()
start,end=int(start),int(end)

cnt=0
for num in range(start,end+1):
    sum_val=0
    for n in range(1,num):
        if num%n==0:
            sum_val+=n
    if num==sum_val:
        cnt+=1
print(cnt)