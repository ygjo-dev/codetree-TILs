A=list(input())
B=list(input())

while True:
    have_deleted=False

    for idx in range(len(A)-len(B)+1):
        if A[idx:idx+len(B)]==B[::]:
            A=A[:idx]+A[idx+len(B):]
            have_deleted=True

    if have_deleted==False:
        print(''.join(A))
        break