a,b=input().split()
a,b=int(a),int(b)

if a%2==0:
    a+=1
for i in range(a,b+1,2):
    print(i,end=' ')