print('문자열 입력')
S = input()
result = []
value = 0

for i in range(len(S)):
    if S[i].isalpha(): #이런 함수가 있네;;
        result.append(S[i])
    else:
        value += int(S[i])

result.sort()

if value > 0:
    result.append(str(value))

print(''.join(result)) #이 표현 기억해두자