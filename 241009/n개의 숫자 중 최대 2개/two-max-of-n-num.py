import sys

N=int(input())
arr=list(map(int,input().split()))


new_arr=[]

for _ in range(N):
    max_val=-sys.maxsize
    for n in arr:
        if n in new_arr:
            continue
        
        if n>max_val:
            max_val=n
    
    new_arr.append(max_val)


print(new_arr[0], new_arr[1])