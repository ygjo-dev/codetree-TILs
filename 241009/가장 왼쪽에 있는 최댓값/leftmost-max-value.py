N=int(input())
arr=list(map(int,input().split()))

max_idx=N
while True:
    max_val=arr[0]
    for n in arr[:max_idx]:
        if n>max_val:
            max_val=n
    
    max_idx=arr.index(max_val)

    print(max_idx+1, end=" ")
    if (max_idx+1)==1:
        break