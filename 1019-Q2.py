#곱하기 혹은 더하기
#각 자리가 숫자로만 이루어진 문자열 S가 주어졌을 때 왼쪽부터 하나씩 확인하며 숫자 사이에 곱셈 또는 덧셈을 넣어 결과값이 가장 큰 수 찾기
#입력 조건
#첫 줄에 여러 숫자로 구성된 하나의 문자열 S가 주어짐

#출력 조건 : 만들어질 수 있는 가장 큰 수를 출력

print('넘버 스트링 입력')
N = list(map(int, input()))

print(N)

result = 0

for i in range(len(N)):
    if result == 0:
        result += N[i]
    else:
        if N[i] == 0 or N[i] == 1:
            result += N[i]
        else:
            result *= N[i]

print(result)

#자체 평가 : 아이디어 자체가 심플했고 구현하는데 큰 어려움이 없었음
#0과 1인 경우는 덧셈 그외에는 곱셈 처리
#처음 스트링 입력을 받을 때 이를 split 없이 list로 받는 방법이 주효했음