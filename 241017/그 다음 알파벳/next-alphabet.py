c=input()

ans=chr(ord(c)+1)

if ord(ans)>ord('z'):
    ans='a'

print(ans)