n,q=tuple(map(int,input().split()))
arr=list(map(int,input().split()))

for _ in range(q):
    question_arr=list(map(int,input().split()))

    if question_arr[0]==1:
        a=question_arr[1]
        print(arr[a-1])
    elif question_arr[0]==2:
        b=question_arr[1]
        if b not in arr:
            print("0")
        else:
            print(arr.index(b)+1)
    elif question_arr[0]==3:
        s,e=question_arr[1], question_arr[2]
        print(s,e)
        #for n in arr[s-1:e]:
        #    print(n, end=" ")