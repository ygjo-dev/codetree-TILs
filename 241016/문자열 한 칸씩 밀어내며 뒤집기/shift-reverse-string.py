string, q = input().split()
q=int(q)

ans=list(string)
for _ in range(q):
    question=int(input())
    if len(ans)==1:
        print(''.join(ans))
        continue

    if question==1:
        ans=ans[1:]+[ans[0]]
        print(''.join(ans))
    elif question==2:
        ans=[ans[-1]]+ans[:-1]
        print(''.join(ans))
    elif question==3:
        for idx in range(len(ans)//2):
            temp=ans[idx]
            ans[idx]=ans[len(ans)-1-idx]
            ans[len(ans)-1-idx]=temp
        print(''.join(ans))