n=int(input())

sum_val=0
for _ in range(n):
    sum_val+=int(input())

ans=str(sum_val)
ans= ans[1:]+ans[0]
print(ans)