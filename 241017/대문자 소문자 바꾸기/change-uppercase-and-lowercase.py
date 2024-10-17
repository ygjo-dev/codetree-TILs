string=input()

for s in string:
    if s >= 'A' and s <= 'Z':
        print(s.lower(),end="")
    elif s >='a' and s<='z':
        print(s.upper(),end="")