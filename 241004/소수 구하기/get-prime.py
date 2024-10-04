num=int(input())


for n in range(1,num+1):
    div_cnt=0
    for divisor in range(1,n+1):
        if n%divisor==0:
            div_cnt+=1
    if div_cnt==2:
        print(n,end=" ")