import sys

N=int(input())
arr=list(map(int,input().split()))


new_arr=[]
idx_arr=[]
for _ in range(N):
    max_val=-sys.maxsize
    max_idx=-sys.maxsize
    for idx in range(N):
        if idx in idx_arr:
            continue
        
        if arr[idx]>max_val:
            max_val=arr[idx]
            max_idx=idx
    
    new_arr.append(max_val)
    idx_arr.append(max_idx)


print(new_arr[0], new_arr[1])