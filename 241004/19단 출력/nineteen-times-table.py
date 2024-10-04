for i in range(1,20):
    cnt = 0
    for j in range(1,20):
        cnt+=1
        if cnt%2!=0:
            if j==19:
                print(f"{i} * {j} = {i*j}", end="\n")
            else:                
                print(f"{i} * {j} = {i*j}", end=" / ")                
        else:
            print(f"{i} * {j} = {i*j}", end="\n")