n1,n2=tuple(map(int,input().split()))

A=list(map(int,input().split()))
B=list(map(int,input().split()))

ans=True

prev_idx=-1
curr_idx=-1
for b in B:
    if b not in A:
        ans=False
    else:
        if curr_idx-1!=prev_idx:
            curr_idx=A.index(b)   

        if prev_idx>=0:
            if b!=A[curr_idx]:
                ans=False
        
        prev_idx=curr_idx
        curr_idx+=1


print("Yes" if ans else "No")