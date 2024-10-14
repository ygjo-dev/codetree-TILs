string=input()

arr=[]
cnt=0

for elem in string:
    if len(arr)==0:
        arr.append(elem)
        cnt+=1
        continue
    if elem != arr[-1]:
        arr.append(cnt)
        arr.append(elem)
        cnt=0
    
    if elem ==arr[-1]:
        cnt+=1
arr.append(cnt)

ans=0
for elem in arr:
    if type(elem) != str:
        ans+=len(str(elem))
    else:
        ans+=len(elem)
print(ans)
for elem in arr:
    print(elem,end="")