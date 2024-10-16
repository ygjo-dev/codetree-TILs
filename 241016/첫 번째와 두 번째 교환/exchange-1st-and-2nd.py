string=input()

arr=list(string)

c1=arr[0]
c2=arr[1]

ans=""
for elem in arr:
    if elem == c1:
        ans+=c2
    elif elem == c2:
        ans+=c1
    else:
        ans+=elem

print(ans)