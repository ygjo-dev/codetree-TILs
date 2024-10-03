n = int(input())

for i in range(n):
    for j in range(n):
        if i==0:
            print("*",end=" ")
        
        if i!=0:
            if j%2!=0 and i<=j:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()