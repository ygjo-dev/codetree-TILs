arr=[]
while True:
    string=input()
    if string=='0':
        break
    else:
        arr.append(string)

print(len(arr))
for idx in range(len(arr)):
    if (idx+1)%2!=0:
        print(arr[idx])