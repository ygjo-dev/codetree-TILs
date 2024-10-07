n1,n2=tuple(map(int,input().split()))

A=list(map(int,input().split()))
B=list(map(int,input().split()))

ans=True

idx=-1
for b in B:
    if b not in A:
        ans=False
    else:
        if idx==-1:
            idx=A.index(b)        
        else:
            if b!=A[idx]:
                ans=False
        idx+=1

print("Yes" if ans else "No")