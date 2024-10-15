string1=input()
string2=input()

ans=-1
len1=len(string1)
len2=len(string2)
for idx in range(len1-len2+1):
    if string1[idx:idx+len2]==string2[::]:
        ans=idx
        break

print(ans)