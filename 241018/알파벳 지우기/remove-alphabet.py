str1=input()
str2=input()

str1_int=""
for elem in str1:
    if elem>='0' and elem<='9':
        str1_int+=elem

str2_int=""
for elem in str2:
    if elem>='0' and elem<='9':
        str2_int+=elem

print(int(str1_int)+int(str2_int))