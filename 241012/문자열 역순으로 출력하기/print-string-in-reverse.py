string = [
	input()
	for _ in range(4)
]

# 입력받은 문자열을 역순으로 출력합니다.
for s in string[-1::-1]:
    print(s)