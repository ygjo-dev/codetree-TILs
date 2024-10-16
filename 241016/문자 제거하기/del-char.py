arr=list(input())

while True:
    if len(arr)==1:
        break
    
    n=int(input())
    if n>=len(arr):
        arr.pop(-1)
    else:
        arr.pop(n)
    print(''.join(arr))