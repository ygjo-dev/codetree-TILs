n=int(input())

for _ in range(n):
    a,b=input().split()
    a,b=int(a),int(b)

    sum_val=0
    for num in range(a,b+1):
        if num%2==0:
            sum_val+=num
    print(sum_val)