a,b=input().split()
a,b=int(a),int(b)

arr=[0 for _ in range(10)]

while True:
    if a<=1:
        break
    arr[a%b]+=1
    a = a//b

ans=[i**2 for i in arr]

print(sum(ans))