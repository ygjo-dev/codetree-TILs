string=input()

curr_char=""
num_char=0

save_string=""
save_len=0
for elem in string:
    if curr_char=="":
        curr_char=elem
        num_char=1
        continue
    if elem != curr_char:
        save_len+=len(curr_char)+len(str(num_char))
        save_string+= curr_char+str(num_char)
        curr_char=elem
        num_char=1
    else:
        num_char+=1

save_len+=len(curr_char)+len(str(num_char))
save_string+= curr_char+str(num_char)
print(save_len)
print(save_string)