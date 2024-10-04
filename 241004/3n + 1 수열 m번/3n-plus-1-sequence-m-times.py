m=int(input())

n=[]
for _ in range(m):
    cnt=0
    n.append(int(input()))

for idx in range(len(n)):
    while True:
        if n[idx]%2==0:
            n[idx] /=2
            cnt+=1
        else:
            n[idx] = 3*n[idx]+1
            cnt+=1
        if n[idx]==1:
            break
    print(cnt)