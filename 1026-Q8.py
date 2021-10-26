#문자열 재정렬
#알파벳 대문자와 숫자 0~9로만 구성된 문자열이 주어짐
#이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력

#입력조건
#첫 줄에 하나의 문자열 S가 주어짐

#출력조건 : 첫 줄에 요구하는 정답 출력

print('문자열 입력')
S = list(map(str, input()))

string = []
number = []

print(type(str(1)))

for i in range(len(S)):
    if S[i] == str(0):
        number.append(int(S[i]))
    elif S[i] == str(1):
        number.append(int(S[i]))
    elif S[i] == str(2):
        number.append(int(S[i]))
    elif S[i] == str(3):
        number.append(int(S[i]))
    elif S[i] == str(4):
        number.append(int(S[i]))
    elif S[i] == str(5):
        number.append(int(S[i]))
    elif S[i] == str(6):
        number.append(int(S[i]))
    elif S[i] == str(7):
        number.append(int(S[i]))
    elif S[i] == str(8):
        number.append(int(S[i]))
    elif S[i] == str(9):
        number.append(int(S[i]))
    else:
        string.append(str(S[i]))

print(string)
print(number)

string.sort() #문자부터 정렬

#숫자가 포함되어 있다면
if len(number) > 0:
    sum = 0
    for i in range(len(number)):
        sum += number[i]

    string.append(sum) #마지막에 합을 출력해야하기 때문에 마지막에 삽입

for i in string:
    print(i, end = '')

#자체 평가 : 먼저 string 리스트 선언 과정에서 str로 명명했다가 뒤 조건문과 충돌;;
#조금 지저분한 풀이가 아닌가..