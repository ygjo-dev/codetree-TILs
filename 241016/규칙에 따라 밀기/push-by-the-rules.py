A=input()
command=list(input())

for elem in command:
    if elem == 'L':
        A=A[1:]+A[0]
    elif elem == 'R':
        A=A[-1]+A[:-1]
    
 
print(A)