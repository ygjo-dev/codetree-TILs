A=input()
B=input()

cnt=0
while True:
    if cnt==len(A):
        print("-1")
        break
    else:
        A=A[-1]+A[:-1]
        cnt+=1
        if A==B:
            print(cnt)
            break