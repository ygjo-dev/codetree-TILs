a,b,c=input().split()
a,b,c=int(a),int(b),int(c)

if a>=b and a<=c or a>=c and a<=b:
    print(a)
if b>=a and b<=c or b>=c and b<=a:
    print(b)
if c>=a and c<=b or c>=b and c<=a:
    print(c)