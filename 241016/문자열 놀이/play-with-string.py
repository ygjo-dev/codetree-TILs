s, q = input().split()
q=int(q)

ans=list(s)
for _ in range(q):
    arr=list(input().split())

    if arr[0]=='1':
        temp=ans[int(arr[1])-1]
        ans[int(arr[1])-1]=ans[int(arr[2])-1]
        ans[int(arr[2])-1]=temp
    elif arr[0]=='2':
        for idx in range(len(ans)):
            if ans[idx] == arr[1]:
                ans[idx]=arr[2]
    print(''.join(ans))