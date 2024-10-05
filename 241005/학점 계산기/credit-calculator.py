n=int(input())

arr=list(map(float,input().split()))

sum_val=sum(arr)
average=sum_val/n

print(f"{average:.1f}")
if average>=4.0:
    print("Perfect")
elif average>=3.0:
    print("Good")
else:
    print("Poor")