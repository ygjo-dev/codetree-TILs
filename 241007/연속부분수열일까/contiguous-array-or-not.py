n1,n2=tuple(map(int,input().split()))

A=list(map(int,input().split()))
B=list(map(int,input().split()))

ans=False

b_idx=0
for a_idx in range(n1):
    if B[b_idx] == A[a_idx]:
        b_idx+=1
    else:
        b_idx=0

if b_idx==n2:
    ans=True

print("Yes" if ans else "No")