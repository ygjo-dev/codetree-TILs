h,w=input().split()
h,w=int(h),int(w)

b=(10000*w)/(h*h)
print(f"{int(b)}")
if b>=25:
    print("Obesity")