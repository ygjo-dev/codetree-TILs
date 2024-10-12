a=input()
b=input()
c=input()

arr=[]
arr.append(len(a))
arr.append(len(b))
arr.append(len(c))

print(max(arr)-min(arr))