string=input()

c1=string[0]
c2=string[1]
for idx in range(len(string)):
    if string[idx]==c2:
        string = string[:idx] + c1 + string[idx+1:]
print(string)