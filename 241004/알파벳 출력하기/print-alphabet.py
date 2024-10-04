n =int(input())

cnt='A'
for i in range(n):
    for j in range(i+1):
        print(cnt,end="")        
        if cnt=='Z':
            cnt='A'
            continue
        cnt=chr(ord(cnt)+1)
    print()