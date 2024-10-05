arr=list(map(int,input().split()))

for _ in range(len(arr)):
    if arr[-1]==0:
        arr.pop()
        continue
    print(arr.pop(),end=" ")