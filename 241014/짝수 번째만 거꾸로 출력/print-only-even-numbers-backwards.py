string=input()

for idx in range(len(string)-1,-1,-1):
    if idx%2!=0:
        print(string[idx],end="")