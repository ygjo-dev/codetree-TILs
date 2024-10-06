n=int(input())

ans=[]
ans.append(1)
ans.append(n)

while True:
    n=ans[-2]+ans[-1]
    ans.append(n)
    if n>100:
        break

for n in ans:
    print(n,end=" ")