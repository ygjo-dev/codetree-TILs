string=input()

cnt1=0
cnt2=0
for idx in range(len(string)-1):
    if string[idx:idx+2]=='ee':
        cnt1+=1
    elif string[idx:idx+2]=='eb':
        cnt2+=1

print(cnt1,cnt2)