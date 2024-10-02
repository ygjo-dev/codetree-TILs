N=int(input())

cnt=1
while True:
    N=N//2
    cnt+=1
    if N==2:
        print(N)
        break
print(cnt)