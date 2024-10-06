ans=[0 for _ in range(4)]
for _ in range(3):
    state, temp = input().split()

    temp=float(temp)

    if state =='Y' and temp>=37:
        ans[0]+=1
    elif state=='N' and temp>=37:
        ans[1]+=1
    elif state=='Y':
        ans[2]+=1
    else:
        ans[3]+=1

for n in ans:
    print(n,end=" ")
if ans[0]>=2:
    print("E")