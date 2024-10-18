str1, str2 = tuple(input().split())

str1_int=""
for elem in str1:
    if elem.isdigit():
        str1_int+=elem
    else:
        break

str2_int=""
for elem in str2:
    if elem.isdigit():
        str2_int+=elem
    else:
        break
print(int(str1_int)+int(str2_int))