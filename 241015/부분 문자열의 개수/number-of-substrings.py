A=input()
B=input()

cnt=0
for idx in range(len(A)-len(B)+1):
    if A[idx:idx+len(B)]==B:
        cnt+=1

print(cnt)