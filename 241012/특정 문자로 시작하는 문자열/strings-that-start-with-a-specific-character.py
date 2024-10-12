n=int(input())
arr= [input() for _ in range(n)]
c = input()

cnt=0
sum_val=0
for string in arr:
    if string[0]==c:
        cnt+=1
        sum_val+=len(string)

print(f"{cnt} {sum_val/cnt:.2f}")