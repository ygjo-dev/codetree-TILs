n=int(input())
string=input().split()

string_val=""

for elem in string:
    string_val+=elem

cnt=0
for elem in string_val:
    print(elem,end="")
    cnt+=1
    if cnt%5==0:
        print()