b,a = input().split()
b,a=int(b),int(a)

if b%2==0:
    b-=1
for i in range(b,a-1,-2):
    print(i,end=' ')